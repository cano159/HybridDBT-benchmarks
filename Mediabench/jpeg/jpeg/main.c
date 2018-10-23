#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <math.h>

#include <string.h>

#include "bitmap.h"
#include "dct.h"
#include "jpegenc.h"

/*
RGB to YCbCr Conversion:
*/
// Y = 0.299*R + 0.587*G + 0.114*B
color RGB2Y(const color r, const color g, const color b)
{
	return (32768 + 19595*r + 38470*g + 7471*b) >> 16;
}
// Cb = 128 - 0.1687*R - 0.3313*G + 0.5*B
color RGB2Cb(const color r, const color g, const color b)
{
	return (8421376 - 11058*r - 21709*g + 32767*b) >> 16;
}
// Cr = 128 + 0.5*R - 0.4187*G - 0.0813*B
color RGB2Cr(const color r, const color g, const color b)
{
	return (8421376 + 32767*r - 27438*g - 5329*b) >> 16;
}


#define CHECK(n) (((n) < 0)? 0: (((n) > 255)? 255: (n)))

inline color YCbCr2R(const conv y, const conv cb, const conv cr) {
	conv ret = y + 1.402 * (cr - 128);
	return CHECK(ret);
}

inline color YCbCr2G(const conv y, const conv cb, const conv cr) {
	conv ret = y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128);
	return CHECK(ret);
}

inline color YCbCr2B(const conv y, const conv cb, const conv cr) {
	conv ret = y + 1.772 * (cb - 128);
	return CHECK(ret);
}

void correct_color(conv data[8][8]) {
	unsigned r, c;

	for (r = 0; r < 8; r++)
		for (c = 0; c < 8; c++) {
			conv p = data[r][c];

			if (p < 0)
				p = 0;
			if (p > 255)
				p = 255;

			data[r][c] = p;
		}
}

static FILE* file_jpg = 0;

void write_jpeg(const unsigned char buff[], const unsigned size) {
	fwrite(buff, size, 1, file_jpg);
}

static void dump(conv data[], FILE *file) {
	for (unsigned i = 0; i < 64; i++) {
		fwrite(data + zig[i], sizeof(conv), 1, file);
	}
}

static void recalc_qtab(unsigned div, const unsigned char qtab[8][8], int t) {
	unsigned r, c;

	for (r = 0; r < 8; r++) {
		printf("{");
		for (c = 0; c < 8; c++) {
			unsigned n = (div * 2 + qtab[r][c]) / (qtab[r][c] * 2);
			printf("%3d,", t ? n : div / n);
		}
		printf("},\n");
	}
	printf("\n");
}


extern const unsigned char qtable_paint_lum[8][8];
extern const unsigned char qtable_paint_chrom[8][8];


//// chroma subsampling, i.e. converting a 16x16 RGB block into 8x8 Cb and Cr
void subsample(const BGR rgb[16][16], conv cb[8][8], conv cr[8][8]) {
	for (unsigned r = 0; r < 8; r++)
		for (unsigned c = 0; c < 8; c++) {
			unsigned rr = (r << 1);
			unsigned cc = (c << 1);

			// calculating an average values
			color R = (rgb[rr][cc].Red + rgb[rr][cc + 1].Red
					+ rgb[rr + 1][cc].Red + rgb[rr + 1][cc + 1].Red) >> 2;
			color G = (rgb[rr][cc].Green + rgb[rr][cc + 1].Green
					+ rgb[rr + 1][cc].Green + rgb[rr + 1][cc + 1].Green) >> 2;
			color B = (rgb[rr][cc].Blue + rgb[rr][cc + 1].Blue
					+ rgb[rr + 1][cc].Blue + rgb[rr + 1][cc + 1].Blue) >> 2;

			cb[r][c] = (conv) RGB2Cb(R, G, B) - 128;
			cr[r][c] = (conv) RGB2Cr(R, G, B) - 128;
		}
}

void subsample2(const BGR rgb[16][16], conv Y[2][2][8][8], conv cb[8][8],
		conv cr[8][8]) {
	unsigned r, c;

	for (r = 0; r < 16; r += 2)
		for (c = 0; c < 16; c += 2) {
			//unsigned rr, cc;
			unsigned i, j, k, l;
			unsigned sR, sG, sB;
			unsigned R, G, B;

			i = r >> 3, j = c >> 3, k = r & 7, l = c & 7;

			sR = R = rgb[r][c].Red, sG = G = rgb[r][c].Green, sB = B =
					rgb[r][c].Blue;
			Y[i][j][k][l] = RGB2Y(R, G, B) - 128;

			sR += R = rgb[r][c + 1].Red, sG += G = rgb[r][c + 1].Green, sB +=
					B = rgb[r][c + 1].Blue;
			Y[i][j][k][l + 1] = RGB2Y(R, G, B) - 128;

			sR += R = rgb[r + 1][c].Red, sG += G = rgb[r + 1][c].Green, sB +=
					B = rgb[r + 1][c].Blue;
			Y[i][j][k + 1][l] = RGB2Y(R, G, B) - 128;

			sR += R = rgb[r + 1][c + 1].Red, sG += G = rgb[r + 1][c + 1].Green, sB +=
					B = rgb[r + 1][c + 1].Blue;
			Y[i][j][k + 1][l + 1] = RGB2Y(R, G, B) - 128;

			// calculating an average values
			R = sR >> 2, G = sG >> 2, B = sB >> 2;

			//rr = r >> 1, cc = c >> 1;

			cb[r >> 1][c >> 1] = (conv) RGB2Cb(R, G, B) - 128;
			cr[r >> 1][c >> 1] = (conv) RGB2Cr(R, G, B) - 128;
		}
}

void subsample3(const color R[16][16], const color G[16][16],
		const color B[16][16], conv Y[2][2][8][8], conv cb[8][8],
		conv cr[8][8]) {
	unsigned r, c;

	for (r = 0; r < 16; r += 2)
		for (c = 0; c < 16; c += 2) {
			//unsigned rr, cc;
			unsigned i, j, k, l;
			unsigned sR, sG, sB;
			unsigned R1, G1, B1;

			i = r >> 3, j = c >> 3, k = r & 7, l = c & 7;

			sR = R1 = R[r][c], sG = G1 = G[r][c], sB = B1 = B[r][c];
			Y[i][j][k][l] = RGB2Y(R1, G1, B1) - 128;

			sR += R1 = R[r][c + 1], sG += G1 = G[r][c + 1], sB += B1 = B[r][c
					+ 1];
			Y[i][j][k][l + 1] = RGB2Y(R1, G1, B1) - 128;

			sR += R1 = R[r + 1][c], sG += G1 = G[r + 1][c], sB += B1 =
					B[r + 1][c];
			Y[i][j][k + 1][l] = RGB2Y(R1, G1, B1) - 128;

			sR += R1 = R[r + 1][c + 1], sG += G1 = G[r + 1][c + 1], sB += B1 =
					B[r + 1][c + 1];
			Y[i][j][k + 1][l + 1] = RGB2Y(R1, G1, B1) - 128;

			// calculating an average values
			R1 = sR >> 2, G1 = sG >> 2, B1 = sB >> 2;

			cb[r >> 1][c >> 1] = (conv) RGB2Cb(R1, G1, B1) - 128;
			cr[r >> 1][c >> 1] = (conv) RGB2Cr(R1, G1, B1) - 128;
		}
}



int main(int argc, char *argv[]) {

	if (argc != 3) {
		printf("Incorrect arguments, usage is jpegenc input.bmp output.jpeg\n");
		return -1;
	}



	if (!Load(argv[1])) {
		fprintf(stdout, "Error: cannot open %s\n", argv[1]);
		return -1;
	}

	if (GetBitCount() != 24) {
		fprintf(stdout, "Error BitCount != 24 : %d\n", GetBitCount());
		return -1;
	}

	BGR RGB16x16[16][16];
	color R[16][16], G[16][16], B[16][16];
	conv Y8x8[2][2][8][8]; // four 8x8 blocks - 16x16
	conv Cb8x8[8][8];
	conv Cr8x8[8][8];

	if (!(file_jpg = fopen(argv[2], "w"))) {
		printf("Error: cannot create jpeg file\n");
		return -1;
	}

	// Process image by 16x16 blocks, (16x16 because of chroma subsampling)
	// The resulting image will be truncated on the right/down side
	// if its width/height is not multiple of 16.
	// The data is written into <file_jpg> file by write_jpeg() function
	// which Huffman encoder uses to flush its output, so this file
	// should be opened before the call of huffman_start().

	huffman_start(GetHeight() & -16, GetWidth() & -16);

	for (unsigned y = 0; y < GetHeight() - 15; y += 16) {
		for (unsigned x = 0; x < GetWidth() - 15; x += 16) {
			if (!GetBlock_bgr(x, y, 16, 16, (BGR*) RGB16x16)) {
				printf("Error: getBlock(%d,%d)\n", x, y);
				break;
			}
//			printf("%x, %x\n", x, y);
			// getting subsampled Cb and Cr
			subsample2(RGB16x16, Y8x8, Cb8x8, Cr8x8);
			//subsample3(R, G, B, Y8x8, Cb8x8, Cr8x8);

			dct8x8(Y8x8[0][0], Y8x8[0][0]);	// 1 Y-transform
			dct8x8(Y8x8[0][1], Y8x8[0][1]);	// 2 Y-transform
			dct8x8(Y8x8[1][0], Y8x8[1][0]);	// 3 Y-transform
			dct8x8(Y8x8[1][1], Y8x8[1][1]);	// 4 Y-transform
			dct8x8(Cb8x8, Cb8x8);				// Cb-transform
			dct8x8(Cr8x8, Cr8x8);				// Cr-transform



			huffman_encode(HUFFMAN_CTX_Y, (short*)Y8x8[0][0]);
			huffman_encode(HUFFMAN_CTX_Y, (short*)Y8x8[0][1]);
			huffman_encode(HUFFMAN_CTX_Y, (short*)Y8x8[1][0]);
			huffman_encode(HUFFMAN_CTX_Y, (short*)Y8x8[1][1]);
			huffman_encode(HUFFMAN_CTX_Cb, (short*)Cb8x8);
			huffman_encode(HUFFMAN_CTX_Cr, (short*)Cr8x8);
		}
	}

	huffman_stop();



	return 0;
}

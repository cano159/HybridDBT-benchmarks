#ifndef __JPEG_H__
#define __JPEG_H__


typedef unsigned char color;
typedef short conv;

/*
RGB to YCbCr Conversion:
*/
// Y = 0.299*R + 0.587*G + 0.114*B
color RGB2Y(const color r, const color g, const color b);
// Cb = 128 - 0.1687*R - 0.3313*G + 0.5*B
color RGB2Cb(const color r, const color g, const color b);
// Cr = 128 + 0.5*R - 0.4187*G - 0.0813*B
color RGB2Cr(const color r, const color g, const color b);

// quantization table
//extern const unsigned char qtable_lum[64];
//extern const unsigned char qtable_chrom[64];
extern const unsigned char zig[64];

void quantization_lum(conv data[64]);
void quantization_chrom(conv data[64]);
void iquantization_lum(conv data[64]);
void iquantization_chrom(conv data[64]);

void correct_color(conv data[8][8]);

//---------------- J P E G ---------------

// Application should provide this function for JPEG stream flushing
void write_jpeg(const unsigned char buff[], const unsigned size);

//void write_APP0info(void);
// should set width and height before writing
//void write_SOF0info(const short height, const short width);
//void write_SOSinfo(void);
//void write_DQTinfo(void);
//void write_DHTinfo(void);

typedef struct huffman_s
{
	const unsigned char  (*haclen)[12];
	const unsigned short (*hacbit)[12];
	const unsigned char  *hdclen;
	const unsigned short *hdcbit;
	const unsigned char  *qtable;
	short                dc;
}
huffman_t;

extern huffman_t huffman_ctx[3];

#define	HUFFMAN_CTX_Y	&huffman_ctx[0]
#define	HUFFMAN_CTX_Cb	&huffman_ctx[1]
#define	HUFFMAN_CTX_Cr	&huffman_ctx[2]

void huffman_start(short height, short width);
void huffman_stop(void);
void huffman_encode(huffman_t *const ctx, const short data[64]);


#endif//__JPEG_H__

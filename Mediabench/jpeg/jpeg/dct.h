#ifndef __DCT_H__
#define __DCT_H__

#ifdef __cplusplus
extern "C" {
#endif

#define PI 3.1416


void dct8x8(short pixel[8][8], short data[8][8]);

typedef int Q11 ;


#ifdef __cplusplus
}
#endif


#endif//__DCT_H__

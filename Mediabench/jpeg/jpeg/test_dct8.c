#include<stdio.h>
#include<math.h>


float insample8[] = {1.0, 13.0, 5.0, 45.0, 24.0, 9.0, 12.0, 24.0};
int insample8_fixed[] = {1, 13, 5, 45, 24, 9, 12, 24};
float refsample8[] = {81.31, -9.85, -29.55, -44.71, 51.61, 6.4, -43.6, -13.0};


void print_vector(char* mess, float* in) {
	int i,j;
	printf("\nVector %s :\n",mess);
	for (i=0;i<8;i++) {
		printf("%f ",in[i]);
	}
	printf("\n");
	fflush(stdout);
}


extern void fast_fixed_dct8(int in[8], int out[8]);

int main() {
	float float_output[8];
	int fixed_output[8];
	float float_input[8];

	int i=0;


	fast_fixed_dct8(insample8_fixed, fixed_output);

	return fixed_output[7];
}

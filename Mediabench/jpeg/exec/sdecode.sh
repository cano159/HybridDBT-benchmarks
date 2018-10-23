#!/bin/sh -f
BENCHMARK=jpeg/jpeg-6a/bin/djpeg
INPUT=
OUTPUT=
ARGS=-dct int -ppm -outfile ../data/testout.ppm ../data/testimg.jpg

NAME=djpeg
BENCH_OPT="-dct int -ppm"
BENCH_INP=../data/testimg.jpg
BENCH_OUT="-outfile ../data/testout.ppm"
BENCH_ARG="${BENCH_OPT} ${BENCH_OUT} ${BENCH_INP}"
#

#simRISCV -f ../../build/jpeg/jpeg-6a/bin/djpeg -a "-dct int -ppm -outfile ../data/testout.ppm ../data/testimg.jpg"
 
 

dbt -f ../../build/jpeg/jpeg-6a/bin/djpeg -O 5 -c 0 -coef 90 -type 1 -o test -- -dct int -ppm -outfile ../data/testout.ppm ../data/testimg.jpg

#!/bin/sh -f
BENCHMARK=jpeg/jpeg/bin/jpegenc
INPUT=
OUTPUT=
ARGS=../jpeg/data/brueghel.bmp test.jpeg

BENCH_BIN=../../build/jpeg/jpeg-6a/bin/cjpeg
BENCH_OPT="-dct int -progressive -opt"
BENCH_INP=../data/testimg.ppm
BENCH_OUT="-outfile ../data/testout.jpeg"
BENCH_ARG="${BENCH_OPT} ${BENCH_OUT} ${BENCH_INP}"
#
#simRISCV -f ../jpeg/jpegenc -a "../jpeg/data/brueghel.bmp test.jpeg"
dbt -f ../jpeg/jpegenc -O 4 -c 9 -- ../jpeg/data/brueghel.bmp test.jpeg

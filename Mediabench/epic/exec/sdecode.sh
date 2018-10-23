#!/bin/sh -f
BENCHMARK=epic/src/bin/unepic
INPUT=
OUTPUT=
ARGS=../data/test.image.pgm.E


BENCH_BIN=../../build/epic/src/bin/unepic
BENCH_OPT=
BENCH_INP=../data/test.image.pgm.E
BENCH_OUT=
BENCH_ARG="${BENCH_INP} ${BENCH_OPT} ${BENCH_OUT}"
#
#simRISCV -f ${BENCH_BIN} -a"../data/test.image.pgm.E" 

dbt -f ${BENCH_BIN} -O 5 -c 0 -coef 90 -- ../data/test.image.pgm.E

	


#!/bin/sh -f
BENCHMARK=epic/src/bin/epic
INPUT=
OUTPUT=
ARGS=../data/test_image.pgm -b 25

BENCH_BIN=../../build/epic/src/bin/epic
BENCH_OPT="-b 25"
BENCH_INP=../data/test_image.pgm
BENCH_OUT=
BENCH_ARG="${BENCH_INP} ${BENCH_OPT} ${BENCH_OUT}"
#simRISCV -f ${BENCH_BIN} -a "../data/test_image.pgm -b 25"
gdb --args dbt -f ${BENCH_BIN} -c 2 -O 4 -- ../data/test_image.pgm -b 25

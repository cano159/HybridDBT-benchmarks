#!/bin/sh -f
BENCHMARK=g721/src/bin/decode
INPUT=
OUTPUT=
ARGS=-4 -l -f ../data/clinton.g721

BENCH_BIN=../../build/g721/src/bin/decode
BENCH_OPT="-4 -l -f"
BENCH_INP=../data/clinton.g721
BENCH_OUT=
BENCH_ARG="${BENCH_OPT} ${BENCH_INP}"
#
simRISCV -f ${BENCH_BIN} -a "${BENCH_ARG}"
#dbt -f ${BENCH_BIN} -O 2 -c 2 -- ${BENCH_ARG}






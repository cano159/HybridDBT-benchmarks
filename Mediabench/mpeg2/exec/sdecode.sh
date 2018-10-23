#!/bin/sh -f
BENCHMARK=mpeg2/src/mpeg2dec/bin/mpeg2dec
INPUT=
OUTPUT=
ARGS=-b ../data/mei16v2.m2v -r -f -o ../data/tmpc2%d

NAME=mpeg2decode
BENCH_BIN=../../build/mpeg2/src/mpeg2dec/bin/mpeg2dec
BENCH_OPT="-r -f -o"
BENCH_INP="-b ../data/mei16v2.m2v"
BENCH_OUT="../data/tmpc2%d"
BENCH_ARG="${BENCH_INP} ${BENCH_OPT} ${BENCH_OUT}"
#
#simRISCV -f ${BENCH_BIN} -a "${BENCH_ARG}"
dbt -f ${BENCH_BIN} -O 4 -c 2 -o test -- ${BENCH_ARG}


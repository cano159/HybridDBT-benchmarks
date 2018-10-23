#!/bin/sh -f
BENCHMARK=mpeg2/src/mpeg2dec/bin/mpeg2enc
INPUT=
OUTPUT=
ARGS= ../data/out.m2v ../data/options.par

NAME=mpeg2enc
BENCH_BIN=../../build/mpeg2/src/mpeg2enc/bin/mpeg2enc
BENCH_OPT="../data/options.par"
BENCH_INP="../data/out.m2v"
BENCH_OUT=
BENCH_ARG="${BENCH_OPT} ${BENCH_INP} ${BENCH_OUT}"
#
echo simRISCV -f ${BENCH_BIN} -a "${BENCH_ARG}"
echo dbt -f ${BENCH_BIN} -O 2 -c 0 -- ${BENCH_ARG}
dbt -f ${BENCH_BIN} -O 2 -c 0 -- ${BENCH_ARG}

#!/bin/sh -f
BENCHMARK=gsm/src/bin/toast
INPUT=
OUTPUT=
ARGS=-fpl ../data/clinton.pcm

BENCH_BIN=../../build/gsm/src/bin/toast
BENCH_OPT="-fpl"
BENCH_INP=../data/clinton.pcm
BENCH_OUT=
BENCH_ARG="${BENCH_OPT} ${BENCH_INP}"
#

simRISCV -f ${BENCH_BIN} -a "${BENCH_ARG}"
#dbt -f ${BENCH_BIN} -O 2 -c 2 -- ${BENCH_ARG}


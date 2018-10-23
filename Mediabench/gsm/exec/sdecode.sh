#!/bin/sh -f
BENCHMARK=gsm/src/bin/untoast
INPUT=
OUTPUT=../data/clinton.pcm.run
ARGS=-fpl ../data/clinton.pcm.run.gsm

BENCH_BIN=../../build/gsm/src/bin/untoast
BENCH_OPT="-fpl"
BENCH_INP=../data/clinton.pcm.run.gsm
BENCH_OUT=../data/clinton.pcm.run
BENCH_ARG="${BENCH_OPT} ${BENCH_INP}"
#

simRISCV -f ${BENCH_BIN} -a "${BENCH_ARG}" 
#dbt -f ${BENCH_BIN} -O 4 -c 2 -v 5 -- ${BENCH_ARG}





#!/bin/sh 
BENCHMARK=g721/src/bin/encode
INPUT=
OUTPUT=
ARGS=-4 -l -f ../data/clinton.pcm

BENCH_BIN=../../build/g721/src/bin/encode
BENCH_OPT="-4 -l -f"
BENCH_INP=../data/clinton.pcm
BENCH_OUT=
BENCH_ARG=${BENCH_OPT} ${BENCH_INP}
#
#simRISCV -f ${BENCH_BIN} -a "-4 -l -f ../data/clinton.pcm"
dbt -f ${BENCH_BIN} -c 0 -O 5 -- -4 -l -f ../data/clinton.pcm

#!/bin/sh -f
BENCHMARK=adpcm/src/bin/rawcaudio
INPUT=../data/clinton.pcm
OUTPUT=../results/out.adpcm
ARGS=
#
#simRISCV -f ${BENCHMARK} -i ${INPUT} -o ${OUTPUT}
dbt -O 4 -c 2 -f ${BENCHMARK} -i ${INPUT} -o ${OUTPUT} -v 5

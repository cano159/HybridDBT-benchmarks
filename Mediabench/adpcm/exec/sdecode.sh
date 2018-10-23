#!/bin/sh -f
BENCHMARK=adpcm/src/bin/rawdaudio
INPUT=../data/clinton.adpcm
OUTPUT=../results/out.pcm
ARGS=
#



dbt -f ${BENCHMARK} -i ${INPUT} -o ${OUTPUT} -c 0 -O 5 -coef 90 -type 1
#simRISCV -f ${BENCHMARK} -i ${INPUT} -o ${OUTPUT}

#echo emulator-freechips.rocketchip.system-DefaultConfig pk ../../build/adpcm/src/bin/rawdaudio < ../data/clinton.adpcm > ../results/out.pcm



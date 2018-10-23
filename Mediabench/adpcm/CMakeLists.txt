add_subdirectory(src)


add_test(NAME test_adpcm_encode_conf2  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 13 -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawcaudio -i ../data/clinton.pcm -o ../results/out.adpcm) 
add_test(NAME test_adpcm_decode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 13 -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawdaudio -i ../data/clinton.adpcm -o ../results/out.pcm) 


#set(previousConf 0)
#foreach(conf 0 1 2)

#add_test(NAME test_adpcm_encode_conf${conf}  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawcaudio -i ../data/clinton.pcm -o ../results/out.adpcm) 
#add_test(NAME test_adpcm_decode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawdaudio -i ../data/clinton.adpcm -o ../results/out.pcm) 

#if (NOT ${conf} EQUAL 0)
#	SET_TESTS_PROPERTIES ( test_adpcm_encode_conf${previousConf} PROPERTIES DEPENDS test_adpcm_encode_conf${conf})
#	SET_TESTS_PROPERTIES ( test_adpcm_decode_conf${previousConf} PROPERTIES DEPENDS test_adpcm_decode_conf${conf})
#endif(NOT ${conf} EQUAL 0)

#set(previousConf ${conf})

#endforeach(conf)


#add_test(NAME test_adpcm_encode_reconf  WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawcaudio -i ../data/clinton.pcm -o ../results/out.adpcm) 
#add_test(NAME test_adpcm_decode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rawdaudio -i ../data/clinton.adpcm -o ../results/out.pcm) 

#SET_TESTS_PROPERTIES ( test_adpcm_encode_conf${previousConf} PROPERTIES DEPENDS test_adpcm_encode_reconf)
#SET_TESTS_PROPERTIES ( test_adpcm_decode_conf${previousConf} PROPERTIES DEPENDS test_adpcm_decode_reconf)


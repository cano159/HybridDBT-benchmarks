
set(GSM_BASE ${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(src)

add_test(NAME test_gsm_encode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -c 2 -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/toast -- -fpl ./data/clinton.pcm) 
add_test(NAME test_gsm_decode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -c 2 -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/untoast -- -fpl ./data/clinton.pcm.run.gsm) 


#set(previousConf 0)
#foreach(conf 0 1 2)
#add_test(NAME test_gsm_encode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/toast -- -fpl ./data/clinton.pcm) 
#add_test(NAME test_gsm_decode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/untoast -- -fpl ./data/clinton.pcm.run.gsm) 

#if (NOT ${conf} EQUAL 0)
#	SET_TESTS_PROPERTIES ( test_gsm_encode_conf${previousConf} PROPERTIES DEPENDS test_gsm_encode_conf${conf})
#	SET_TESTS_PROPERTIES ( test_gsm_decode_conf${previousConf} PROPERTIES DEPENDS test_gsm_decode_conf${conf})
#endif(NOT ${conf} EQUAL 0)

#set(previousConf ${conf})

#endforeach(conf)

#add_test(NAME test_gsm_encode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/toast -- -fpl ./data/clinton.pcm) 
#add_test(NAME test_gsm_decode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/untoast -- -fpl ./data/clinton.pcm.run.gsm) 
#	SET_TESTS_PROPERTIES ( test_gsm_encode_conf${previousConf} PROPERTIES DEPENDS test_gsm_encode_reconf)
#	SET_TESTS_PROPERTIES ( test_gsm_decode_conf${previousConf} PROPERTIES DEPENDS test_gsm_decode_reconf)


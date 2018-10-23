add_subdirectory(src/mpeg2enc)
add_subdirectory(src/mpeg2dec)

add_test(NAME test_mpeg2_decode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 2 -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/mpeg2dec/bin/mpeg2dec -- -b ../data/mei16v2.m2v -r -f -o ../data/tmp%d)


#set(previousConf 0)
#foreach(conf 0 1 2)
#add_test(NAME test_mpeg2_encode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/mpeg2enc/bin/mpeg2enc -- ../data/options.par ../data/out.m2v)
#add_test(NAME test_mpeg2_decode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -c 2 -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/mpeg2dec/bin/mpeg2dec -- -b ../data/mei16v2.m2v -r -f -o ../data/tmp%d)

#if (NOT ${conf} EQUAL 0)
#	SET_TESTS_PROPERTIES ( test_mpeg2_encode_conf${previousConf} PROPERTIES DEPENDS test_mpeg2_encode_conf${conf})
#	SET_TESTS_PROPERTIES ( test_mpeg2_decode_conf${previousConf} PROPERTIES DEPENDS test_mpeg2_decode_conf${conf})
#endif(NOT ${conf} EQUAL 0)

#set(previousConf ${conf})

#endforeach(conf)

#add_test(NAME test_mpeg2_encode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/mpeg2enc/bin/mpeg2enc -- ../data/options.par ../data/out.m2v)
#add_test(NAME test_mpeg2_decode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt  -O 3 -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/mpeg2dec/bin/mpeg2dec -- -b ../data/mei16v2.m2v -r -f -o ../data/tmp%d)

#SET_TESTS_PROPERTIES ( test_mpeg2_encode_conf${previousConf} PROPERTIES DEPENDS test_mpeg2_encode_reconf)
#SET_TESTS_PROPERTIES ( test_mpeg2_decode_conf${previousConf} PROPERTIES DEPENDS test_mpeg2_decode_reconf)


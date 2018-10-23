add_subdirectory(src)

add_test(NAME test_epic_decode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -c 2   -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/unepic -- ./data/test.image.pgm.E) 
add_test(NAME test_epic_encode_conf2 WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -c 2   -O 2 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/epic -- ./data/test_image.pgm) 


#set(previousConf 0)
#foreach(conf 0 1 2)
#add_test(NAME test_epic_decode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -c 2   -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/unepic -- ./data/test.image.pgm.E) 
#add_test(NAME test_epic_encode_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -c 2   -O ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/epic -- ./data/test_image.pgm) 

#if (NOT ${conf} EQUAL 0)
#	SET_TESTS_PROPERTIES ( test_epic_decode_conf${previousConf} PROPERTIES DEPENDS test_epic_decode_conf${conf})
#	SET_TESTS_PROPERTIES ( test_epic_encode_conf${previousConf} PROPERTIES DEPENDS test_epic_encode_conf${conf})
#endif(NOT ${conf} EQUAL 0)

#set(previousConf ${conf})

#endforeach(conf)

#add_test(NAME test_epic_decode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -O 3  -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/unepic -- ./data/test.image.pgm.E) 
#add_test(NAME test_epic_encode_reconf WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/ COMMAND dbt -O 3  -c 0 -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/epic -- ./data/test_image.pgm) 
#SET_TESTS_PROPERTIES ( test_epic_decode_conf${previousConf} PROPERTIES DEPENDS test_epic_decode_reconf)
#SET_TESTS_PROPERTIES ( test_epic_encode_conf${previousConf} PROPERTIES DEPENDS test_epic_encode_reconf)



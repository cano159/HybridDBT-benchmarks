add_subdirectory(src)

#set(previousConf 0)
#foreach(conf 0 2 13)
#add_test(NAME test_rasta_conf${conf} WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/test/ COMMAND dbt -c ${conf} -f ${CMAKE_CURRENT_BINARY_DIR}/src/bin/rasta -i ex5_c1.wav -o ex5.asc -o stderr -o rasta.shade -- -z -A -J -S 8000 -n 12 -f map_weights.dat) 

#if (NOT ${conf} EQUAL 0)
#	SET_TESTS_PROPERTIES ( test_rasta_conf${previousConf} PROPERTIES DEPENDS test_rasta_conf${conf})
#endif(NOT ${conf} EQUAL 0)

#set(previousConf ${conf})

#endforeach(conf)

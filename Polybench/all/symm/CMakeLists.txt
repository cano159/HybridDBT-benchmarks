include_directories(./ ../../utilities/)
add_executable(symm symm.c ../../utilities/polybench.c)

set_target_properties(symm PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

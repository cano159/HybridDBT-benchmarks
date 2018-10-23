include_directories(./ ../../utilities/)
add_executable(lu lu.c ../../utilities/polybench.c)

set_target_properties(lu PROPERTIES COMPILE_DEFINITIONS "SMALL_DATASET")

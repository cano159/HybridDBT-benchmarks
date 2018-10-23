include_directories(./ ../../utilities/)
add_executable(syr2k syr2k.c ../../utilities/polybench.c)

set_target_properties(syr2k PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

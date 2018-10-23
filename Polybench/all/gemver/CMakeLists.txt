include_directories(./ ../../utilities/)
add_executable(gemver gemver.c ../../utilities/polybench.c)

set_target_properties(gemver PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

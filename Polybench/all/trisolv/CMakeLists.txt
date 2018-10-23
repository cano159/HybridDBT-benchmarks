include_directories(./ ../../utilities/)
add_executable(trisolv trisolv.c ../../utilities/polybench.c)

set_target_properties(trisolv PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

include_directories(./ ../../utilities/)
add_executable(atax 	atax.c ../../utilities/polybench.c)

set_target_properties(atax PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

include_directories(./ ../../utilities/)
add_executable(jacobi-1d jacobi-1d.c ../../utilities/polybench.c)

set_target_properties(jacobi-1d PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

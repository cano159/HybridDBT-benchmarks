include_directories(./ ../../utilities/)
add_executable(jacobi-2d jacobi-2d.c ../../utilities/polybench.c)

set_target_properties(jacobi-2d PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")


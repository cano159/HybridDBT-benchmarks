include_directories(./ ../../utilities/)
add_executable(seidel-2d seidel-2d.c ../../utilities/polybench.c)

set_target_properties(seidel-2d PROPERTIES COMPILE_DEFINITIONS "SMALL_DATASET")

include_directories(./ ../../utilities/)
add_executable(ludcmp ludcmp.c ../../utilities/polybench.c)

set_target_properties(ludcmp PROPERTIES COMPILE_DEFINITIONS "SMALL_DATASET")

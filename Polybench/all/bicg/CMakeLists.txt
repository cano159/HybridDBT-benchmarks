include_directories(./ ../../utilities/)
add_executable(bicg bicg.c ../../utilities/polybench.c)

set_target_properties(bicg PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

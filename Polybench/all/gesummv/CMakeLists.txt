include_directories(./ ../../utilities/)
add_executable(gesummv gesummv.c ../../utilities/polybench.c)

set_target_properties(gesummv PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")

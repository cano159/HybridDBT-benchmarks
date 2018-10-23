include_directories(./ ../../utilities/)
add_executable(correlation correlation.c ../../utilities/polybench.c)

set_target_properties(correlation PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

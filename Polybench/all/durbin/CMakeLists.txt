include_directories(./ ../../utilities/)
add_executable(durbin durbin.c ../../utilities/polybench.c)

set_target_properties(durbin PROPERTIES COMPILE_DEFINITIONS "LARGE_DATASET")



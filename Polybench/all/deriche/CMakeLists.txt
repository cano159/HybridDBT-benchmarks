include_directories(./ ../../utilities/)
add_executable(deriche deriche.c ../../utilities/polybench.c)

set_target_properties(deriche PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

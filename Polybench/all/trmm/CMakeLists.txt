include_directories(./ ../../utilities/)
add_executable(trmm trmm.c ../../utilities/polybench.c)

set_target_properties(trmm PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

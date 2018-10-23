include_directories(./ ../../utilities/)
add_executable(syrk syrk.c ../../utilities/polybench.c)

set_target_properties(syrk PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

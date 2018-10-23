include_directories(./ ../../utilities/)
add_executable(3mm 3mm.c ../../utilities/polybench.c)
set_target_properties(3mm PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")


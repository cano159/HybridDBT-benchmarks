include_directories(./ ../../utilities/)
add_executable(2mm 2mm.c ../../utilities/polybench.c)

set_target_properties(2mm PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

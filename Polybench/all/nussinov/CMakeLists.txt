include_directories(./ ../../utilities/)
add_executable(nussinov nussinov.c ../../utilities/polybench.c)

set_target_properties(nussinov PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

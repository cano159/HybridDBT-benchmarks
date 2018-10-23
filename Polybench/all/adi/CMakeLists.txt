include_directories(./ ../../utilities/)
add_executable(adi adi.c ../../utilities/polybench.c)

set_target_properties(adi PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

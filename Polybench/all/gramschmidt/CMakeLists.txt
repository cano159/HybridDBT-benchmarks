include_directories(./ ../../utilities/)
add_executable(gramschmidt gramschmidt.c ../../utilities/polybench.c)

set_target_properties(gramschmidt PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

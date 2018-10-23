include_directories(./ ../../utilities/)
add_executable(cholesky cholesky.c ../../utilities/polybench.c)

set_target_properties(cholesky PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

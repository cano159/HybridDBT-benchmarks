include_directories(./ ../../utilities/)
add_executable(covariance covariance.c ../../utilities/polybench.c)

set_target_properties(covariance PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

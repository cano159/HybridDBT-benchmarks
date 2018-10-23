include_directories(./ ../../utilities/)
add_executable(fdtd-2d fdtd-2d.c ../../utilities/polybench.c)

set_target_properties(fdtd-2d PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")


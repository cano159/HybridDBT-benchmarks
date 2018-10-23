include_directories(./ ../../utilities/)
add_executable(heat-3d heat-3d.c ../../utilities/polybench.c)

set_target_properties(heat-3d PROPERTIES COMPILE_DEFINITIONS "SMALL_DATASET")

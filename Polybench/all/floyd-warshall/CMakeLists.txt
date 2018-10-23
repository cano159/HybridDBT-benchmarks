include_directories(./ ../../utilities/)
add_executable(floyd-warshall floyd-warshall.c ../../utilities/polybench.c)

set_target_properties(floyd-warshall PROPERTIES COMPILE_DEFINITIONS "SMALL_DATASET")

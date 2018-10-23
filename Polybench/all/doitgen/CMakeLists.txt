include_directories(./ ../../utilities/)
add_executable(doitgen doitgen.c ../../utilities/polybench.c)

set_target_properties(doitgen PROPERTIES COMPILE_DEFINITIONS "MEDIUM_DATASET")

cmake_minimum_required (VERSION 3.5)


set(CMAKE_C_COMPILER riscv64-unknown-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER riscv64-unknown-linux-gnu-g++)


project (HybridDBT_testbench)

set(CMAKE_C_FLAGS "-O3 -static -DSMALL_DATASET -DDATA_TYPE_IS_INT")
set(CMAKE_CXX_FLAGS "-O3 -static -DSMALL_DATASET -DDATA_TYPE_IS_INT")


link_libraries("-lm")

set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ./bin)

add_subdirectory(Mediabench)
add_subdirectory(Polybench/all)
#add_subdirectory(Polybench_modif/all)




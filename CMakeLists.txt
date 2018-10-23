cmake_minimum_required (VERSION 3.5)


set(CMAKE_C_COMPILER riscv64-unknown-elf-gcc)
set(CMAKE_CXX_COMPILER riscv64-unknown-elf-g++)


project (HybridDBT_testbench)

set(CMAKE_C_FLAGS "-O3 -static -march=rv64imf -DSMALL_DATASET -DDATA_TYPE_IS_INT")
set(CMAKE_CXX_FLAGS "-O3 -static -march=rv64imf -DSMALL_DATASET -DDATA_TYPE_IS_INT")


link_libraries("-lm")

set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ./bin)

add_subdirectory(Mediabench)
add_subdirectory(Polybench/all)





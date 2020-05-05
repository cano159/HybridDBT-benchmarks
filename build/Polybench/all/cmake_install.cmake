# Install script for directory: /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/all

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/2mm/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/3mm/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/adi/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/atax/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/bicg/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/cholesky/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/correlation/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/covariance/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/deriche/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/doitgen/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/durbin/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/fdtd-2d/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/floyd-warshall/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/gemm/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/gemver/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/gesummv/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/gramschmidt/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/heat-3d/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/jacobi-1d/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/jacobi-2d/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/lu/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/ludcmp/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/mvt/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/nussinov/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/seidel-2d/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/symm/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syrk/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/trisolv/cmake_install.cmake")
  include("/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/trmm/cmake_install.cmake")

endif()


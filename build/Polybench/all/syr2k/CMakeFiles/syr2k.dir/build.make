# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build

# Include any dependencies generated for this target.
include Polybench/all/syr2k/CMakeFiles/syr2k.dir/depend.make

# Include the progress variables for this target.
include Polybench/all/syr2k/CMakeFiles/syr2k.dir/progress.make

# Include the compile flags for this target's objects.
include Polybench/all/syr2k/CMakeFiles/syr2k.dir/flags.make

Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.o: Polybench/all/syr2k/CMakeFiles/syr2k.dir/flags.make
Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.o: ../Polybench/all/syr2k/syr2k.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.o"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/syr2k.dir/syr2k.c.o   -c /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/all/syr2k/syr2k.c

Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/syr2k.dir/syr2k.c.i"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/all/syr2k/syr2k.c > CMakeFiles/syr2k.dir/syr2k.c.i

Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/syr2k.dir/syr2k.c.s"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/all/syr2k/syr2k.c -o CMakeFiles/syr2k.dir/syr2k.c.s

Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o: Polybench/all/syr2k/CMakeFiles/syr2k.dir/flags.make
Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o: ../Polybench/utilities/polybench.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o   -c /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/utilities/polybench.c

Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.i"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/utilities/polybench.c > CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.i

Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.s"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/utilities/polybench.c -o CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.s

# Object files for target syr2k
syr2k_OBJECTS = \
"CMakeFiles/syr2k.dir/syr2k.c.o" \
"CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o"

# External object files for target syr2k
syr2k_EXTERNAL_OBJECTS =

Polybench/all/syr2k/bin/syr2k: Polybench/all/syr2k/CMakeFiles/syr2k.dir/syr2k.c.o
Polybench/all/syr2k/bin/syr2k: Polybench/all/syr2k/CMakeFiles/syr2k.dir/__/__/utilities/polybench.c.o
Polybench/all/syr2k/bin/syr2k: Polybench/all/syr2k/CMakeFiles/syr2k.dir/build.make
Polybench/all/syr2k/bin/syr2k: Polybench/all/syr2k/CMakeFiles/syr2k.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable bin/syr2k"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/syr2k.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Polybench/all/syr2k/CMakeFiles/syr2k.dir/build: Polybench/all/syr2k/bin/syr2k

.PHONY : Polybench/all/syr2k/CMakeFiles/syr2k.dir/build

Polybench/all/syr2k/CMakeFiles/syr2k.dir/clean:
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k && $(CMAKE_COMMAND) -P CMakeFiles/syr2k.dir/cmake_clean.cmake
.PHONY : Polybench/all/syr2k/CMakeFiles/syr2k.dir/clean

Polybench/all/syr2k/CMakeFiles/syr2k.dir/depend:
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Polybench/all/syr2k /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Polybench/all/syr2k/CMakeFiles/syr2k.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Polybench/all/syr2k/CMakeFiles/syr2k.dir/depend


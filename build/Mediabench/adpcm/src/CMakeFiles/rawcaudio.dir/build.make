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
include Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/depend.make

# Include the progress variables for this target.
include Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/progress.make

# Include the compile flags for this target's objects.
include Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/flags.make

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.o: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/flags.make
Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.o: ../Mediabench/adpcm/src/rawcaudio.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.o"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/rawcaudio.dir/rawcaudio.c.o   -c /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/rawcaudio.c

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/rawcaudio.dir/rawcaudio.c.i"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/rawcaudio.c > CMakeFiles/rawcaudio.dir/rawcaudio.c.i

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/rawcaudio.dir/rawcaudio.c.s"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/rawcaudio.c -o CMakeFiles/rawcaudio.dir/rawcaudio.c.s

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.o: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/flags.make
Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.o: ../Mediabench/adpcm/src/adpcm.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.o"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/rawcaudio.dir/adpcm.c.o   -c /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/adpcm.c

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/rawcaudio.dir/adpcm.c.i"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/adpcm.c > CMakeFiles/rawcaudio.dir/adpcm.c.i

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/rawcaudio.dir/adpcm.c.s"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && /opt/riscv/rv64g-linux/bin/riscv64-unknown-linux-gnu-gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src/adpcm.c -o CMakeFiles/rawcaudio.dir/adpcm.c.s

# Object files for target rawcaudio
rawcaudio_OBJECTS = \
"CMakeFiles/rawcaudio.dir/rawcaudio.c.o" \
"CMakeFiles/rawcaudio.dir/adpcm.c.o"

# External object files for target rawcaudio
rawcaudio_EXTERNAL_OBJECTS =

Mediabench/adpcm/src/bin/rawcaudio: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/rawcaudio.c.o
Mediabench/adpcm/src/bin/rawcaudio: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/adpcm.c.o
Mediabench/adpcm/src/bin/rawcaudio: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/build.make
Mediabench/adpcm/src/bin/rawcaudio: Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable bin/rawcaudio"
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rawcaudio.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/build: Mediabench/adpcm/src/bin/rawcaudio

.PHONY : Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/build

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/clean:
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src && $(CMAKE_COMMAND) -P CMakeFiles/rawcaudio.dir/cmake_clean.cmake
.PHONY : Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/clean

Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/depend:
	cd /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/Mediabench/adpcm/src /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src /home/srokicki/Documents/Recherche/Benchmarks/HybridDBT-benchmarks/build/Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Mediabench/adpcm/src/CMakeFiles/rawcaudio.dir/depend


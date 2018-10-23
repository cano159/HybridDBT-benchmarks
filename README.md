Hybrid-DBT
=====================

This repository contains all the benchmark application used by <a href="https://github.com/srokicki/HybridDBT">Hybrid-DBT</a>, and scripts used for running the different experiments.


## Table of Contents
+ [Building the dependencies](#build)
+ [Using the script](#script)


## <a name="build"></a> Building the dependencies

### RISC-V GNU Toolchain

In order to compile an application and generated RISC-V binaries compatible with the DBT framework, we have to build the standard toolchain (from <a href="https://github.com/riscv/riscv-gnu-toolchain"> here</a>). To build it with the correct configuration, execute the following commands:

	$ $ git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
	$ export RISCV=/path/to/install/riscv/toolchain
	
Then configure the toolchain to be compatible with the DBT framework: it needs to generate code for a RISC-V 64-bits core with the M extension. Floating point operation are done in software. You can change the prefix to choose where to install the toolchain.

	$ ./configure --prefix=/opt/riscv --with-arch=rv64im --with-abi=lp64
	$ make

	
Once the compiler is generated, you can add the folder /opt/riscv/bin to the path so that the compiler is easily used. To generate RISC-V binaries, just run the following command:

	$ riscv64-unknown-elf-gcc -std=c99 -O3 helloworld.c -o helloworld

The CMake is configured to use "riscv64-unknown-elf-gcc" to compile all the benchmark applications.

### Hybrid-DBT Toolchain

Hybrid-DBT is necessary to run the benchmark script. To download ad compile it, run the following commands:

	$ git clone https://github.com/srokicki/HybridDBT.git
	
Then create a build folder and use CMAKE to generate makefiles:
	
	$ cd HybridDBT
	$ mkdir build
	$ cd build
	$ cmake ../
	
Compile the two tools used in the script:
	
	$ make dbt
	$ make simRISCV

Add the build/bin/ folder in your PATH, the benchmark script needs to see it.

### GEM5 Simulator

One experiment alsow use GEM5 simulator. To download the sources and build them using scons run the following commands:

	$ git clone https://gem5.googlesource.com/public/gem5
	$ scons build/RISCV/gem5.opt 

Add GEM5 to you PATH, the script needs to see it.

## <a name="script"></a> Using the script

The repository also contains a python script for running all experiments and writing the results in csv files. To run all the experiments on 2mm and 3mm applications from Polybench, run the following command:

	$ ./benchmarkLib.py 2mm 3mm

The list of accepted application can be obtained running:

	$ ./benchmarkLib.py -h

### TODO List

* Using Python to draw the different histograms
* Factorizing code in the Python script
* Adding a better management of threads created by the script. It currently creates all the thread for one experiments and waits their completion to start the other ones. It should always start a limited number of thread and start the new experiments before the previous one is finisched.

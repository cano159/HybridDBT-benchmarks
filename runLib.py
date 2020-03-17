#! /usr/bin/python

import sys, subprocess, os, shutil, random, shlex, time, re, distutils.spawn

BOOM_SIM=""
BOOM_PK=""
ROCKET_SIM=""
ROCKET_PK=""
GEM5=""


runs = []
tempFiles = []
results = {}


######################################################################################################################################################
##		Functions to start new executions and parse results
##
######################################################################################################################################################
##
##	getTempFileName() 								Generates random string for temporaray files (always inside /tmp/)
##	getRunTime(process)								Outputs the runtime of a process (NOT WORKING)
##	startRun(command, inFile, name)		Starts a subprocess called $name, running $command, using $file as standard input.
##  wait()														Check all running process, waiting for one to finish. It returns the finishing one.
##	parseResults(nameOut, name)				Parse the output of a file $nameOut and attribute it to the run $name
##	printResult(resultFile, resultList)
##
######################################################################################################################################################

def checkConfig():
	if not distutils.spawn.find_executable("dbt"):
		print "Error: Can't find Hybrid-DBT main executable. Please add it to your PATH."
		exit()

	if not distutils.spawn.find_executable("simRISCV"):
		print "Error: Can't find simRISCV main executable (from Hybrid-DBT git). Please add it to your PATH."
		exit()

	if GEM5 == "" and not distutils.spawn.find_executable("gem5"):
		print "WARNING: Can't find gem5 executable. Please add it to your PATH, document its location in the script or remove the experiment based on GEM5."
	
########

def getTempFileName():
	random.seed()
	tempFileName = "/temp_dd/igrida-fs1/srokicki/tmp/tempFile" + hex(random.randint(0, 4000000000000000000000000))[2:]
	
	if os.path.exists(tempFileName):
		return getTempFileName()
	else:
		return tempFileName

########

def getRunTime(process):
	pid = process.pid
	tempFileName = getTempFileName()
	tempFile = file(tempFileName, "w")
	subprocess.check_call(["ps", str(pid)], stdout = tempFile, shell=False)
	tempFile.close()
	tempFile = file(tempFileName, "r")
	value = "00:00"
	for line in tempFile:
		if re.sub('\s{2,}', ' ', line).split()[3] != "TIME":
			value = re.sub('\s{2,}', ' ', line).split()[3]

	tempFile.close()
	os.remove(tempFileName)
	return int(value.split(':')[0])

	
#########

def startRun(command, inFile, name):
	nameErr = getTempFileName()
	nameOut = getTempFileName()
	nameOutOar = getTempFileName()
	nameScript = getTempFileName() + ".sh"

	script = file(nameScript, "w")
	err = file(nameErr, "w")
	outOar = file(nameOutOar, "w")
	out = file(nameOut, "w")
	script.write(command + "\n")
	subprocess.check_call(['chmod', 'u+x', nameScript])

	#process = subprocess.Popen(command, stdin = inFile, stdout = out, stderr = err, shell = True)
	process = subprocess.check_call("oarsub -l core=1,walltime=03:50:00 -O " + nameOut + " " + nameScript, stdin = inFile, stdout = outOar, stderr = err, shell = True)
	print "oarsub -l core=1,walltime=03:50:00 -O " + nameOut + " " + nameScript

	outFile = open(nameOutOar, "r")
	for oneLine in outFile:
		print oneLine		
		if len(oneLine.split('=')) == 2 and oneLine.split('=')[0] == "OAR_JOB_ID":	
			oarProcess = oneLine.split('=')[1][:-1]


	runs.append((name, command, nameOut, nameErr, out, err, oarProcess))

#########

def wait():
	while True:
		nameOut = getTempFileName()
		out = file(nameOut, "w")
		process = subprocess.check_call("oarstat -u srokicki", stdout = out, shell = True)
		
		outFile = open(nameOut, "r")
		processAlive = []
		processAlive.append("0");
		for oneLine in outFile:
			while "  " in oneLine:
				oneLine = oneLine.replace("  ", " ")

			if len(oneLine.split(' '))>2 and oneLine.split(' ')[2] == "srokicki":
				processAlive.append(oneLine.split(' ')[0]);


		print processAlive
		
		for (name, command, nameOut, nameErr, out, err, process) in runs:
			print process
			#getRunTime(process)
			if process not in processAlive:
				out.close()
				err.close()
				runs.remove((name, command, nameOut, nameErr, out, err, process))
				return (name, command, nameOut, nameErr, process)


		time.sleep(20)

#########

def parseResults(nameOut, name):
	out = open(nameOut, "r")
	results = {"name": name}
	for oneLine in out:
		if oneLine[0] == '\t' and len(oneLine.split(':')) > 1:
			key = oneLine.split(':')[0].split('\t')[-1]
			results[key] = oneLine.split(':')[1].replace('\n', '')
		elif oneLine[:16] == "Completed after ":
			key = "cycle"
			results[key] = oneLine[16:-8]
		elif oneLine[:20] == "system.cpu.numCycles":
			key = "cycle"
			results[key] = oneLine.split()[1]
	return results

#########

def printResult(resultFile, resultList):
	resultFile = open(resultFile, "w+")
	if len(resultList) > 0:
		for oneRes in resultList:
			if len(oneRes.keys()) > 1:

				for oneKey in oneRes.keys():
					resultFile.write("\n" + oneKey)
					for oneResult in resultList:
						if oneResult.has_key(oneKey):
							resultFile.write(";" + oneResult[oneKey])
						else:
							resultFile.write(";?")
				break;

######################################################################################################################################################
##		Functions to parse benchmark sets
##
######################################################################################################################################################
##
##	scanMediabench(benchmarks)				Goes through benchmarks from Mediabench, finds folder name exec and extracts args. Returns the list of runs to execute
##	scanPolybench(benchmarks)					Goes through benchmarks from Polybench and returns list of runs to executes.
##
######################################################################################################################################################

def scanMediabench(benchmarks):
	localResult = []
	for oneBenchmark in benchmarks:
		for oneType in ["decode", "encode"]:
			decodeFile = open("./Mediabench/" + oneBenchmark + "/exec/s" + oneType + ".sh", "r")

			place = "./Mediabench/"+oneBenchmark+"/exec/"
			benchmark = ""
			args = ""
			inputs = ""
			outputs = ""

			for oneLine in decodeFile:
				splitted = oneLine[:-1].split("=")
				if len(splitted) > 1 and splitted[0] == "BENCHMARK":
					benchmark="../../../build/Mediabench/" + splitted[1]
				if len(splitted) > 1 and splitted[0] == "ARGS":
					args=splitted[1]
				if len(splitted) > 1 and splitted[0] == "INPUT":
					inputs=splitted[1]
				if len(splitted) > 1 and splitted[0] == "OUTPUT":
					outputs=splitted[1]

			if (benchmark != ""):
				localResult.append((oneBenchmark + "_" + oneType, place, benchmark, args, inputs, outputs))

	return localResult;

#########

def scanPolybench(benchmarks):
	localResult = []
	for oneBenchmark in benchmarks:

		localResult.append((oneBenchmark, "./", "/temp_dd/igrida-fs1/srokicki/HybridDBT-benchmarks/build/Polybench/all/" + oneBenchmark + "/bin/" + oneBenchmark, "", "", ""))

	return localResult;

def scanSpec():
	localResult = []
	localResult.append(("perlbench", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/600.perlbench_s/", "./perlbench_s_base.riscv-64", "-I./lib checkspam.pl 2500 5 25 11 150 1 1 1 1", "", ""))
	localResult.append(("mcf", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/605.mcf_s/", "./mcf_s_base.riscv-64", "inp.in", "", ""))
	#localResult.append(("omnetpp", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/620.omnetpp_s/", "./omnetpp_s_base.riscv-64", "-c General -r 0", "", ""))
	#localResult.append(("xalancbmk", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/623.xalancbmk_s/", "./xalancbmk_s_base.riscv-64", "-v t5.xml xalanc.xsl", "", ""))
	#localResult.append(("x264", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/625.x264_s/", "./x264_s_base.riscv-64", "--pass 1 --stats x264_stats.log --bitrate 1000 --frames 1000 -o BuckBunny_New.264 BuckBunny.yuv 1280x720", "", ""))
	#localResult.append(("deepsjeng", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/631.deepsjeng_s/", "./deepsjeng_s_base.riscv-64", "ref.txt", "", ""))
	#localResult.append(("leela", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/641.leela_s/", "./leela_s_base.riscv-64", "ref.sgf", "", ""))
	#localResult.append(("exchange2", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/648.exchange2_s/", "./exchange2_s_base.riscv-64", "6", "", ""))
	#localResult.append(("xz", "/temp_dd/igrida-fs1/srokicki/Speckle/build/overlay/intspeed/657.xz_s/", "./xz_s_base.riscv-64", "cpu2006docs.tar.xz 6643 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1036078272 1111795472 4", "", ""))

	return localResult

######################################################################################################################################################
##		Functions to start specific runs
##
######################################################################################################################################################
##
##	startsAllRunsGem5Big(runsToDo)		Executes benchmarks applications with GEM5, using the model for OoO core
##	startsAllRunsBoom(runsToDo)				Executes benchmarks applications using BOOM Verilator
##	startsAllRunsRocket(runsToDo)			Executes all applications on the Rocket Verilator
##	startsAllRunsDBT(runsToDo, optLevels, configs, extra) 	Executes all applications using Hybrid-DBT, with optLevels[], VLIW configs[] and extra flags (string)
##	startsAllRunsSimRISCV(runsToDo)		Executes all applications on the RISC-V pipelined simulator
##
######################################################################################################################################################

def startsAllRunsDBT(runsToDo, optLevels, configs, extra):
	for oneConfig in configs:
		for oneOpt in optLevels:
			for (name, place, benchmark, args, inputs, outputs) in runsToDo:
				runString = "dbt -f " + benchmark + " -O " + str(oneOpt) + " -c " + str(oneConfig) + " " + extra + " " 
				if inputs != "":
					runString = runString + " -i " + inputs
				if outputs != "":
					runString = runString + " -o " + outputs
				if args != "":
					runString = runString +" -- " + args
	
				originalPlace = os.getcwd()
				os.chdir(place)
				startRun(runString, None, name + "_O" + str(oneOpt) + "_c" + str(oneConfig))
				os.chdir(originalPlace)


def startsAllRunsQemu(runsToDo):
	for (name, place, benchmark, args, inputs, outputs) in runsToDo:
		runString = "LD_LIBRARY_PATH=/temp_dd/igrida-fs1/srokicki/install/HybridDBT/build/ /temp_dd/igrida-fs1/srokicki/install/riscv-gnu-toolchain/toolchain/bin/qemu-riscv64 " + benchmark + " " 
		if args != "":
			runString = runString + " " + args

		originalPlace = os.getcwd()
		os.chdir(place)
		startRun(runString, None, name)
		os.chdir(originalPlace)


######################################################################################################################################################
##		Functions to describe specific experiments
##
######################################################################################################################################################
##
##	runDBTPerf(runsToDo)			Runs maximal performance DBT on default config (config 2 which is 4 issues)
##
######################################################################################################################################################

def runQemu(runsToDo):

	resultFile = "results_qemu.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsQemu(runsToDo)

	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited ..."
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)


#########


#["adpcm", "jpeg", "epic", "g721", "gsm", "mpeg2"]
#["2mm","3mm", "adi", "atax", "bicg", "cholesky", "correlation", "covariance", "deriche", "doitgen", "durbin", "fdtd-2d", "floyd-warshall", "gemm", "gemver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp", "mvt", "nussinov", "seidel-2d", "symm", "syr2k", "syrk", "trisolv", "trmm"]
#runsToDo = scanMediabench(["adpcm", "jpeg", "epic", "g721", "gsm", "mpeg2"])
#runsToDo = scanPolybench(["2mm","3mm"])#, "atax", "bicg", "correlation", "covariance", "deriche", "doitgen", "durbin", "floyd-warshall", "gemm", "gemver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp", "nussinov", "seidel-2d", "syr2k", "syrk", "trisolv", "trmm"]) + scanMediabench(["adpcm", "jpeg", "epic", "g721", "gsm"])

runsToDo = []
#polybenchApps = ["2mm","3mm", "atax", "bicg", "correlation", "covariance", "deriche", "doitgen", "durbin", "floyd-warshall", "gemm", "gemver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp", "nussinov", "seidel-2d", "syr2k", "syrk", "trisolv", "trmm"]
#mediabenchApps = ["adpcm", "jpeg", "epic", "g721", "gsm"]
polybenchApps = ["2mm","3mm", "atax", "bicg"]
mediabenchApps = []
#runsToDo = scanMediabench(["adpcm", "jpeg", "epic", "g721", "gsm"])

if len(sys.argv) > 1:
	if sys.argv[1] in ["help", "-h", "--help"]:
		print "Usage: ./benchmarkLib.py [help/-h/--help] [apps]"
		print "Where apps is a list of application names from Polybench or Mediabench"
		print "Accepted Polybench apps are:"
		for oneApp in polybenchApps:
			print oneApp + " ",
		print "\nAccepted Mediabenchd apps are:"
		for oneApp in mediabenchApps:
			print oneApp + " ",
		exit()
	else:
		for oneApp in sys.argv[1:]:
			if oneApp in polybenchApps:
				runsToDo = runsToDo + scanPolybench([oneApp])
			elif oneApp in mediabenchApps:
				runsToDo = runsToDo + scanMediabench([oneApp])
			else:
				print "Unknown application '" + oneApp + "'. Ignoring it."
else:
	runsToDo = scanSpec()

checkConfig()


runQemu(runsToDo)
#runDBTnoSpec(runsToDo)
#runLittle(runsToDo)
#runDBTc0(runsToDo)
#runDBTc9(runsToDo)
#runDBTc13(runsToDo)
#runDBTsw(runsToDo)
#runDBTO0(runsToDo)
#runDBTO1(runsToDo)
#runDBTnospec9(runsToDo)
#runDBTreconf1(runsToDo)
#runDBTreconf2(runsToDo)
#runBIG(runsToDo)

# List of all experiments that have to be run 
#
# For all bnchmarks: 
#		- running at different optimization levels with only configuration 2.
#   - running with main configurations only at optimization level 2
#  	- running with configuration 0 and optimization level 3 (reconf)
#		- running with simRISCV
#		- running with boom
#		- running with rocket
#		- running with software DBT
# 	- running with tatic DBT on simRISCV
#		- running with reconfiguration models



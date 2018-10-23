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
	tempFileName = "/tmp/tempFile" + hex(random.randint(0, 4000000000000000000000000))[2:]
	
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

	err = file(nameErr, "w")
	out = file(nameOut, "w")

	process = subprocess.Popen(command, stdin = inFile, stdout = out, stderr = err, shell = True)

	runs.append((name, command, nameOut, nameErr, out, err, process))

#########

def wait():
	while True:	
		for (name, command, nameOut, nameErr, out, err, process) in runs:
			#getRunTime(process)
			if process.poll() != None:
				out.close()
				err.close()
				runs.remove((name, command, nameOut, nameErr, out, err, process))
				return (name, command, nameOut, nameErr, process.returncode)
		time.sleep(1)

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

		localResult.append((oneBenchmark, "./", "./build/Polybench/all/" + oneBenchmark + "/bin/" + oneBenchmark, "", "", ""))

	return localResult;

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

def startsAllRunsGem5Big(runsToDo):

	for (name, place, benchmark, args, inputs, outputs) in runsToDo:

		#location of gem5 script
		proc = os.path.dirname(os.path.realpath(__file__)) + "/scripts/big.py"

		nameStat = getTempFileName()
		runString = "gem5.opt " + " --stats-file=" + nameStat + " " + proc + " --caches --l2cache --l1d_size=8192 --l1i_size=8192 --l2_size=1048576 --l1d_assoc=4 --l1i_assoc=4 --l2_assoc=8 --cpu-clock=700MHz -c " + benchmark

		if args != "":
			runString += " --options=\"" + args + "\" " 

		if inputs != "":
			runString += " -i" + inputs + " " 

		runString += " > /dev/null ; grep numCycles " + nameStat + "; rm " + nameStat
		
		originalPlace = os.getcwd()
		os.chdir(place)
		if inputs != "":
			inputFile = open(inputs, "r")
			startRun(runString, inputFile, name)
		else:
			startRun(runString, None, name + "_gem5_" + "big")
		os.chdir(originalPlace)

#########

def startsAllRunsBoom(runsToDo):
	for (name, place, benchmark, args, inputs, outputs) in runsToDo:
		runString = BOOM_SIM + " -c " + BOOM_PK + " " + benchmark + " " + args
		if outputs != "":
			runString = runString + " > " + outputs

		originalPlace = os.getcwd()
		os.chdir(place)
		if inputs != "":
			inputFile = open(inputs, "r")
			startRun(runString, inputFile, name)
		else:
			startRun(runString, None, name)
		os.chdir(originalPlace)

#########

def startsAllRunsRocket(runsToDo):
	for (name, place, benchmark, args, inputs, outputs) in runsToDo:
		runString = ROCKET_SIM + " -c " + ROCKET_PK + " " + benchmark + " " + args
		if outputs != "":
			runString = runString + " > " + outputs

		originalPlace = os.getcwd()
		os.chdir(place)
		if inputs != "":
			inputFile = open(inputs, "r")
			startRun(runString, inputFile, name)
		else:
			startRun(runString, None, name)
		os.chdir(originalPlace)

#########

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

#########

def startsAllRunsSimRISCV(runsToDo):
	for (name, place, benchmark, args, inputs, outputs) in runsToDo:
		runString = "simRISCV -f " + benchmark 
		if inputs != "":
			runString = runString + " -i " + inputs
		if outputs != "":
			runString = runString + " -o " + outputs
		if args != "":
			runString = runString + " -a \" " + args + "\""

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

def runDBTPerf(runsToDo):

	resultFile = "results_dbt_O4_c2.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [4], [2], "")

	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTnoSpec(runsToDo):

	resultFile = "results_dbt_O2_c2.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [2], [2], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runLittle(runsToDo):

	resultFile = "results_LITTLE.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsSimRISCV(runsToDo)
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTc0(runsToDo):

	resultFile = "results_dbt_O4_c0.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [4], [0], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTc9(runsToDo):

	resultFile = "results_dbt_O4_c9.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [4], [9], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTc13(runsToDo):

	resultFile = "results_dbt_O4_c13.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [4], [13], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTsw(runsToDo):

	resultFile = "results_dbt_sw.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [5], [0], " -type 1 ")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTO0(runsToDo):

	resultFile = "results_dbt_O0.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [0], [2], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTO1(runsToDo):

	resultFile = "results_dbt_O1.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [1], [2], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTnospec9(runsToDo):

	resultFile = "results_dbt_nospec_9.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [2], [9], "")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTreconf1(runsToDo):

	resultFile = "results_dbt_reconf1.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [5], [0], " -coef 0")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runDBTreconf2(runsToDo):

	resultFile = "results_dbt_reconf2.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsDBT(runsToDo, [5], [0], " -coef 100")
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
		resultList.append(parseResults(nameOut, name))

		os.remove(nameOut)
		os.remove(nameErr)

	printResult(resultFile, resultList)

#########

def runBIG(runsToDo):

	resultFile = "results_big.csv"

	#We check if the result file already exists
	if os.path.exists(resultFile):
		return

	startsAllRunsGem5Big(runsToDo)
	results[resultFile] = []
	resultList = results	[resultFile]

	while	(len(runs) > 0):
		(name, command, nameOut, nameErr, returnCode) = wait()

		print "command " + command +" exited with code "+ str(returnCode)
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
polybenchApps = ["2mm","3mm", "atax", "bicg", "correlation", "covariance", "deriche", "doitgen", "durbin", "floyd-warshall", "gemm", "gemver", "gesummv", "gramschmidt", "heat-3d", "jacobi-1d", "jacobi-2d", "lu", "ludcmp", "nussinov", "seidel-2d", "syr2k", "syrk", "trisolv", "trmm"]
mediabenchApps = ["adpcm", "jpeg", "epic", "g721", "gsm"]

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
	runsToDo = scanPolybench(polybenchApps) + scanMediabench(mediabenchApps)

checkConfig()


runDBTPerf(runsToDo)
runDBTnoSpec(runsToDo)
runLittle(runsToDo)
runDBTc0(runsToDo)
runDBTc9(runsToDo)
runDBTc13(runsToDo)
runDBTsw(runsToDo)
runDBTO0(runsToDo)
runDBTO1(runsToDo)
runDBTnospec9(runsToDo)
runDBTreconf1(runsToDo)
runDBTreconf2(runsToDo)
runBIG(runsToDo)

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



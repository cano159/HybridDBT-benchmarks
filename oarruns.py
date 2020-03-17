import sys, subprocess, os, shutil, random, shlex, time, re, distutils.spawn, json

for oneRun in range (10):
	runId = subprocess.check_output(["oarsub", '"sleep ' + str(10+oneRun) + '"']).split("OAR_JOB_ID=")[1].split("\n")[0]

	print runId

aliveRuns = json.loads(subprocess.check_output(["oarstat", "-u", "srokicki", "-J"]))
for oneRun in aliveRuns:
	print oneRun



#!/usr/bin/env python
import os, sys
import subprocess

opts = {}
<<<<<<< HEAD
opts["out"] = '/home/users/bdillon/P-ONE/sim0002/eventfiles'
opts["job"] = '/home/users/bdillon/P-ONE/sim0002/src_sim'
opts["gcd"] = '/home/users/bdillon/P-ONE/sim0002/gcdfile'
=======
opts["out"] = '/mnt/home/dillonb5/P-ONE/sim0002/eventfiles'
opts["job"] = '/mnt/home/dillonb5/P-ONE/sim0002/src_sim'
opts["gcd"] = '/mnt/home/dillonb5/P-ONE/sim0002/gcdfile'
>>>>>>> 7fc7936 (initial commit)

processfilename = 'run_muon'
submissionfilename = 'run_muon.submit'

job_string = '''#!/bin/bash 

<<<<<<< HEAD
bash /home/users/bdillon/pone_offline/env-shell_Container.sh python {}/GenerateEvents.py -o {} -r $1 -g {} -n 100

'''.format(opts["job"],
           opts["out"]+"/SingleMuon",
           opts["gcd"]+"/PONE_10String_7Cluster_*.i3.gz")
=======
bash /mnt/home/dillonb5/pone_offline/env-shell_Container.sh python {}/GenerateEvents.py -o {} -r $1 -g {} -n 10

'''.format(opts["job"],
           opts["out"]+"/SingleMuon",
           opts["gcd"]+"/PONE_10String_7Cluster_standard.i3.gz")
>>>>>>> 7fc7936 (initial commit)

with open(opts["job"] + "/" + processfilename + '.sh', 'w') as ofile:
	ofile.write(job_string)
	subprocess.Popen(['chmod','777',opts["job"] + "/" +  processfilename + '.sh'])

submit_string = '''
executable = {}/{}

Arguments = $(Item)
output = {}_$(Item).out
error = {}_$(Item).err
log = {}_$(Item).log

<<<<<<< HEAD
+SingularityImage = "/data/p-one/icetray_offline_june24_2022.sif"
=======

>>>>>>> 7fc7936 (initial commit)

Universe = vanilla
request_memory = 4GB
request_cpus = 1
requirements = HasSingularity
requirements = CUDADeviceName == "NVIDIA TITAN Xp"

notification = never

+TransferOutput=""

queue from seq {} {} |
'''.format(opts["job"],
           processfilename + '.sh',
           opts["job"]+"/out/"+processfilename,
           opts["job"]+"/error/"+processfilename,
           opts["job"]+"/log/"+processfilename,
<<<<<<< HEAD
           1, 1000)
=======
           1, 10)
>>>>>>> 7fc7936 (initial commit)

with open(opts["job"] + "/" +  submissionfilename, 'w') as ofile:
	ofile.write(submit_string)

<<<<<<< HEAD
submit = subprocess.Popen(['condor_submit', opts["job"] + "/" + submissionfilename])
=======
submit = subprocess.Popen(['sbatch', opts["job"] + "/" + submissionfilename])
>>>>>>> 7fc7936 (initial commit)

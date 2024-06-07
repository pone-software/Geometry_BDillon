#!/usr/bin/env python
import os, sys
import subprocess

opts = {}
opts["out"] = '/home/users/bdillon/P-ONE/sim0002/reco_spline'
opts["data"] = '/home/users/bdillon/P-ONE/sim0002/linefit'
opts["job"] = '/home/users/bdillon/P-ONE/sim0002/src_spline'
opts["gcd"] = '/home/users/bdillon/P-ONE/sim0002/gcdfile'

processfilename = 'run_spline'
submissionfilename = 'run_spline.submit'

job_string = '''#!/bin/bash 

eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`

bash /data/p-one/twagiray/trackreco/mmsreco_convs/env-shell.sh python {}/mmsreco_spline_convs.py -i {} -o {} -r $1 -g {}

'''.format(opts["job"],
           opts["data"]+"/SingleMuon_",
           opts["out"]+"/SingleMuon_",
           opts["gcd"]+"/PONE_10String_7Cluster_*.i3.gz")

with open(opts["job"] + "/" + processfilename + '.sh', 'w') as ofile:
	ofile.write(job_string)
	subprocess.Popen(['chmod','777',opts["job"] + "/" +  processfilename + '.sh'])

submit_string = '''
executable = {}/{}

Arguments = $(Item)
output = {}_$(Item).out
error = {}_$(Item).err
log = {}_$(Item).log


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
           1, 1000)

with open(opts["job"] + "/" +  submissionfilename, 'w') as ofile:
	ofile.write(submit_string)

submit = subprocess.Popen(['condor_submit', opts["job"] + "/" + submissionfilename])

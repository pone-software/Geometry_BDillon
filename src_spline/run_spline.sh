#!/bin/bash 

eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`

bash /data/p-one/twagiray/trackreco/mmsreco_convs/env-shell.sh python /home/users/bdillon/P-ONE/sim0002/src_spline/mmsreco_spline_convs.py -i /home/users/bdillon/P-ONE/sim0002/linefit/SingleMuon_ -o /home/users/bdillon/P-ONE/sim0002/reco_spline/SingleMuon_ -r $1 -g /home/users/bdillon/P-ONE/sim0002/gcdfile/PONE_10String_7Cluster_*.i3.gz


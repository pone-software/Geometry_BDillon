#!/bin/bash

eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`

bash /data/p-one/twagiray/trackreco/common_variables/env-shell.sh python /home/users/bdillon/P-ONE/sim0002/src_spline/make_ldir_selection.py -i /home/users/bdillon/P-ONE/sim0002/reco_spline/SingleMuon_ -o /home/users/bdillon/P-ONE/sim0002/reco_spline/selection/SingleMuon_ -r $1 -g /home/users/bdillon/P-ONE/sim0002/gcdfile/PONE_10String_7Cluster_*.i3.gz


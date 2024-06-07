#!/bin/bash

bash /home/users/bdillon/pone_offline/env-shell_Container.sh python /home/users/bdillon/P-ONE/sim0002/src_sim/DAQSim.py -i /home/users/bdillon/P-ONE/sim0002/photonfiles/SingleMuon_ -o /home/users/bdillon/P-ONE/sim0002/daqfiles/SingleMuon_ -r $1 -g /home/users/bdillon/P-ONE/sim0002/gcdfile/PONE_10String_7Cluster_*.i3.gz -e .gz -n 2


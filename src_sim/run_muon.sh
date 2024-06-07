#!/bin/bash 

bash /home/users/bdillon/pone_offline/env-shell_Container.sh python /home/users/bdillon/P-ONE/sim0002/src_sim/GenerateEvents.py -o /home/users/bdillon/P-ONE/sim0002/eventfiles/SingleMuon -r $1 -g /home/users/bdillon/P-ONE/sim0002/gcdfile/PONE_10String_7Cluster_*.i3.gz -n 100


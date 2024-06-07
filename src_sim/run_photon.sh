#!/bin/bash 

bash /home/users/bdillon/pone_offline/env-shell_Container.sh python /home/users/bdillon/P-ONE/sim0002/src_sim/PropogatePhotons.py -i /home/users/bdillon/P-ONE/sim0002/eventfiles/SingleMuon_ -o /home/users/bdillon/P-ONE/sim0002/photonfiles/SingleMuon_ -r $1 -m I3MCTree -g /home/users/bdillon/P-ONE/sim0002/gcdfile/PONE_10String_7Cluster_*.i3.gz


#!/bin/bash

. /mnt/home/dillonb5/pone_offline/env.sh
python3 ./TrackReconstruction.py -g /mnt/home/dillonb5/P-ONE/sim00Ty/gcdfile/* -r $SLURM_ARRAY_TASK_ID -i /mnt/home/dillonb5/P-ONE/sim00Ty/daqfiles/SingleMuon_ -o /mnt/home/dillonb5/P-ONE/sim00Ty/linefit/SingleMuon_ -r 1

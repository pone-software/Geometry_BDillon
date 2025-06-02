#!/bin/bash

. /mnt/home/dillonb5/pone_offline/env.sh 
python3 /mnt/home/dillonb5/P-ONE/sim00Ty/src_sim/PropogatePhotons.py -i /mnt/home/dillonb5/P-ONE/sim00Ty/eventfiles/singlemuon_ -g /mnt/home/dillonb5/P-ONE/sim00Ty/gcdfile/* -o /mnt/home/dillonb5/P-ONE/sim00Ty/photonfiles/test-$SLURM_ARRAY_TASK_ID -r $SLURM_ARRAY_TASK_ID 

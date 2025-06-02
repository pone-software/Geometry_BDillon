#!/bin/bash

. /mnt/home/dillonb5/pone_offline/env.sh
python3 ./make_ldir_selection.py -i /mnt/home/dillonb5/P-ONE/sim00Ty/reco_spline/singlemuon_  -r $SLURM_ARRAY_TASK_ID -o /mnt/home/dillonb5/P-ONE/sim00Ty/selection/ -g /mnt/home/dillonb5/P-ONE/sim00Ty/gcdfile

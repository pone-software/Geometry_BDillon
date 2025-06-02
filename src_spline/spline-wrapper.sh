#!/bin/bash

. /mnt/home/dillonb5/pone_offline/env.sh
python3 mmsreco_spline_convs.py -i /mnt/home/dillonb5/P-ONE/sim00Ty/linefit/SingleMuon_  -r $SLURM_ARRAY_TASK_ID -o /mnt/home/dillonb5/P-ONE/sim00Ty/reco_spline/SingleMuon -g /mnt/home/dillonb5/P-ONE/sim00Ty/gcdfile/*

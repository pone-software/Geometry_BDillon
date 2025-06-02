. /mnt/home/dillonb5/pone_offline/env.sh
python3 ./DAQSim.py -g /mnt/home/dillonb5/P-ONE/sim00Ty/gcdfile/* -i /mnt/home/dillonb5/P-ONE/sim00Ty/photonfiles/SingleMuon_ -r $SLURM_ARRAY_TASK_ID -o /mnt/home/dillonb5/P-ONE/sim00Ty/daqfiles/SingleMuon_ -n 2 

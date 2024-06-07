#!/bin/bash

eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`

bash /home/users/twagiray/icetray/build/env-shell.sh python /home/users/bdillon/P-ONE/sim0002/src_spline/get_mmsreco_hdfdata.py -i /home/users/bdillon/P-ONE/sim0002/reco_spline/selection/SingleMuon_ --hdf5file /home/users/bdillon/P-ONE/sim0002/src_spline/70_string_muon_gun_reco_spline_test2.hdf5 -r $1


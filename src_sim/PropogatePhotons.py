#!/usr/bin/env python

"""

source: https://github.com/pone-software/pone_offline/tree/master/Examples

"""

import argparse
import os
from I3Tray import *
from icecube import icetray
from icecube import phys_services
from icecube import clsim
# import WaterOpticalModel.MakePoneMediumPropertiesConservative as Medium
import WaterOpticalModel.MakePoneMediumPropertiesSpeculativeExtendedRange as Medium
from Utilities.DOMUtility import DOMProperties

parser = argparse.ArgumentParser(description = "Takes I3Photons from step2 of the simulations and generates DOM hits")
parser.add_argument("-i", "--infile",default="./test_input.i3", 
                    help="Write output to OUTFILE (.i3{.gz} format)")
parser.add_argument("-o", "--outfile",default="./test_output.i3", 
                    help="Write output to OUTFILE (.i3{.gz} format)")
parser.add_argument("-r", "--runnumber", type=int, default=1, 
                    help="The run/dataset number for this simulation, is used as seed for random generator")
parser.add_argument("-l", "--filenr",type=int, default=1, 
                    help="File number, stream of I3SPRNGRandomService")
parser.add_argument("-g", "--gcdfile", default='PONE_10String_7Cluster_baseline.i3.gz', help="Read in GCD file")
parser.add_argument("-e", "--efficiency", type=float,default=1.0,
                    help="DOM Efficiency ... the same as UnshadowedFraction")
parser.add_argument("-m", "--mctree", default="I3MCTree", help="I3MCTree to go into clsim")
parser.add_argument("-c", "--crossenergy", type=float,default=200.0, 
                    help="The cross energy where the hybrid clsim approach will be used")
args = parser.parse_args()
count = 0
CPU=False

# load DOM properties
dom_properties = DOMProperties()

photon_series = "I3Photons"
#print 'CUDA devices: ', options.DEVICE
tray = I3Tray()

# Now fire up the random number generator with that seed
randomService = phys_services.I3SPRNGRandomService(
                seed = int(args.runnumber),
               nstreams = int(4e7),
                streamnum = int(args.runnumber))

tray.context['I3RandomService'] = randomService

outfile = args.outfile +str(args.runnumber)+".i3.gz"

infile = args.infile + str(args.runnumber)+".i3.gz"

#gcd_file = dataio.I3File(args.gcdfile)
print(args.gcdfile)

tray.AddModule('I3Reader', 'reader',
            FilenameList = [infile]
            )

#tray.AddModule('I3Reader', 'reader',
#            FilenameList = [args.gcdfile,infile]
#            )

tray.AddSegment(clsim.I3CLSimMakePhotons, 'goCLSIM',
                # UseCPUs=True,
                UseGPUs=True,
                MCTreeName=args.mctree,
                UseI3PropagatorService=False,
                PhotonSeriesName=photon_series,
                MCPESeriesName='',
                RandomService=randomService,
                IceModelLocation=Medium.MakePoneMediumProperties(),
                UnWeightedPhotons=False,
                # UnWeightedPhotonsScalingFactor = None,
                DOMRadius=(17.0*2.54*0.01/2.0)*icetray.I3Units.m,
                UseGeant4=False,
                CrossoverEnergyEM=None,
                PhotonHistoryEntries=0,
                StopDetectedPhotons=True,
                DoNotParallelize=False,
                WavelengthAcceptance=dom_properties.GetCLSimQETable(
                    factor=dom_properties.GetMaxAngularAcceptance()*1.05),
                DOMOversizeFactor=1.0,  # (17./13.),
                UnshadowedFraction=1.,  # normal in IC79 and older CLSim versions was 0.9, now it is 1.0
                GCDFile=args.gcdfile,  # gcd_file
                )

#icetray.logging.I3Logger.global_logger.set_level_for_unit('clsim', icetray.logging.I3LogLevel.LOG_ERROR)
#icetray.logging.I3Logger.global_logger.set_level_for_unit('I3CLSimStepToPhotonConverterOpenCL', icetray.logging.I3LogLevel.LOG_WARN)

#tray.AddModule(PrintMessage,"print",message = "CLSiM Check")

tray.AddModule("I3Writer","writer",
#               SkipKeys=SkipKeys,
               Filename =  outfile,
               Streams = [icetray.I3Frame.TrayInfo, icetray.I3Frame.DAQ],
              )

tray.AddModule("TrashCan","adios")

tray.Execute()
tray.Finish()

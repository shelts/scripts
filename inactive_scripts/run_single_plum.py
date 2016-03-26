#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#######################################################################
#This creates a histrogram and matches to another histogram.
#    LIBRARY   #
args = [3.08944663435935, 0.90864900742945, 0.339201272068107, 0.528328962440291, 110.650249409941, 0.529997456877515]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

#print "parameters: ", back_time, r0, light_r_ratio, mass, mass_ratio
y = True
n = False

#    SWITCHES  #
run_single_plum = n
remake_single   = n


#    Histogram names     #

#    histograms for runs #
seed = '379780525'
lua = "EMD_20k_1_54.lua"
#######################################################################

if(run_single_plum == True):
    histogram_single = "tidal_histogram_single_plummer.hist"
    print('running single plummer nbody')
    back_time = "1"
    r0 = "0.2"
    mass = "11"
    if(remake_single == True):
        os.chdir("./")
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/single_plum_EMD_20k_isotropic_1_54.lua \
        -z ~/Desktop/research/quick_plots/hists_outputs/" + histogram_single + " \
        -n 8 -x -e  961694  -i "+ sim_time + " " + back_time + " " + r0 + " " + mass)
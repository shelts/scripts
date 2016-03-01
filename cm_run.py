#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#This creates a histrogram and matches to another histogram.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

#args = [3.945, 0.9862, 0.2, 0.2, 12, 0.2] #for hist with dark matter
args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter


sim_time = ['0.0000000001', '4']
#sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = y
remake    = y

match_histograms = n
calc_cm = n

plot_stability = n
plot_lb = n


seed = ['124135', '765483']
hists = ['seed1_' + seed[0] + '_0g', 'seed2_' + seed[1] + '_0g', 'seed1_' + seed[0] + '_4g', 'seed2_' + seed[1] + '_4g']
hists_woc = ['seed1_' + seed[0] + '_0g_woc', 'seed2_' + seed[1] + '_0g_woc', 'seed1_' + seed[0] + '_4g_woc', 'seed2_' + seed[1] + '_4g_woc']

N = 4  
M = 2

#    Histogram names     #
histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist"
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16.hist"



#    histograms for runs #
histogram_for_nbody_run = hists
output1 = 'cm_test/outs/' + hists[2] + '.out'
output2 = 'cm_test/outs/' + hists_woc[2] + '.out'

match_hist_correct = histogram_mw_1d_new
match_hist_compare = histogram_for_nbody_run

lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"

#lua = "EMD_20k_v154_fixed_seed.lua"
#lua = "Null.lua"

outs = 2

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(M, N):
    if(run_nbody == True):
        print('running nbody')
        if(remake == True and i == 0):
            os.chdir("./")
            #os.system("rm -r nbody_test")
            #os.system("mkdir nbody_test")
            os.chdir("nbody_test")
            os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
            os.system("make -j ")
            os.chdir("../")
        #-h ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_correct + " \
        if(i % 2 == 0):#for the seed
            q = 0
        else:
            q = 1
        if(i < 2):#for the sim time
            j = 0
        else:
            j = 1
        print('q = ', q)
        os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody \
            -f ~/Desktop/research/lua/" + lua + " \
            -z ~/Desktop/research/quick_plots/hists_outputs/cm_test/hists/" + histogram_for_nbody_run[i] + ".hist \
            -o ~/Desktop/research/quick_plots/hists_outputs/cm_test/outs/" + histogram_for_nbody_run[i] + ".out \
            -n 8 -x -P -e " + seed[q] + " -i " + sim_time[j] + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )

    if(match_histograms == True):
        print "matching histograms: "
        #using call here instead so the format of using it is on record
        call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody  " 
            + "-h ~/Desktop/research/quick_plots/hists_outputs/cm_test/" + match_hist_correct
            + " -s ~/Desktop/research/quick_plots/hists_outputs/cm_test/hists/" + histogram_for_nbody_run[i] + ".hist"], shell=True)
    
if(calc_cm == True):
    if(outs == 2):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output)
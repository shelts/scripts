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
#args = [0.0001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter

sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = y
remake    = y

plot_plot_hists  = y
match_histograms = y
calc_cm = y

plot_stability = n
plot_lb = n


#    Histogram names     #
histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist"
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16.hist"

#0.000355062517318
test_seed1_124135 = "test_seed1_124135.hist"
test_seed2_765483 = "test_seed2_765483.hist"

#0.000320048580327
test_seed1_124135_wo_cm_correction = "test_seed1_124135_wo_cm_correction.hist"
test_seed2_765483_wo_cm_correction = "test_seed2_765483_wo_cm_correction.hist"


test_seed1_124135_4gy = "test_seed1_124135_4gy.hist"
test_seed2_765483_4gy = "test_seed2_765483_4gy.hist"

test_seed1_124135_4gy_wo_cm_correction = "test_seed1_124135_4gy_wo_cm_correction.hist"
test_seed2_765483_4gy_wo_cm_correction = "test_seed2_765483_4gy_wo_cm_correction.hist"

#    histograms for runs #
histogram_for_nbody_run = test_seed2_765483_4gy

match_hist_correct = test_seed1_124135_4gy
match_hist_compare = test_seed2_765483_4gy
#seed = '86043093'
#seed = '124135'
seed = '765483'
lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"
#lua = "EMD_20k_v154_fixed_seed.lua"
#lua = "Null.lua"

output1 = "regular.out"
output2 = "out.out"
output = "out.out"
outs = 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(run_nbody == True):
    print('running nbody')
    #-h ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_correct + " \
    if(remake == True):
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/" + lua + " \
        -z ~/Desktop/research/quick_plots/hists_outputs/" + histogram_for_nbody_run + " \
        -o ~/Desktop/research/quick_plots/hists_outputs/" + output + " \
        -n 8 -x -P -e " + seed + " -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_stability == True):
    os.chdir("./data_testing")
    os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_lb == True):
    os.chdir("./quick_plots")
    os.system("python lb_plot.py hists_outputs/out.out")
    os.chdir("../")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_plot_hists == True):
    os.system("./plot_matching_hist.py " + match_hist_correct + " " + match_hist_compare)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(match_histograms == True):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody  " 
          + "-h ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_correct
          + " -s ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_compare], shell=True)
print "\n"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
if(calc_cm == True):
    if(outs == 2):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output)
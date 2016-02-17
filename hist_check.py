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
args = [4, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
# -5.533137043,
#args = [3.66095915716141, 0.937350090872496, 0.861348122358322, 0.870432981872, 13.5649889884517, 0.45703884701361]
#-0.1085871427, laptop calced: 0.508502685556493
#args = [3.68159410255875, 0.860706978637003, 0.995861475185167, 0.68189520501899, 60.6192551418029, 0.487269480544337]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = n
remake    = n

plot_plot_hists  = n
match_histograms = n
calc_cm = n

plot_stability = y
plot_lb = n


#    Histogram names     #
histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist"
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16.hist"

histogram_mw_2d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_ml12_mr0p2_2D.hist" #histogram up on MW

best_fit_narrow = 'fixed_seed_new_hist_best_fit_narrow.hist'
best_fit_wide = 'fixed_seed_new_hist_best_fit_wide.hist'
test = 'regular_vel.hist'
test1 = 'shifted_vel.hist'
test3 = 'shifted_vel2.hist'


histogram_best_fit_2d = "best_fit_parameter_hist_2d.hist" #best fit para hist from MW

#    histograms for runs #
histogram_for_nbody_run = best_fit_wide

match_hist_correct = histogram_mw_1d_new
match_hist_compare = best_fit_wide
seed = '98756'
lua = "EMD_20k_1_54_fixed_seed.lua"
#lua = "Null.lua"
output = "regular.out"
output2 = "shifted.out"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(run_nbody == True):
    print('running nbody')
    if(remake == True):
        os.chdir("./")
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
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
    os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output + " " + output2)
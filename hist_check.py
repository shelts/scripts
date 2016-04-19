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

#args = [3.945, 0.98, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [0.000000000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter

#args = [4.2041079448536, 0.960966924019158, 0.484794405009598, 0.479905157536268, 16.1179897373077, 0.512380058807321]

#milkyway_nbody 1.58 Linux x86_64 double ps_nbody_3_21_16_orphansim_v158_1_1453826702_1418990 [1122644556]
#l= -135.500988330967346 rep = 135.500958116596394
args = [4.21055801725015, 1.09857470542192, 1.09701466690749, 0.228068244457245, 11.4035462443717, 0.0868122079118621]

#milkyway_nbody 1.58 Windows x86_64 double ps_nbody_3_21_16_orphansim_v158_3_1453826702_1419047 [1122645405]
#l=-11.259544051913556 rep = 9.020718669753517
#args = [3.5778652629815, 0.90785959744826, 0.535200041718781, 0.585243403911591, 51.6602049868088, 0.105707221332705]

sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = y
remake    = n
remake_only = n

plot_hists  = y
match_histograms = y
calc_cm = n

plot_stability = n
plot_lb = n


#    Histogram names     #

test = "test"
histogram_mw_1d_v158 = "tidal_histogram_EMD_20k_v158_ft3p945_rt0p98_r0p2_rr0p2_ml12_mr0p2__3_21_16"

def stuff():
    histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist"
    old_binary_test = "old_binary_test"
    new_binary_test = "new_binary_test"
    with_correction_on_new_binary = 'with_correction_on_new_binary'
    with_lua_correction_on_old_binary = 'with_lua_correction_on_old_binary'
    t_3p945gy_p9862 = '3p945gy_p9862'
    t_3p945gy_p9862_2 = '3p945gy_p9862_2'
    t_4gy_p9862 = '4gy_p9862'
    t_4gy_p9862_2 ='4gy_p9862_2'
    t_3p95gy_p9862 = '3p95gy_p9862'
    t_3p95gy_p9862_2 = '3p95gy_p9862_2'
    t_3p9gy_p9862 = '3p9gy_p9862'
    t_3p9gy_p9862_2 = '3p9gy_p9862_2'

#    histograms1 for runs #
histogram_for_nbody_run = test 

match_hist_correct = histogram_mw_1d_v158 
match_hist_compare = test

seed = '124135'
#lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"
lua = "EMD_20k_v158_fixed_seed.lua"
#lua = "Null.lua"
version = '_158'
versioning = '1'
output1 = "regular.out"
output2 = "out.out"
output = histogram_for_nbody_run
outs = 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(run_nbody == True):
    print('running nbody')
    if(remake == True):
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
        #-h ~/Desktop/research/quick_plots/hists/" + match_hist_correct + ".hist \
    if(remake_only == False):
        os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + version + " \
            -f ~/Desktop/research/lua/" + lua + " \
            -z ~/Desktop/research/quick_plots/hists/" + histogram_for_nbody_run + ".hist \
            -o ~/Desktop/research/quick_plots/outputs/" + output + ".out \
            -n 8 -x  -e " + seed + " -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
     #+ " \
        #> new_binary1.txt"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_stability == True):
    os.chdir("./data_testing")
    os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_lb == True):
    os.chdir("./quick_plots")
    os.system("python lb_plot.py outputs/out.out")
    os.chdir("../")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_hists == True):
    os.system("./plot_matching_hist.py " + match_hist_correct + " " + match_hist_compare)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(match_histograms == True):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + version  
          + " -h ~/Desktop/research/quick_plots/hists/" + match_hist_correct + '.hist'
          + " -s ~/Desktop/research/quick_plots/hists/" + match_hist_compare + '.hist'], shell=True)
    print match_hist_correct, "\n", match_hist_compare
print "\n"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
if(calc_cm == True):
    if(outs == 2):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output)
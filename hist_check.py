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
args = [0.000000000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter

#-1.403549100742481 , 
#Name ps_nbody_2_10_16_orphan1_1_v154_1453826702_744952_7
#Workunit  ps_nbody_2_10_16_orphan1_1_v154_1453826702_744952 [1096242405]
#args = args = [4.11503687418494, 0.870267120797343, 0.537036828384213, 0.325201157589727, 73.3972095967662, 0.418435603009849]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = y
remake    = y
remake_only = y

plot_hists  = n
match_histograms = y
calc_cm = n

plot_stability = n
plot_lb = n


#    Histogram names     #

test = "test"
mw_hist_1d = 'tidal_histogram_EMD_20k_v156_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_3_8_16' 
histogram_mw_1d_newer = "tidal_histogram_EMD_20k_v156_ft3p9_rt0p9862_r0p2_rr0p2_ml12_mr0p2_3_8_16"
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16"

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

match_hist_correct = mw_hist_1d 
match_hist_compare = mw_hist_1d

seed = '124135'
#lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"
lua = "EMD_20k_v154_fixed_seed.lua"
#lua = "Null.lua"
version = ''
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
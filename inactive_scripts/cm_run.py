#! /usr/bin/python
import os
import subprocess
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#This script was meant for comparing histograms of different seeds to check 
#if the center of mass correction in the lua actually works or not. 
#It also checks to see if it improves the likelihood.
#it also runs the center of mass calculation script.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

#args = [3.945, 0.9862, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
args = [4, 0.9862, 0.2, 0.2, 12, 0.2]

sim_time = ['0.00000000000001', '4', '3.945']
test = ['3p946gy_p9862', '3p946gy_p9862_2']
#sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = y
remake    = n

match_histograms = y
calc_cm = n

plot_plot_hists = n
plot_lb = n


seed = ['124135', '765483', '235234', '687867834', '10398463', '1614616']
hists = ['seed1_' + seed[0] + '_0g', 'seed2_' + seed[1] + '_0g', 'seed1_' + seed[0] + '_4g', 'seed2_' + seed[1] + '_4g']
hists_woc = ['seed1_' + seed[0] + '_0g_woc', 'seed2_' + seed[1] + '_0g_woc', 'seed1_' + seed[0] + '_4g_woc', 'seed2_' + seed[1] + '_4g_woc']

hists_2d = ['2d_seed1_' + seed[0] + '_0g', '2d_seed2_' + seed[1] + '_0g', '2d_seed1_' + seed[0] + '_4g', '2d_seed2_' + seed[1] + '_4g']
hists_2d_woc = ['2d_seed1_' + seed[0] + '_0g_woc', '2d_seed2_' + seed[1] + '_0g_woc', '2d_seed1_' + seed[0] + '_4g_woc', '2d_seed2_' + seed[1] + '_4g_woc']

hists_wide = ['wide_seed1_' + seed[0] + '_0g', 'wide_seed2_' + seed[1] + '_0g', 'wide_seed1_' + seed[0] + '_4g', 'wide_seed2_' + seed[1] + '_4g']
hists_woc_wide = ['wide_seed1_' + seed[0] + '_0g_woc', 'wide_seed2_' + seed[1] + '_0g_woc', 'wide_seed1_' + seed[0] + '_4g_woc', 'wide_seed2_' + seed[1] + '_4g_woc']

in_c_hists_wide = ['in_c_wide_seed1_' + seed[0] + '_0g', 'in_c_wide_seed2_' + seed[1] + '_0g', 'in_c_wide_seed1_' + seed[0] + '_4g', 'in_c_wide_seed2_' + seed[1] + '_4g']
in_c_hists_woc_wide = ['in_c_wide_seed1_' + seed[0] + '_0g_woc', 'in_c_wide_seed2_' + seed[1] + '_0g_woc', 'in_c_wide_seed1_' + seed[0] + '_4g_woc', 'in_c_wide_seed2_' + seed[1] + '_4g_woc']

in_c_wide_woc_multipleSeeds_4gy = ['in_c_wide_seed3_' + seed[2] + '_4g_woc', 'in_c_wide_seed4_' + seed[3] + '_4g_woc', 'in_c_wide_seed5_' + seed[4] + '_4g_woc', 'in_c_wide_seed6_' + seed[5] + '_4g_woc']
in_c_wide_woc_multipleSeeds_0gy = ['in_c_wide_seed3_' + seed[2] + '_0g_woc', 'in_c_wide_seed4_' + seed[3] + '_0g_woc', 'in_c_wide_seed5_' + seed[4] + '_0g_woc', 'in_c_wide_seed6_' + seed[5] + '_0g_woc']

in_c_wide_multipleSeeds_4gy = ['in_c_wide_seed3_' + seed[2] + '_4g', 'in_c_wide_seed4_' + seed[3] + '_4g', 'in_c_wide_seed5_' + seed[4] + '_4g', 'in_c_wide_seed6_' + seed[5] + '_4g']
in_c_wide_multipleSeeds_0gy = ['in_c_wide_seed3_' + seed[2] + '_0g', 'in_c_wide_seed4_' + seed[3] + '_0g', 'in_c_wide_seed5_' + seed[4] + '_0g', 'in_c_wide_seed6_' + seed[5] + '_0g']

in_c_multipleSeeds_3945gy = ['in_c_seed1_' + seed[0] + '_3945g', 'in_c_seed2_' + seed[1] + '_3945g', 'in_c_seed3_' + seed[2] + '_3945g', 'in_c_seed4_' + seed[3] + '_3945g', 'in_c_seed5_' + seed[4] + '_3945g', 'in_c_seed6_' + seed[5] + '_3945g']
in_c_multipleSeeds_wide_4gy = ['in_c_seed1_' + seed[0] + '_wide_4g', 'in_c_seed2_' + seed[1] + '_wide_4g', 'in_c_seed3_' + seed[2] + '_wide_4g', 'in_c_seed4_' + seed[3] + '_wide_4g', 'in_c_seed5_' + seed[4] + '_wide_4g', 'in_c_seed6_' + seed[5] + '_wide_4g']

N = 6
M = 0

#    Histogram names     #
histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist"
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16.hist"



#    histograms for runs #
#histogram_for_nbody_run = in_c_wide_woc_multipleSeeds_0gy
histogram_for_nbody_run = in_c_multipleSeeds_wide_4gy

output1 = 'cm_test/outs/' + in_c_hists_wide[0] + '.out'
output2 = 'cm_test/outs/' + in_c_hists_wide[1] + '.out'

match_hist_correct = "cm_test/hists/" + in_c_wide_woc_multipleSeeds_0gy[0] + ".hist"
match_hist_compare = "cm_test/hists/" + in_c_wide_woc_multipleSeeds_0gy[0] + ".hist"

#lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"

lua = "EMD_20k_v156_fixed_seed.lua"
#lua = "Null.lua"
folder = 'hists/multiseed_test'
outs = 2 
x = 1

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
        #print('q = ', q)
        j = 1
        q = i 
        os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody \
            -f ~/Desktop/research/lua/" + lua + " \
            -z ~/Desktop/research/quick_plots/" + folder + "/" + histogram_for_nbody_run[i] + ".hist \
            -o ~/Desktop/research/quick_plots/" + folder + "/" + histogram_for_nbody_run[i] + ".out \
            -n 8 -x -e " + seed[q] + " -i " + sim_time[j] + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
i = 0
if(match_histograms == True):
    print "matching histograms: "
    while(1):
        #using call here instead so the format of using it is on record
        print("matching hist:\n 1. %s \n 2. %s" % (histogram_for_nbody_run[i], histogram_for_nbody_run[i + x]))
        print("likelihood:")
        call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody  " 
            + " -h ~/Desktop/research/quick_plots/" + folder + "/" + histogram_for_nbody_run[i] + ".hist"
            + " -s ~/Desktop/research/quick_plots/" + folder + "/" + histogram_for_nbody_run[i + x] + ".hist"], shell=True)
        
        #lines = open('temp.out').readlines()
        #for line in lines:
            #like = line.split()
            #like = float(like[0])
        #call(["rm temp.out"], shell=True)
        #print 'likelihood = ', like, '\n'
        
        i = i + 2
        if(i >= len(histogram_for_nbody_run)):
            break

if(plot_plot_hists == True):
    os.system("./plot_matching_hist.py " + match_hist_correct + " " + match_hist_compare)

    
if(calc_cm == True):
    if(outs == 2):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./cm_shift_test.py " + mass_l + " " + mass_ratio + " " + output)
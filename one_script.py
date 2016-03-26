#! /usr/bin/python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # # # #\#
                #    One script to rule them all.   #
                #    One script to call them        #
                #    One script to run them.        #
                #    And in the folder, bind them   #
                #\# # # # # # # # # # # # # # # # #/#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import subprocess
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
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
#args = [4, 0.9862, 0.2, 0.2, 12, 0.2]

#    SWITCHES for standard_run()  #
run_nbody = n
remake    = n 
match_histograms = n 

calc_cm = n
plot_hists = n
plot_lb = n 

# possible tests #
run_diff_OS_test = n
run_binary_compare = n
run_stability_test = n

#    Histogram names     #
histogram_mw_1d_v158 = "tidal_histogram_EMD_20k_v158_ft3p945_rt0p98_r0p2_rr0p2_ml12_mr0p2__3_21_16"

#    histograms for runs #
histogram_for_nbody_run = 'test'
output = histogram_for_nbody_run
match_hist_correct = "test"
match_hist_compare = "test"
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

version = '' #determines which binary is run
lua = "EMD_20k_v158_fixed_seed.lua"

outs = 2 #for the cm calculation function

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#    standard nbody running functions     #
# # # # # # # # # # # # # # # # # # # # # #
def standard_run():
    if(remake == True):
        make_nbody()
    
    if(run_nbody == True):
        nbody(args, lua, histogram_for_nbody_run, output, version)
    
    if(match_histograms == True):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(calc_cm == True):
        calculate_cm(args, output1, output2, outs)
    
    if(plot_hists == True):
        plot(match_hist_correct + ".hist  " , match_hist_compare + ".hist")
    
    if(plot_lb == True):
        os.system("./scripts/lb_plot.py quick_plots/outputs/" + output)
        
def make_nbody():
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    
def nbody(paras, lua_file, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h ~/Desktop/research/quick_plots/hists/" + match_hist_correct + ".hist \
    
    print('running nbody')
    os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + ver + " \
        -f ~/Desktop/research/lua/" + lua_file + " \
        -z ~/Desktop/research/quick_plots/hists/" + hist + ".hist \
        -o ~/Desktop/research/quick_plots/outputs/" + out + ".out \
        -n 8 -x -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )

def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + ver  
          + " -h ~/Desktop/research/quick_plots/hists/" + hist1 + '.hist'
          + " -s ~/Desktop/research/quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"

def plot(hist1, hist2):
    os.system("./quick_plots/plot_matching_hist.py " + hist1 + " " + hist2)

def calculate_cm(paras, output1, output2, outs):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
    
    if(outs == 2):
        os.system("./scripts/output_cm_calc.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./scripts/output_cm_calc.py " + mass_l + " " + mass_ratio + " " + output)
    
# # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#        differenct test functions        #
# # # # # # # # # # # # # # # # # # # # # #
def stabity_test():
    args = [0.9862, 0.2, 0.2, 12, .2]

    sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
    ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
    N               = 1
    M               = 0
    back_time       = str(args[0])
    r_l             = str(args[1])
    light_r_ratio   = str(args[2])
    mass_l          = str(args[3])
    mass_ratio      = str(args[4])
    
    stability_rebuild = y
    stability_run     = y
    
    if(stability_rebuild == True):
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    
    if(stability_run == True):
        for i in range(M, N):
            os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
                -f ~/Desktop/research/lua/Null.lua \
                -o ~/Desktop/research/data_testing/sim_outputs/output_" + (ext[i]) + "gy.out \
                -n 8 -x -i "+ str(sim_time[i]) + " " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )

    os.chdir("data_testing")    
    os.system("./stability_test.py " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # # # # # # # # # # # # # #
def old_new_binary_compare():
    binary_run_nbody = n
    binary_match_histograms = n
    binary_plot_hists = n
    binary_calc_chi_sq = n
    
    versions = ['_154', '_158']
    time  = "1"
    binary_outputs = [with_lua_correction_on_old_binary + time + "gy.out", with_correction_on_new_binary + time + "gy.out"]
    binary_hists   = [with_lua_correction_on_old_binary + time + "gy.hist", with_correction_on_new_binary + time + "gy.hist"]
    folder = "/home/sidd/Desktop/research/outputs/"
    binary_lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"
    
    if(binary_run_nbody == True):
        nbody(args, binary_lua, binary_hists[0], binary_outputs[0], versions[0], 0)
        nbody(args, binary_lua, binary_hists[1], binary_outputs[1], versions[1], 1)
    
    if(binary_match_histograms == True):
        match_hists(binary_hists[0], binary_hists[0], versions[0]) #match old hist on the old binary
        match_hists(binary_hists[1], binary_hists[1], versions[0]) #match new hist on the old binary
        
        match_hists(binary_hists[0], binary_hists[0], versions[1]) #match old hist on the new binary
        match_hists(binary_hists[1], binary_hists[1], versions[1]) #match old hist on the new binary
        
    if(binary_plot_hists == True):
        plot(hists[0], hists[1])
        
    #os.system("mv " + names[0] + " " + names[1] + " quick_plots")
    
    if(binary_calc_chi_sq == True):
        os.system("./scripts/old_new_binary_chi_sq.py " + folder + outputs[0] + " " + folder + outputs[1] + " " + "output")
# # # # # # # # # # # # # # # # # # # # # #
def diff_OS_test():
    args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2]
    #OS: 
    #MW_like = 
    #laptop_like = 
    hist = 'test1'
    output = 'test1'
    nbody(args, lua, hist, output)
    match_hists(histogram_mw_1d_v158, hist)
    
    args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2]
    #OS: 
    #MW_like = 
    #laptop_like = 
    hist = 'test2'
    output = 'test'
    nbody(args, lua, hist, output)
    match_hists(histogram_mw_1d_v158, hist)
    
    args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2]
    #OS: 
    #MW_like = 
    #laptop_like = 
    hist = 'test3'
    output = 'test'
    nbody(args, lua, hist, output)
    match_hists(histogram_mw_1d_v158, hist)
# # # # # # # # # # # # # # # # # # # # # #
def clean():
    os.system("rm boinc_finish_called")
    os.system("rm boinc_milkyway_nbody_1.54_x86_64-pc-linux-gnu__mt_0")
    os.system("rm boinc_milkyway_nbody_1.58_x86_64-pc-linux-gnu__mt_0")
    
def main():    
    standard_run()
    
    if(run_binary_compare == True):
        old_new_binary_compare()
        
    if(run_diff_OS_test == True):
        diff_OS_test()
    
    if(run_stability_test == True):
        stabity_test()
    clean()
    
main()
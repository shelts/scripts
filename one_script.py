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
import matplotlib.patches as mpatches
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
#args = [3.945, 0.9862, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [0.0000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [3.95, 0.98, 0.2, 0.8, 12, 48] #for hist with dark matter
args = [3.96509911271539, 0.931875356807537, 0.46182892204695, 0.206712561291835, 13.1087647177516, 69.9587140449245]
#    SWITCHES for standard_run()  #
run_nbody = n
remake    = n
match_histograms = n

calc_cm = n
plot_hists = n
plot_overlapping = n
plot_adjacent = n
plot_lb = n 

# possible tests #
recalc_para_sweep_likes = n
make_a_few_hists = n
run_diff_OS_test = n
run_binary_compare = n
run_stability_test = n
run_seed_fluctuation_test = n
velocity_dispersion_calc = y

#    Histogram names     #
histogram_mw_1d_v160 = 'hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16'
#    histograms for runs #
histogram_for_nbody_run = 'test'

match_hist_correct = histogram_mw_1d_v160
match_hist_compare = histogram_for_nbody_run
plot_name = 'mw_hist'

output = histogram_for_nbody_run
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

version = '' #determines which binary is run
#lua = "EMD_v160.lua"
lua = "EMD_v160_direct_fit.lua"

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
        plot(match_hist_correct + ".hist" , match_hist_compare + ".hist", plot_name)
    
    if(plot_lb == True):
        os.system("./scripts/lb_plot.py quick_plots/outputs/" + output)
# # # # # # # # # #         
def make_nbody():
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
# # # # # # # # # #           
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
        -n 8 -x  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
    
# # # # # # # # # #     
def nbody_custom_lua(paras, lua_file, hist, out, ver, seed, bins):#this is for lua files that have non-normal parameters
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
        -n 8 -x -e " + seed + " -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " " + bins)
# # # # # # # # # #       
def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + ver  
          + " -h ~/Desktop/research/quick_plots/hists/" + hist1 + '.hist'
          + " -s ~/Desktop/research/quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"
# # # # # # # # # #       
def match_hists_piped(hist1, hist2, ver, pipe_name):
    os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + ver  
                + " -h ~/Desktop/research/quick_plots/hists/" + hist1 + '.hist'
                + " -s ~/Desktop/research/quick_plots/hists/" + hist2 + '.hist'
                + "  2>>'" + pipe_name + ".txt' ")

# # # # # # # # # #  
def plot(hist1, hist2, name):
    ylimit = 0.4
    xlower = 50
    xupper = -75
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    #os.system("~/Desktop/research/scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    plot_hist1 = hist1
    plot_hist2 = hist2
    
    print("plotting histograms\n")
    lines = []
    #print(os.getcwd())
    lines = open(folder + plot_hist1).readlines();
    
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("betaBins")):
            break 
    lines = lines[starting_line:len(lines)]
    
    sim_l = []
    sim_n = []
    for line in lines:
        if (line.startswith("</histogram>")):
            continue
        tokens = line.split();
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            cts = float(tokens[3])
            sim_l.append(lda)
            sim_n.append(cts)

    lines = []
    lines = open(folder + plot_hist2).readlines();
    
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("betaBins")):
            break 
    lines = lines[starting_line:len(lines)]
    
    data_l = []
    data_n = []
    for line in lines:
        if (line.startswith("</histogram>")):
            continue
        tokens = line.split()
        if tokens:
            dat_l = float(tokens[1])
            dat_n = float(tokens[3])
            data_l.append(dat_l)
            data_n.append(dat_n)
            
    if(plot_overlapping == True):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(sim_l, sim_n, width = w_overlap, color='k', alpha=1, label= plot_hist1)
        plt.bar(data_l, data_n, width = w_overlap, color='r', alpha=0.5, label= plot_hist2)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        #plt.show()
        
    if(plot_adjacent == True):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(sim_l, sim_n, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(212)
        plt.bar(data_l, data_n, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        #plt.show()
        return 1
# # # # # # # # # #       
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
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
def velocity_dispersion():
    args = [0.1, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    nbody(args, l, file_name, file_name, version)
    os.system("./scripts/velocity_dispersion.py " + file_name)
# # # # # # # # # # # # # # # # # # # # # #
def recalculate_parameter_sweep_likelihoods():
    args = [3.95, 3.95, 0.2, 0.8, 12, 48]
    sim_time      = str(args[0])
    back_time     = str(args[1])
    rl            = str(args[2])
    rd            = str(args[3])
    mass_l        = str(args[4])
    mass_d        = str(args[5])
    names   = ['ft', 'rad', 'rr', 'mass', 'mr_50bins']
    folder = "parameter_sweep_hists/"
    
    hist_range = [2., 1200.0, 23.0]
    hist_correct = folder + names[4] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm " + names[4] + ".txt")
    while(name <= hist_range[1]):
        mass_d = str(name)
        hist_name = folder + names[4] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', names[4])
        name += hist_range[2]
    mass_d = str(args[5])
    
    hist_range = [8.0, 16.0, 0.25]
    hist_correct = folder + names[3] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm mass.txt")
    while(name <= hist_range[1]):
        mass_l = str(name)
        hist_name = folder + names[3] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'mass')
        name += hist_range[2]
    mass_l = str(args[4])
    
    hist_range = [0.7, 0.9, 0.01]
    hist_correct = folder + names[2] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm rr.txt")
    while(name <= hist_range[1]):
        rd = str(name)
        hist_name = folder + names[2] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'rr')
        name += hist_range[2]
    rd = str(args[3])
    
    
    hist_range = [0.1, 0.3, 0.01]
    hist_correct = folder + names[1] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm rad.txt")
    while(name <= hist_range[1]):
        rl = str(name)
        hist_name = folder + names[1] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'rad')
        name += hist_range[2]
    rl = str(args[2])    
        
    args = [3.95, 0.98, 0.2, 0.8, 12, 48]
    sim_time      = str(args[0])
    back_time     = str(args[1])
    rl            = str(args[2])
    rd            = str(args[3])
    mass_l        = str(args[4])
    mass_d        = str(args[5])
    
    hist_range = [3.85, 4.3, 0.025]
    hist_correct = folder + names[0] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm ft.txt")
    while(name <= hist_range[1]):
        sim_time = str(name)
        hist_name = folder + names[0] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'ft')
        name += hist_range[2]

    os.system("mv " + names[4] + ".txt ~/Desktop/research/like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv mass.txt ~/Desktop/research/like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv rad.txt ~/Desktop/research/like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv rr.txt  ~/Desktop/research/like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv ft.txt ~/Desktop/research/like_surface/1D_like_surface/parameter_sweeps")
    os.chdir("like_surface")
    os.system("./one_like_script.py")
    return 1
# # # # # # # # # # # # # # # # # # # # # #
def make_some_hists():
    ver = ''
    para = [3.95, 0.98, 0.2, 0.2, 12, 0.2] #hist2 correct
    hist = "total_sim_test2"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 15, 0.2] #hist3 different mass
    hist = "total_sim_test3"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.93, 0.98, 0.2, 0.2, 12, 0.2] #hist4 slightly different sim time
    hist = "total_sim_test4"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 13, 0.2] #hist5 slightly different mass
    hist = "total_sim_test5"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 13, 0.213] #hist6 slightly different mass same DM mass
    hist = "total_sim_test6"
    #3.95  4.030612244898
    #0.2  0.8
    #48.032863849765     13
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 4.03061, 0.2, 0.8, 13, 48] #hist7 slightly different mass same DM mass (samish as 6)
    hist = "total_sim_test7"
    #3.95  4.03061
    #0.2  0.8
    #48   13
    nbody(para, lua, hist, hist, ver)
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
def different_seed_fluctuation():
    make_compare_hists = n
    make_correct_hists = y
    compare_only = n
    
    args = [3.95, 0.98, 0.2, 0.8, 12, 48]
    v = '_160'
    l = 'seed_test.lua'
    seed = [435833, 8376425, 34857265, 3462946, 8974526, 87625496, 76235986, 136725897, 39685235, 51699263]
    bins = [100, 200, 300, 400]
    if(make_correct_hists == True):
        for j in range(1, len(bins)):
            seed_default = '34086709' #this is the seed it was originally created with
            hist = 'hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16_bins' + str(bins[j])
            nbody_custom_lua(args, l, hist, hist, v, seed_default, str(bins[j]))
    
    if(make_compare_hists == True):
        for j in range(0, len(bins)):
            for i in range(0, len(seed)):
                hist = 'seed_test/seed' + str(seed[i]) + '_bins' + str(bins[j])  
                nbody_custom_lua(args, l, hist, hist, v, str(seed[i]), str(bins[j]))
                match_hists(histogram_mw_1d_v160, hist, v )
                
    if(compare_only == True):
        for j in range(0, len(bins)):
            for i in range(0, len(seed)):
                hist_correct = 'hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16_bins' + str(bins[j])
                hist = 'seed_test/seed' + str(seed[i]) + '_bins' + str(bins[j])  
                match_hists(hist_correct, hist, v )
                
                
# # # # # # # # # # # # # # # # # # # # # #
def diff_OS_test_v160():
    v = '_160'
    #linux
    args = [3.70778452511877, 1.01667175907642, 0.254742649011314, 0.143711601383984, 11.3450273240451, 574.759386941092]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_2757434 [1146228735]
    #MW_like = 579.736066389484677
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded1'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    
    args = [4.27052977262065, 0.898590506706387, 1.13573807105422, 1.05763955467846, 4.26117976009846, 505.117312682793]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit:ps_nbody_4_14_16_orphansim_v160_1_1453826702_2757546 [1146230255]
    #MW_like = -2411.196889060096055
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded2'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    args = [4.28939779102802, 1.1479856419377, 0.81844124076888, 1.40610990077257, 42.8358124603983, 493.859601157717]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_2757751 [1146232693]
    #MW_like = -12991.388977929243993
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded3'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    args = [3.90124507574365, 0.940801729913801, 0.864376512635499, 0.365644396073185, 54.3746401073877, 376.632761744782]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_4_14_16_orphansim_v160_1_1453826702_2757837 [1146235164]
    #MW_like = -1103.915226218623047
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded4'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    args = [3.15275016007945, 1.01077198171988, 0.518699688930064, 1.16948326204438, 45.0927923207637, 224.0722140742]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_4_14_16_orphansim_v160_1_1453826702_2758001 [1146237706]
    #MW_like = -7276.429429114665254
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded5'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    args = [3.47986795054749, 1.13666507601738, 0.755570971686393, 1.23453689094167, 50.398002382135, 426.925432941876]
    #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_4_14_16_orphansim_v160_3_1453826702_2758209 [1146240830]
    #MW_like = -17637.067619180670590
    #laptop_like = 
    hist = 'OS_test/linux_multithreaded6'
    output = hist
    nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    match_hists(histogram_mw_1d_v160, hist, v)
# # # # # # # # # # # # # # # # # # # # # #
def diff_OS_test_v158():
    v = ''
    #windows
    args = [4.29822369291337, 0.903418915209326, 0.96168017496667, 0.636458776995275, 34.646854473218, 0.310731262105537]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_3_1453826702_1539995 [1126649807]
    #MW_like = -3.941582191124151
    #laptop_like = 3.380992366981500
    hist = 'OS_test/windows_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)

    args =  [3.64909463274645, 0.800092264528703, 1.29968128990876, 0.572091462517946, 119.996024088228, 0.294493798125456]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_1_1453826702_1691839 [1129898216]
    #MW_like =  0.668375079402415
    #laptop_like =  0.881392082076118
    hist = 'OS_test/windows_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.65144453661503, 0.919067429256722, 1.22340315081706, 0.854927185363449, 39.0082337940657, 0.500514083832232]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_3_1453826702_1708283 [1130209342]
    #MW_like =  0.140110685580532
    #laptop_like =  0.182138917764999
    hist = 'OS_test/windows_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)   
    
    args =  [4.19661544276295, 0.897629903758155, 1.29495109835948, 0.896362260366003, 52.5909815487292, 0.542975688910794]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_8_16_orphansim_v156_1_1453826702_1415872 [1122507395]
    #MW_like =  1.132654164145936
    #laptop_like =  10.256920398728917
    hist = 'OS_test/windows_multithreaded4'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [3.59013215543578, 0.8, 1.3, 0.61475411883109, 120, 0.310571082931839]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_1_1453826702_1694659 [1129955208]
    #MW_like =  21.420239313972647
    #laptop_like =  20.349634374025626
    hist = 'OS_test/windows_multithreaded5'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.59379936660717, 0.917773637213971, 1.23133908813293, 0.852202997878081, 39.1675896978381, 0.503544745988189]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_3_1453826702_1694823 [1129959188]
    #MW_like =  0.701643535578343
    #laptop_like =  2.412993814130235
    hist = 'OS_test/windows_multithreaded6'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    #linux:    
    args = [3.54663939082478, 0.817954573674686, 1.27616329135743, 0.615843914911811, 118.889074577371, 0.325446608590623]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1551799 [1126955705]
    #MW_like = -447.279182742111402
    #laptop_like = 436.441079660549804
    hist = 'OS_test/linux_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args = [3.55130600333676, 0.8, 1.3, 0.64627393759699, 120, 0.335997932965623]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1683119 [1129726733]
    #MW_like = -37.147633105012268
    #laptop_like = 31.344591576360859
    hist = 'OS_test/linux_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args = [3.70941156624545, 0.8, 1.3, 0.594552172354105, 120, 0.296728543273283]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1706469 [1130177360]
    #MW_like = -1.158941882456867
    #laptop_like = 0.153304537068448
    hist = 'OS_test/linux_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args = [4.19661544276295, 0.897629903758155, 1.29495109835948, 0.896362260366003, 52.5909815487292, 0.542975688910794]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_8_16_orphansim_v156_1_1453826702_1415872 [1122507395]
    #MW_like = -1.132654164145936
    #laptop_like =  10.256920398728917
    hist = 'OS_test/linux_multithreaded4'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args = [3.56693763038042, 0.8, 1.3, 0.554551674635198, 119.854123758034, 0.305987721006952] 
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1697633 [1130014242]
    #MW_like = -4.074673238994799 
    #laptop_like =  5.045502971691247
    hist = 'OS_test/linux_multithreaded5'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    #mac
    args = [4.85215253988281, 0.811699599213898, 0.259284052159637, 0.892385273054242, 101.71602185443, 0.366507535497658]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1419252 [1122650947]
    #MW_like = -568.469347072597884
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args =  [3.48619072407142, 0.93569692173099, 0.997117511086704, 0.88680122652172, 29.086175902524, 0.309459403191991]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit:  ps_nbody_3_8_16_orphansim_v156_2_1453826702_1418150 [1122562759]
    #MW_like =  -0.709366128677001
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.32493866118717, 0.90350496717366, 1.29756680316448, 0.891263826616564, 48.8403305705139, 0.544722103651006]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit:  ps_nbody_3_8_16_orphansim_v156_1_1453826702_1390970 [1121841784]
    #MW_like =  -2.121557178729414
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    return 1
# # # # # # # # # # # # # # # # # # # # # #
def clean():
    os.system("rm boinc_finish_called")
    os.system("rm boinc_milkyway_nbody_1.54_x86_64-pc-linux-gnu__mt_0")
    os.system("rm boinc_milkyway_nbody_1.58_x86_64-pc-linux-gnu__mt_0")
    
def main():    
    standard_run()
    
    if(make_a_few_hists == True):
        make_some_hists()
    
    if(run_binary_compare == True):
        old_new_binary_compare()
        
    if(run_diff_OS_test == True):
        diff_OS_test_v160()
        #diff_OS_test_v158()
    
    if(run_stability_test == True):
        stabity_test()
    
    if(recalc_para_sweep_likes == True):
        recalculate_parameter_sweep_likelihoods()
    
    if(run_seed_fluctuation_test == True):
        different_seed_fluctuation()
    
    if(velocity_dispersion_calc == True):
        velocity_dispersion()
    
    #clean()
    
main()
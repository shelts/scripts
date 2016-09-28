#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
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
import matplotlib.pyplot as plt
from matplotlib import cm
import math as mt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np
import random
random.seed(a = 12345678)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
args = [3.95, 0.98, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [0.000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter

#args = [3.30911987740549, 0.916102936025716, 1.12718301676212, 0.1, 103.027752634138, 0.01]
#args = [5, 0.969492704328154, 0.1, 0.1, 25.3226470423393, 0.95]#-5.851168932
#args = [4.7954947538674, 0.968157430551938, 0.1, 0.157181217824109, 27.4116374908477, 0.95]#-7.072973562,


# # # # # # # # # # # # # # # # # # # # # # # #
#    SWITCHES for standard_run()  #           #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = n                 #
match_histograms          = n                 #
run_and_compare           = n                 #
plot_multiple             = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
charles                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
calc_cm                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_hists                = n                 #
plot_overlapping          = y                 #
plot_adjacent             = y                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_lb                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
get_fornax_binary_now     = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
# possible tests #                            #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_dispersion_calc  = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_a_few_hists          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
run_stability_test        = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
run_mixeddward_test       = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
slight_hist_change_test   = n                 #
surface_spikes            = n                 #
orbit_loc_test            = y                 #
# # # # # # # # # # # # # # # # # # # # # # # #


#    Histogram names     #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'
histogram_mw_1d_v162_1comp = 'hist_v162_ft3p945_rt0p98_r0p2_m12__8_30_16'
histogram_mw_1d_v162_2k = "hist_v162_2k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__7_11_16"
histogram_mw_1d_v162_2k_25bins = "hist_v162_2k__25bins_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_14_16"
histogram_mw_1d_v162_20k_25bins = "hist_v162_20k__25bins_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_14_16"

#    histograms for runs #
test = 'bestfit_2k_1000pop_sept14'

#hist to match against for compare after run
correct_hist = histogram_mw_1d_v162_20k_25bins
#hist name for the nbody run
histogram_for_nbody_run = histogram_mw_1d_v162_20k_25bins

#if you are just matching, these are the two hists
match_hist_correct = histogram_mw_1d_v162_1comp
match_hist_compare = histogram_mw_1d_v162_1comp
plot_name = histogram_for_nbody_run

output = plot_name
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
#lua = "mixeddwarf.lua"
lua = "EMD_v162.lua"
#lua = "EMD_v162_onecomp.lua"

outs = 2 #for the cm calculation function

#I am tired of constantly adapting it for the servers
lmc_dir = '~/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = sid_dir
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
        
    if(plot_multiple == True):    
        multiple_plot()
    
    if(run_nbody == True):
        nbody(args, lua, histogram_for_nbody_run, output, version, False)
    
    if(run_and_compare == True):
        compare_after_run(args, lua, correct_hist, histogram_for_nbody_run, output, version)
    
    if(match_histograms == True):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(calc_cm == True):
        calculate_cm(args, output1, output2, outs)
    
    if(plot_hists == True):
        plot(match_hist_correct + ".hist" , match_hist_compare + ".hist", plot_name)
    
    #if(plot_lb == True):
        #os.system("./scripts/lb_plot.py quick_plots/outputs/" + output)
    return 0
# # # # # # # # # #         
def make_nbody():
        os.chdir("./")
        #-DCMAKE_C_COMPILER=/usr/bin/cc 
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=ON -DNBODY_STATIC=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
# # # # # # # # # #           
def nbody(paras, lua_file, hist, out, ver, should_pipe):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    
    if(should_pipe == False):
        print('running nbody')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 12 -b -P -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
    if(should_pipe == True):
        print('running nbody')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 12 -b -P  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " \
         2>> " + out + "_piped.out")
     
     
     
    os.chdir(path)
    #os.chdir("../")
# # # # # # # # # #     
def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
          + " -s " + path + "quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0

def match_hists_pipe(hist1, hist2, ver, pipe_name):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
          + " -s " + path + "quick_plots/hists/" + hist2 + '.hist' + " 2>>" + pipe_name], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0
# # # # # # # # # # 
def compare_after_run(paras, lua_file, correct, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    print('running nbody')
    os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
        -f " + path + "lua/" + lua_file + " \
        -h " + path + "quick_plots/hists/" + correct + ".hist \
        -z " + path + "quick_plots/hists/" + hist + ".hist \
        -o " + path + "quick_plots/outputs/" + out + ".out \
        -n 10 -b  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
# # # # # # # # # #
def plot_N(hists, name, N):
    ylimit = 0.4
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'

    #ls_counts = [ [][] ] 

    
    print("plotting histograms\n")
    
    read_data = False
    lbins1 = []
    counts1 = []
    lines = open(folder + plot_hist1, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins1.append(float(ss[1]))
                counts1.append(float(ss[3]))
                
    # # # # #
    read_data = False
    lbins2 = []
    counts2 = []
    lines = open(folder + plot_hist2, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins2.append(float(ss[1]))
                counts2.append(float(ss[3]))
            
            
    # # # # #      
    read_data = False
    lbins3 = []
    counts3 = []
    lines = open(folder + plot_hist1, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins3.append(float(ss[1]))
                counts3.append(float(ss[3]))
            
    if(plot_overlapping == True):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(lbins1, counts1, width = w_overlap, color='k', alpha=1, label= plot_hist1)
        plt.bar(lbins2, counts2, width = w_overlap, color='r', alpha=0.5, label= plot_hist2)
        plt.bar(lbins3, counts3, width = w_overlap, color='r', alpha=0.5, label= plot_hist2)
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
        plt.bar(lbins1, counts1, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(212)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        
        
        plt.subplot(213)
        plt.bar(lbins3, counts3, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        #plt.show()
        return 1

def plot_4(hist1, hist2, hist3, hist4, hist5, name):
    ylimit = 0.4
    xlower = 60 
    xupper = -60
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    print "plot histogram 3: ", hist3
    
    plot_hist1 = hist1 + ".hist"
    plot_hist2 = hist2 + ".hist"
    plot_hist3 = hist3 + ".hist"
    plot_hist4 = hist4 + ".hist"
    plot_hist5 = hist5 + ".hist"
    
    label1 = 'correct\t 3.95'
    label2 = '3.9644355371 \t -10.047131423110589'
    label3 = '3.9658770516 \t -23.976349630274957 '
    label4 = '3.96601335775 \t -11.889794996330375 '
    label5 = '3.97192948281 \t -23.432419009906333'
    
    
    print("plotting histograms\n")
    
    read_data = False
    lbins1 = []
    counts1 = []
    lines = open(folder + plot_hist1, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins1.append(float(ss[1]))
                counts1.append(float(ss[3]))
                
    # # # # #
    read_data = False
    lbins2 = []
    counts2 = []
    lines = open(folder + plot_hist2, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins2.append(float(ss[1]))
                counts2.append(float(ss[3]))
            
            
    # # # # #      
    read_data = False
    lbins3 = []
    counts3 = []
    lines = open(folder + plot_hist3, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins3.append(float(ss[1]))
                counts3.append(float(ss[3]))
                
                
    # # # # #      
    read_data = False
    lbins4 = []
    counts4 = []
    lines = open(folder + plot_hist4, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins4.append(float(ss[1]))
                counts4.append(float(ss[3]))
    
    # # # # #      
    read_data = False
    lbins5 = []
    counts5 = []
    lines = open(folder + plot_hist5, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins5.append(float(ss[1]))
                counts5.append(float(ss[3]))       
    if(plot_overlapping == True):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(lbins1, counts1, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, counts2, width = w_overlap, color='r', alpha=0.75, label= label2)
        plt.bar(lbins3, counts3, width = w_overlap, color='b', alpha=0.5,  label= label3)
        plt.bar(lbins4, counts4, width = w_overlap, color='g', alpha=0.3,  label= label4)
        plt.bar(lbins5, counts5, width = w_overlap, color='y', alpha=0.2,  label= label5)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        #plt.show()
        
    if(plot_adjacent == True):
        plt.subplot(311)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(lbins1, counts1, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= label1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(312)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= label2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        
        
        plt.subplot(313)
        plt.bar(lbins3, counts3, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= label3)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        #plt.show()
        return 1

def plot(hist1, hist2, name, label1, label2):
    ylimit = 0.4
    xlower = 60 
    xupper = -60
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    #os.system("" + path + "scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    plot_hist1 = hist1 + ".hist"
    plot_hist2 = hist2 + ".hist"

    
    print("plotting histograms\n")
    read_data = False
    lbins1 = []
    counts1 = []
    lines = open(folder + plot_hist1, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins1.append(float(ss[1]))
                counts1.append(float(ss[3]))


    read_data = False
    lbins2 = []
    counts2 = []
    lines = open(folder + plot_hist2, 'r')
    for line in lines:
        if (line.startswith("betaBins")):
            read_data = True
            continue
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                lbins2.append(float(ss[1]))
                counts2.append(float(ss[3]))
            
            
    if(plot_overlapping):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(lbins1, counts1, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, counts2, width = w_overlap, color='r', alpha=0.75, label= label2)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        plt.clf()
        #plt.show()
        
    if(plot_adjacent):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(lbins1, counts1, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(212)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        plt.clf()
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
# # # # # # # # # #

def lb_plot(file_name):
    path_charles = 'quick_plots/outputs/'
    path = 'quick_plots/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = n
    plot_dm = n
    plot_xyz = n
    plot_orbit = y
    
    f = open(path_charles + file_name + '.out')
    lines = []
    lines = f.readlines()
    num = 1
    for line in lines:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    
    lines = lines[num:len(lines)]
    #print num
    light_x , light_y , light_z = ([] for i in range(3))
    light_l , light_b , light_r = ([] for i in range(3))
    light_vx , light_vy , light_vz = ([] for i in range(3))
    
    dark_x , dark_y , dark_z = ([] for i in range(3))
    dark_l , dark_b , dark_r = ([] for i in range(3))
    dark_vx , dark_vy , dark_vz = ([] for i in range(3))

    for line in lines:
        if(line.startswith("</bodies>")):
            break
        tokens = line.split(', ')
        isDark = int(tokens[0])
        X = float(tokens[1])
        Y = float(tokens[2])
        Z = float(tokens[3])
        l = float(tokens[4])
        if(l > 180.0):
            l = l - 360.0
        b = float(tokens[5])
        r = float(tokens[6])
        vx = float(tokens[7])
        vy = float(tokens[8])
        vz = float(tokens[9])
        if(isDark == 0):
            light_x.append(X)
            light_y.append(Y)
            light_z.append(Z)
            light_l.append(l)
            light_b.append(b)
            light_r.append(r)
            light_vx.append(vx)
            light_vy.append(vy)
            light_vz.append(vz)
        if(isDark == 1):
            dark_x.append(X)
            dark_y.append(Y)
            dark_z.append(Z)
            dark_l.append(l)
            dark_b.append(b)
            dark_r.append(r)
            dark_vx.append(vx)
            dark_vy.append(vy)
            dark_vz.append(vz)    
    #print(len(light_l))
    #print(len(dark_l))
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr == True):
        plt.figure(figsize=(20, 20))
        xlower = -180.0
        xupper = 180.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel('l')
        plt.ylabel('b')
        plt.title('l vs b')
        #default to just plot lm
        plt.plot(light_l, light_b, '.', markersize = 1.5, color = 'c', alpha=1.0, marker = '.')
        #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_light', format='png')
        print "plotting:", len(light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark == True):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter', format='png')
            print "plotting:", len(light_l) + len(dark_l), " points"
        # # # # # # # # # #
        if(plot_orbit == True):
            f = open(path + 'reverse_orbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'g', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            
            f = open(path + 'forward_orbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'r', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            plt.show()

        # # # # # # # # # #
        if(plot_dm == True):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_dark', format='png')
            
    if(plot_xyz == True):
        xlower = 50
        xupper = -50
        fig.tight_layout()
        plt.axes().set_aspect('equal')
        plt.subplot(131, aspect='equal')
        plt.plot(light_x, light_y, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('x vs y')
        
        plt.subplot(132,aspect='equal')
        plt.plot(light_x, light_z, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title('x vs z')
        
        plt.subplot(133, aspect='equal')
        plt.plot(light_z, light_y, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('z')
        plt.ylabel('y')
        plt.title('z vs y')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_xyz', format='png')
    
    return 0

# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
def velocity_dispersion():
    args = [3.95, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = 'nbody1'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    nbody(args, l, file_name, file_name, version, False)
    #lb_plot(file_name)
    os.system("./scripts/velocity_dispersion.py " + file_name)
# # # # # # # # # # # # # # # # # # # # # #
def make_some_hists():
    ver = '_1.62_x86_64-pc-linux-gnu__mt'
    lua_file = 'EMD_v162.lua'
    hist = 'hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_100bins'
    nbody(args, lua_file, hist, hist, ver, False)
    
    lua_file = 'EMD_v162_25bins.lua'
    hist = 'hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_25bins'
    nbody(args, lua_file, hist, hist, ver, False)
    
    lua_file = 'EMD_v162_50bins.lua'
    hist = 'hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_50bins'
    nbody(args, lua_file, hist, hist, ver, False)

    return 0
# # # # # # # # # # # # # # # # # # # # # #
def test_mixed_dwarf():
    ver = ''
    ft = 0.00001 #gyr
    bt = 1   #gyr
    rl = 0.8  #kpc
    rr = 0.5 #ratio
    ml = 30   #sim
    mr = 0.5   #ratio
    args = [ft, bt, rl, rr, ml, mr]
    
    lua_file = 'EMD_v162.lua'
    output = 'regular_initial'
    #nbody(args, lua_file, output, output, ver, n)
    
    
    lua_file = 'mixeddwarf.lua'
    #output = 'output_plummer_plummer_0gy'
    #output = 'output_hern_hern_0gy'
    output = 'output_nfw_nfw_0gy'
    nbody(args, lua_file, output, output, ver, n)
    os.system("mv ~/Desktop/research/quick_plots/outputs/" + output + ".out ~/Desktop/research/data_testing/sim_outputs/")
# # # # # # # # # # # # # # # # # # # # # #

def randomize(counts, errors, N):
    for i in range(0, N):
        coor1 = random.randint(0, len(counts) - 1)
        coor2 = random.randint(0, len(counts) - 1)
        while(coor1 == coor2):
            coor1 = random.randint(0, len(counts) - 1)
            coor2 = random.randint(0, len(counts) - 1)
        
        #print coor1, coor2, len(counts)
        count_tmp = counts[coor1]
        counts[coor1] = counts[coor2]
        counts[coor2] = count_tmp
    
        error_tmp = errors[coor1]
        errors[coor1] = errors[coor2]
        errors[coor2] = error_tmp
   
    return counts, errors

def slight_hist_alteration_study_bin_switch():
    Nchanges = 25
    folder = "quick_plots/hists/"
    
    histogram_mw_1d_v162_20k_25bins = "hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_25bins"
    histogram_mw_1d_v162_20k_50bins = "hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_50bins"
    histogram_mw_1d_v162_20k_100bins = "hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_100bins"

    name = "100bins"
    prestine = folder + histogram_mw_1d_v162_20k_100bins
    correct = histogram_mw_1d_v162_20k_100bins

    prestinef = open(prestine + ".hist", 'r')
    
    header = []
    counts = []
    errors = []
    col1   = []
    lbins  = []
    bbins  = []
    read_data = False
    read_header = True
    
    for line in prestinef:
        if(read_header):
            header.append(line)
        
        if(line.startswith("betaBins")):
            read_data = True
            read_header = False
            continue
        
        if(read_data):
            if(line.startswith("</histogram>")):
                break
            elif(line.startswith("\n")):
                continue
            else:
                ss = line.split(' ')
                col1.append(ss[0])
                lbins.append(ss[1])
                bbins.append(ss[2])
                
                count = float(ss[3])
                
                dd = ss[4].split("\n")
                error = float(dd[0])
                
                counts.append(count)
                errors.append(error)
    
    prestinef.close()
    counts_tmp = []
    errors_tmp = []
    for N in range(0, Nchanges):
        #print errors[18], errors[16]
        
        counts_tmp, errors_tmp = randomize(counts, errors, N)
        
        #print errors_tmp[18], errors_tmp[16]
        
        copy = prestine + "_" + str(N) + "changes"
        copyf = open(copy + ".hist", 'w')
        
        for i in range(0, len(header)):
            copyf.write(header[i])
        for i in range(0, len(col1)):
            copyf.write("%s %s %s %0.15f %0.15f\n\n" % (col1[i], lbins[i], bbins[i], counts_tmp[i], errors_tmp[i]))
        
        copyf.close()
        
        compare = correct + "_" + str(N) + "changes"
        
        match_hists_pipe(correct, compare, '', name)
        
        
    piped = name
    g = open(name, 'r')
    f = open("data_" + name + ".out", 'w')
    counter = 0
    for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s\t%i\n" % (tt[0], counter))#writes the first of the resplit lines
                counter += 1
    
    f.close()
    g.close()
    
    f = open('data_' + name + '.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key off\n")

    f.write("set xlabel 'number of changes'\n")
    f.write("set ylabel 'likelihood'\n")
    f.write("set yrange [-500:0]\n")
    f.write("set xrange[0:" + str(Nchanges) + "]\n")
        
    p = "./" + "data_" + name + ".out"
    f.write("set output 'quick_plots/plot_" + name + ".jpeg' \n")
    f.write("set title 'likelihood vs changes in hist with " + name + "' \n")
    f.write("plot '" + p + "' using 2:1  with lines\n\n") 

    f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot data_" + name + ".gnuplot 2>>piped_output.txt")
    os.system("rm gnuplot data_" + name + ".gnuplot")
    os.system("rm data_" + name + ".out")
    os.system("rm " + name)
    
    plot_3(histogram_mw_1d_v162_20k_25bins, histogram_mw_1d_v162_20k_50bins, histogram_mw_1d_v162_20k_100bins, 'same_hist_diff_bins')
    return 0


def surface_spike_invest():
    ver = ''
    paras = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
    lua_file = 'EMD_v162.lua'
    #correct = 'hist_v162_20k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__9_19_16_100bins'
    #nbody(args, lua_file, correct, correct, ver, False)
    
    paras = [3.964435537100000, 0.98, 0.2, 0.2, 12, 0.2]#-10.047131423110589
    hist1 = 'spike1' 
    #compare_after_run(paras, lua_file, correct, hist1, hist1, ver)
    #match_hists(correct, hist1, ver)
    
    paras = [3.965877051600000, 0.98, 0.2, 0.2, 12, 0.2]# -23.976349630274957
    hist2 = 'spike2' 
    #compare_after_run(paras, lua_file, correct, hist2, hist2, ver)
    #match_hists(correct, hist2, ver)
    
    #match_hists(hist1, 'arg_3.9644355371_0.98_0.2_0.2_12_0.2', '')
    
    hist3 = 'arg_3.96601335775_0.98_0.2_0.2_12_0.2' #-11.889794996330375
    hist4 = 'arg_3.97192948281_0.98_0.2_0.2_12_0.2' #-23.432419009906333
    
    #plot_4(correct, hist1, hist2, hist3, hist4,  'spike_hists')

    bins = '100'
    correct = 'parameter_sweeps_9_19_2016/hists_' + bins + 'bins_tight/arg_3.95_0.98_0.2_0.2_12_0.2_correct'
    f = open('quick_plots/hists/parameter_sweeps_9_19_2016/likelihood_data_rand_iter_' + bins + 'bins/ft_data_vals.txt', 'r')
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    for i in range(0, len(values)):
        hist_name = 'parameter_sweeps_9_19_2016/hists_' + bins + 'bins_tight/ft_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_0.2'
        label1 = '3.95'
        label2 = str(values[i]) + "  l=" + str(likes[i])
        plot(correct, hist_name, str(i), label1, label2)
    return 0

##def slight_hist_alteration_study_particle_shifting():
    
def orbit_location():    
    args = [2.0, 0.98, 0.2, 0.2, 12, 0.2]
    lua_file = "EMD_v162.lua"
    hist =  'orbit_test'
    #nbody(args, lua, hist, hist, version, False)
    os.system('mv nbody_test/bin/forward_orbit.out quick_plots/')
    os.system('mv nbody_test/bin/reverse_orbit.out quick_plots/')
    lb_plot(hist)
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
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    
    if(stability_run == True):
        for i in range(M, N):
            os.system("" + path + "nbody_test/bin/milkyway_nbody \
                -f " + path + "lua/Null.lua \
                -o " + path + "data_testing/sim_outputs/output_" + (ext[i]) + "gy.out \
                -n 8 -x -i "+ str(sim_time[i]) + " " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )

    os.chdir("data_testing")    
    os.system("./stability_test.py " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # # # # # # # # # # # # # #
def clean():
    os.system("rm boinc_*")
    
# # # # # # # # # # # # # # # # # # # # # #    
def main():
    if(get_fornax_binary_now):
        get_fornax_binary()
        
    standard_run()
    
    if(run_mixeddward_test):
        test_mixed_dwarf()
        
    if(charles):
        for_charles()
    
    if(make_a_few_hists):
        make_some_hists()
    
    #if(run_binary_compare):
        #old_new_binary_compare()
        
    #if(run_diff_OS_test):
        #diff_OS_test_v160()
        #diff_OS_test_v158()
    
    if(run_stability_test):
        stabity_test()
    
    #if(recalc_para_sweep_likes):
        #recalc_parameter_sweep_likelihoods()
    
    #if(run_seed_fluctuation_test):
        #different_seed_fluctuation()
    
    if(velocity_dispersion_calc):
        velocity_dispersion()
    
    if(plot_lb):
        lb_plot(output)
        
    if(slight_hist_change_test):
        slight_hist_alteration_study_bin_switch()
        
    if(surface_spikes):
        surface_spike_invest()
        
    if(orbit_loc_test):
        orbit_location()
    clean()
        
main()
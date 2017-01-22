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
#args = [1.0, 0.98, 0.2, 0.2, 12, 0.2] 
args = [0.000001, 1.0, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#    SWITCHES for standard_run()  #           #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = y                 #
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
lb_plot_switch            = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
# possible tests #                            #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_disp_switch      = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_some_hists_switch    = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
stabity_test_switch       = y                 #
# # # # # # # # # # # # # # # # # # # # # # # #
test_mixed_dwarf_switch   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
pots_dens_plot_switch     = n                 #
hstalt_binswap_switch     = n                 #
plot_all_hists_switch     = n                 #
orbit_location_switch     = n                 #
plot_n_ofhist_switch      = n                 #
check_hist_likes_switch   = n                 #
check_timestep_switch     = n                 #
quick_calculator_switch   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #


#    Histogram names     #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'

#    histograms for runs #
nfw  = 'output_nfw_nfw_0gy'
plum = 'output_plummer_plummer_0gy'
hern = 'output_hern_hern_0gy'
plum_nfw = 'output_plummer_nfw_0gy'
#hist to match against for compare after run
correct_hist = nfw
#hist name for the nbody run
histogram_for_nbody_run = correct_hist

#if you are just matching, these are the two hists
match_hist_correct = histogram_for_nbody_run
match_hist_compare = histogram_for_nbody_run
plot_name = histogram_for_nbody_run

output = histogram_for_nbody_run
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
lua = "mixeddwarf.lua"
#lua = "EMD_v162_bestlike.lua"

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
        nbody(args, lua, histogram_for_nbody_run, histogram_for_nbody_run, version, False)
    
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
            -n 8 -b -P -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
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
          + " -h " + path + "" + hist1 + '.hist'
          + " -s " + path + "" + hist2 + '.hist' + " 2>>" + pipe_name], shell=True)
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

def plot_4(hist1, hist2, hist3, hist4, name):
    ylimit = 0.1
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
    #plot_hist5 = hist5 + ".hist"
    
    label1 = 'correct\t 3.95'
    label2 = '-5.615887703633109'
    label3 = '-6.361401978455249 '
    label4 = '-4.853374558 '
    #label5 = '3.97192948281 \t -23.432419009906333'
    
    
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
    
    ## # # # #      
    #read_data = False
    #lbins5 = []
    #counts5 = []
    #lines = open(folder + plot_hist5, 'r')
    #for line in lines:
        #if (line.startswith("betaBins")):
            #read_data = True
            #continue
        #if(read_data):
            #if(line.startswith("</histogram>")):
                #break
            #elif(line.startswith("\n")):
                #continue
            #else:
                #ss = line.split(' ')
                #lbins5.append(float(ss[1]))
                #counts5.append(float(ss[3]))       
                
                
    if(plot_overlapping == True):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(lbins1, counts1, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, counts2, width = w_overlap, color='r', alpha=0.75, label= label2)
        plt.bar(lbins3, counts3, width = w_overlap, color='b', alpha=0.5,  label= label3)
        plt.bar(lbins4, counts4, width = w_overlap, color='g', alpha=0.3,  label= label4)
        #plt.bar(lbins5, counts5, width = w_overlap, color='y', alpha=0.2,  label= label5)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        #plt.show()
        
    if(plot_adjacent == True):
        plt.subplot(411)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(lbins1, counts1, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= label1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(412)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= label2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        
        
        plt.subplot(413)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= label3)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        
        plt.subplot(414)
        plt.bar(lbins3, counts3, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= label4)])
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
    folder = 'like_surface/'
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
    ver = ''
    lua_file = 'EMD_v162_malleable.lua'
    cor_hist = 'hist_v162_2k_ft3p95_rt0p98_rl0p2_rr0p2_ml12_mrp2__7_11_16'
    
    args = [4.98307971702889, 0.968890922982242, 0.104342397337317, 0.454711809661241, 25, 0.95]
    hist1 = 'mw_best_fit1.1'
    #nbody(args, lua_file, hist1, hist1, ver, False)
    #match_hists(cor_hist, hist1, ver)
   
    args = [4.31887475447728, 0.966407963540408, 0.109778609406203, 0.27909923158586, 24.6120846327394, 0.95]
    hist2 = 'mw_best_fit2'
    #nbody(args, lua_file, hist, hist, ver, False)
    match_hists(cor_hist, hist2, ver)
    
    args = [4.19554142467678, 0.965346934366972, 0.146965033782182, 0.5, 24.9266278594736, 0.95]
    hist3 = 'mw_best_fit3.1'
    #nbody(args, lua_file, hist3, hist3, ver, False)
    #compare_after_run(args, lua_file, cor_hist, hist3, hist3, ver)
    match_hists(cor_hist, hist3, ver)
    
    
    #plot_4(cor_hist, hist1, hist2, hist3, 'bestfit')
    
    
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

def hstalt_binswap():
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

# # # # # # # # # # # # # # # # # # # # # #
def plot_all_hists():
    ver = ''
    paras = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
    lua_file = 'EMD_v162.lua'
    sweep = 'parameter_sweeps_10_21_2016_post_best_like_fix_narrow_random_0.9sim'
    bins = '100'
    typ = 'ft'
    correct = sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/arg_3.95_0.98_0.2_0.2_12_0.2_correct'
    f = open('like_surface/' + sweep + '/' + bins + 'bins/likelihood_data_rand_iter_' + bins + 'bins/' + typ + '_data_vals.txt', 'r')
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    for i in range(0, len(values)):
        hist_name = sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/' + typ + '_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_0.2'
        label1 = '3.95gy'
        label2 = "ft = " + str(values[i]) + " likel =    " + str(likes[i]) + "% sim" + str(values[i]/3.95)
        plot(correct, hist_name, str(i), label1, label2)
    return 0
# # # # # # # # # # # # # # # # # # # # # #

def plot_n_ofhist():
    ver = ''
    sweep = 'parameter_sweeps_10_20_2016_post_best_like_fix_narrow_random_0.95sim'
    bins = '100'
    typ = 'ft'
    correct = 'like_surface/' + sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/arg_3.95_0.98_0.2_0.2_12_0.2_correct.hist'
    f = open('like_surface/' + sweep + '/' + bins + 'bins/likelihood_data_rand_iter_' + bins + 'bins/' + typ + '_data_vals.txt', 'r')
    
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    ns = []
    for i in range(0, len(values)):
        hist_name = 'like_surface/' + sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/' + typ + '_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_0.2.hist'
        hist = open(hist_name, 'r')
        for line in hist:
            if(line.startswith("n = ")):
                ss = line.split("n = ")
                n_values = float(ss[1])
                print n_values
                print values[i]
                ns.append(n_values)
                
    plt.plot(values, ns, color='r', label= 'n vs ft')
    plt.title('number of bodies in histogram vs ft')
    #plt.xlim((values[0], xupper))
    #plt.ylim((0.0, ylimit))
    plt.ylabel('n')
    plt.legend()
    plt.savefig('n_vs_ft.png', format='png')
    plt.show()
    plt.clf()           
    
    print n
    
    return 0
# # # # # # # # # # # # # # # # # # # # # #
def check_hist_likes():
    redo_likes = n
    plot_components = y
    ver = ''
    sweep = 'parameter_sweeps_10_20_2016_post_best_like_fix_narrow_random_0.95sim'
    bins = '100'
    typ = 'ft'
    correct = 'like_surface/' + sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/arg_3.95_0.98_0.2_0.2_12_0.2_correct'
    
    f = open('like_surface/' + sweep + '/' + bins + 'bins/likelihood_data_rand_iter_' + bins + 'bins/' + typ + '_data_vals.txt', 'r')
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    if(redo_likes):
        for i in range(0, len(values)):
            hist_name = 'like_surface/' + sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/' + typ + '_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_0.2'
            match_hists_pipe(correct, hist_name, ver, sweep)
            
    f.close()
    
    if(plot_components):
        g = open(sweep, 'r')
        emds = []
        costs = []
        likes = []
        for line in g:
            if(line.startswith("log(CostComponent) = ")):
                ss = line.split("log(CostComponent) = ")
                cost = float(ss[1])
                costs.append(cost)
            if(line.startswith("log(EMDComponent) = ")):
                ss = line.split("log(EMDComponent) = ")
                emd = float(ss[1])
                emds.append(emd)
            if(line.startswith("<search_likelihood>")):
                   ss = line.split("<search_likelihood>")
                   dd = ss[1].split("</search_likelihood>")
                   like = float(dd[0])
                   likes.append(like)
        g.close()
        
        plt.plot(values, emds, color='r', label= 'emd')
        plt.plot(values, costs, color='g', label= 'cost')
        plt.plot(values, likes, color='k', label= 'like')
        plt.title('number of bodies in histogram vs ft')
        #plt.xlim((values[0], xupper))
        plt.ylim((-50.0, 0.0))
        plt.ylabel('likelihood')
        plt.legend()
        plt.savefig('n_vs_ft.png', format='png')
        plt.show()
        plt.clf()
        
# # # # # # # # # # # # # # # # # # # # # #
def orbit_location():         
    lua_file = "EMD_v162_malleable.lua"
    hist =  'orbit_test2'
    run = n
    plot = n
    sweep_radii = y
    trash = n
    #os.system('mv nbody_test/bin/forward_orbit.out quick_plots/')
    #os.system('mv nbody_test/bin/reverse_orbit.out quick_plots/')
    #lb_plot(hist)
    
    if(trash):
        trash = trash
        #args = [3.945, 0.98, 0.2, 0.2, 12, 0.2]#rad: 33.746497660125655
        #nbody(args, lua_file, hist, hist, version, False)
        #args = [3.945, 0.8, 0.2, 0.2, 12, 0.2]#rad: 87.116406835446654
        #nbody(args, lua_file, hist, hist, version, False)

        #args = [3.945, 1.2, 0.2, 0.2, 12, 0.2]#rad: 78.866571119221959
        #nbody(args, lua_file, hist, hist, version, False)
        
        #args = [3.0, 0.98, 0.2, 0.2, 12, 0.2]#rad: 87.233271740740818
        #nbody(args, lua_file, hist, hist, version, False)

        #args = [3.0, 0.8, 0.2, 0.2, 12, 0.2]#rad: 31.251401116618435
        #nbody(args, lua_file, hist, hist, version, False)

        #args = [3.0, 1.2, 0.2, 0.2, 12, 0.2]#rad: 72.026652594362531
        #nbody(args, lua_file, hist, hist, version, False)
        
        
        #args = [5.0, 0.98, 0.2, 0.2, 12, 0.2]#rad: 81.563026239076436
        #nbody(args, lua_file, hist, hist, version, False)

        #args = [5.0, 0.8, 0.2, 0.2, 12, 0.2]#rad: 72.956494004603883
        #nbody(args, lua_file, hist, hist, version, False)

        #args = [5.0, 1.2, 0.2, 0.2, 12, 0.2]#rad: 52.676752723856929
        #nbody(args, lua_file, hist, hist, version, False)
        trash = trash
    
    
    if(run):#runs possible combos of paras to get distance from GC
        ft = 3.0
        bt = 0.8
        NN = 50
        MM = 50
        intv_ft = (5.0 - 3.0) / NN
        intv_bt = (1.2 - 0.8) / MM
        f = open('radii_paras.txt', 'w')
        for i in range(0, NN):
            bt = 0.8
            for j in range(0, MM):
                args = [ft, bt, 0.2, 0.2, 12, 0.2]
                f.write("%0.15f\t%0.15f\t%0.15f\n" % (ft, bt, ft / bt))
                #nbody(args, lua_file, hist, hist, version, False)
                bt += intv_bt
            ft += intv_ft
        f.close()
    
    os.system("mv nbody_test/bin/radii.out ./")
    if(plot):#this plots the radii from the GC it goes through
        f = open('radii_para.gnuplot', 'w')
        f.write("reset\n")
        f.write("set terminal wxt persist\n")
        #size 6000,2000\n")
        f.write("set key off\n")
        f.write("set xlabel 'forward time (Gyr)'\n")
        f.write("set ylabel 'reverse time ratio'\n")
        f.write("set zlabel 'radius GC (kpc)'\n")
        f.write("set xrange[2.9:5.4]\n")
        f.write("set yrange[0.78:1.24]\n")
        f.write("set zrange[0.0:100]\n\n\n")
        
        f.write("set output \"~/Desktop/research/quick_plots/radius_fromGC_vs_FT_BT.jpeg\" \n")
        p = "<paste radii_paras.txt radii.out"
        f.write("set title '' \n")
        f.write("splot '" + p + "' using 1:2:4  with points\n\n") 
                
        f.close()
    os.system("gnuplot radii_para.gnuplot 2>>piped_output.txt")
    os.system("rm radii_para.gnuplot")
    
    
    if(sweep_radii):
        get_radii = n
        if(get_radii):
            bins = '25'
            typ = 'ft'
            f = open('like_surface/parameter_sweeps_10_6_2016_narrow_random_sweep/25bins/likelihood_data_rand_iter_' + bins + 'bins/' + typ + '_data_vals.txt', 'r')
            vals = []
            for line in f:
                ss = line.split("\t")
                value = float(ss[0])
                like  = float(ss[1])
                vals.append(value)
            for i in range(0, len(vals)):
                args = [3.95, vals[i], 0.2, 0.2, 12, 0.2]
                nbody(args, lua_file, hist, hist, version, False)
                
            os.system("mv nbody_test/bin/radii_sweep.out ./")
        
        f = open('radii_sweep.out', 'r')
        radii = []
        for line in f:
            value = float(line)
            radii.append(value)
        
        plot_all_hists()
    
    return 0

# # # # # # # # # # # # # # # # # # # # # #
def check_timestep():
    rl = [0.05, 0.5]
    rr = [0.1, 0.5]
    ml = [1, 50]
    mr = [0.1, 0.95]
    f = open("times.txt", 'w')
    rl_inc = 0.1
    rr_inc = 0.05
    ml_inc = 1
    mr_inc = 0.05
    
    irl = rl[0]
    while(1):
        irr = rr[0]
        while(1):
            iml = ml[0]
            while(1):
                imr = mr[0]
                while(1):
                    dwarfMass = iml / imr
                    rscale_t  = irl / irr
                    rd  = rscale_t *  (1.0 - irr)
                    md    = dwarfMass * (1.0 - imr)
                    
                    
                    mass_enc_d = md * (irl)**3 * ( (irl)**2 + (rd)**2  )**(-3.0/2.0)

                    mass_enc_l = iml * (rd)**3 * ( (irl)**2 + (rd)**2  )**(-3.0/2.0)

                    s1 = (irl)**3 / (mass_enc_d + iml)
                    s2 = (rd)**3 / (mass_enc_l + md)
                    
                    if(s1 < s2):
                        s = s1
                    else:
                        s = s2
                    
                    t = (1 / 100.0) * ( mt.pi * (4.0 / 3.0) * s)**(1.0/2.0)
                    f.write("%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\n" % (t, irl, irr, iml, imr, rd, md))
                    
                    if(imr > mr[1]):
                        break
                    else:
                        imr += mr_inc
                
                if(iml > ml[1]):
                    break
                else:
                    iml += ml_inc
            
            if(irr > rr[1]):
                break
            else:
                irr += rr_inc
                
        if(irl > rl[1]):
            break
        else:
            irl += rl_inc
                    
                    
                    
                   
    f.close()

# # # # # # # # # # # # # # # # # # # # # #

def pots_dens_plot():
    f = open('pots_dens_plt.gnuplot', 'w')
    names = ["NFW", "PL", "GH"]
    if(n):    
        os.system("mv ./nbody_test/bin/dens_potsNFW.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/dist_funcNFW.out ./quick_plots/")
        
        os.system("mv ./nbody_test/bin/dens_potsGH.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/dist_funcGH.out ./quick_plots/")
        
        os.system("mv ./nbody_test/bin/dens_potsPL.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/dist_funcPL.out ./quick_plots/")
        
        f.write("reset\n")
        f.write("set terminal png size 900,1000 enhanced\n")
        f.write("set output './quick_plots/pots_dens.png' \n")
        f.write("set multiplot layout 3,4 rowsfirst\n")
        for i in range(0, len(names)):
            f.write("set key off\n")
            
            
            p = "./quick_plots/dens_pots" + names[i] + ".out"
            f.write("set title 'dens " + names[i] + " ' \n")
            f.write("set xlabel 'r'\n")
            f.write("set ylabel 'r^2 rho'\n")
            #f.write("set yrange [0:4]\n")
            #f.write("set xrange [0:10]\n")
            f.write("plot '" + p + "' using 1:2  with lines, \n\n") 
            
            f.write("set title 'potentials " + names[i] + " ' \n")
            f.write("set xlabel 'r'\n")
            f.write("set ylabel 'potential'\n")
            #f.write("set yrange [0:140]\n")
            #f.write("set xrange [0 :10 ]\n")
            f.write("plot '" + p + "' using 1:3  with lines, \n\n")
            f.write("# # # # # # # # # # # # # # # # # #\n")
            
            f.write("set title 'dist fun " + names[i] + " f(r)' \n")
            f.write("set xlabel 'r'\n")
            f.write("set ylabel 'v^2 f'\n")
            #f.write("set yrange[0:17]\n")
            #f.write("set xrange [0 : 1.2]\n")
            p = "./quick_plots/dist_func" + names[i] + ".out"
            f.write("plot '" + p + "' using 1:5  with lines, '" + p + "' using 7:5  with dots\n\n")
            
            f.write("set title 'dist fun " + names[i] + " f(v)' \n")
            f.write("set xlabel 'v'\n")
            f.write("set ylabel 'v^2 f'\n")
            #f.write("set yrange [0:4]\n")
            #f.write("set xrange [0:10]\n")
            p = "./quick_plots/dist_func" + names[i] + ".out"
            f.write("plot '" + p + "' using 4:6  with dots\n\n")
            
            #f.write("unset multiplot\n")
    
    if(n):
        os.system("mv ./nbody_test/bin/dist_func2D.out ./quick_plots/")
        f.write("reset\n")
        f.write("set terminal wxt persist\n")
        f.write("set key off\n")
        f.write("set xlabel 'r'\n")
        f.write("set ylabel 'v'\n")
        f.write("set zlabel 'v^2 f'\n")
        f.write("set xrange [0.8:1.0]\n")
        f.write("set yrange [0:10]\n")
        f.write("set zrange [0:]\n")
        #f.write("set cbrange [0 :0.001]\n")
        #f.write("set output './quick_plots/distfunc.png' \n")
        p = "./quick_plots/dist_func2D.out"
        f.write("splot '" + p + "' using 1:2:3  with dots \n\n")
    
    

    if(n):
        os.system("mv ./nbody_test/bin/energyNFW.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/energyPL.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/energyGH.out ./quick_plots/")
        
        f.write("reset\n")
        f.write("set terminal png size 900,1000 enhanced\n")
        f.write("set output './quick_plots/energy.png'\n")
        f.write("set multiplot layout 3,1 rowsfirst\n")
        for i in range(0, len(names)):
            p = "./quick_plots/energy" + names[i] + ".out"
            f.write("set title 'energy " + names[i] + " ' \n")
            f.write("set xlabel 'r'\n")
            f.write("set ylabel 'energy'\n")
            #f.write("set yrange [0:4]\n")
            f.write("set xrange [0:50]\n")
            f.write("plot '" + p + "' using 1:2  with lines title 'potential', '" + p + "' using 1:3  with lines title ' energy' \n\n") 

    
    if(y):
        os.system("mv ./nbody_test/bin/integrandNFW.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/integrandPL.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/integrandGH.out ./quick_plots/")
        
        f.write("reset\n")
        f.write("set terminal png size 700,900 enhanced\n")
        f.write("set output './quick_plots/integrand.png'\n")
        f.write("set multiplot layout 3,1 rowsfirst\n")
        ylims = ["-50", "-50", "-1000"]
        for i in range(0, len(names)):
            p = "./quick_plots/integrand" + names[i] + ".out"
            f.write("set title 'integrand " + names[i] + " ' \n")
            f.write("set xlabel 'r'\n")
            f.write("set ylabel 'integrand'\n")
            f.write("set yrange [0:" + ylims[i] + "]\n")
            f.write("set xrange [0:2]\n")
            f.write("plot '" + p + "' using 1:2  with lines title 'integrand', '" + p + "' using 8:2  with lines title ' upperlimit',  '" + p + "' using 9:2  with lines title ' lowerlimit' \n\n") 

    if(n):
        os.system("mv ./nbody_test/bin/NFW.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/PL.out ./quick_plots/")
        os.system("mv ./nbody_test/bin/GH.out ./quick_plots/")
        
        f.write("reset\n")
        f.write("set terminal png size 900,1000 enhanced\n")
        f.write("set output './quick_plots/sampling.png'\n")
        f.write("set multiplot layout 3,1 rowsfirst\n")
        ylims = ["-1000", "-200", "-1000"]
        for i in range(0, len(names)):
            p = "./quick_plots/" + names[i] + ".out"
            f.write("set title 'sampling" + names[i] + " ' \n")
            f.write("set xlabel 'n'\n")
            f.write("set ylabel 'pick'\n")
            f.write("set yrange [0:1]\n")
            f.write("set xrange [0:20]\n")
            f.write("plot '" + p + "' using 0:3  with lines title 'd/dmax', '" + p + "' using 0:4  with lines title ' u' \n\n") 
            
        f.write("unset multiplot\n")
        f.write("reset\n")
        f.write("set terminal png size 900,1000 enhanced\n")
        f.write("set output './quick_plots/sampling2.png'\n")
        f.write("set multiplot layout 3,1 rowsfirst\n")
        for i in range(0, len(names)):
            p = "./quick_plots/" + names[i] + ".out"
            f.write("set title 'sampling" + names[i] + " ' \n")
            f.write("set xlabel 'n'\n")
            f.write("set ylabel 'pick'\n")
            f.write("set yrange [-2:2]\n")
            f.write("set xrange [0:200]\n")
            f.write("plot '" + p + "' using 0:5  with lines title ''  \n\n") 

    
    
    f.close()
    os.system("gnuplot pots_dens_plt.gnuplot 2>>piped_output.txt")
    #os.system("rm pots_dens_plt.gnuplot")
    
    
# # # # # # # # # # # # # # # # # # # # # #
def stabity_test():
    args = [0.0001, 0.9862, 0.2, 0.5, 24, .5]
    #args = [0.0001, 0.9862, 0.2, 0.2, 24, .2]
    sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
    ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
    N               = 1
    M               = 0
    
    b_t = str(args[1])
    r_l = str(args[2])
    r_r = str(args[3])
    m_l = str(args[4])
    m_r = str(args[5])
    
    
    ver = ''
    lua_file = "mixeddwarf.lua"
    
    nfw  = 'output_nfw_nfw_0gy'
    plum = 'output_plummer_plummer_0gy'
    hern = 'output_hern_hern_0gy'
    plum_nfw = 'output_plummer_nfw_0gy'

    fn = nfw
    #args = [sim_time[0], 0.9862, 0.8, 0.5, 24, .5]
    #nbody(args, lua_file, fn, fn, ver, False)
    
    for i in range(M, N):
        args[0] = sim_time[i]
        nfw  = 'output_nfw_nfw_' + ext[i] + 'gy'
        plum = 'output_plummer_plummer_' + ext[i] + 'gy'
        hern = 'output_hern_hern_' + ext[i] + 'gy'
        plum_nfw = 'output_plummer_nfw_' + ext[i] + 'gy'
        fn = nfw
        nbody(args, lua_file, fn, fn, ver, False)
    
    
    os.chdir("data_testing")    
    os.system("./stability_test.py " + b_t + " " + r_l + " " + r_r + " " + m_l + " " + m_r)
# # # # # # # # # # # # # # # # # # # # # #
def clean():
    os.system("rm boinc_*")
# # # # # # # # # # # # # # # # # # # # # #    

def quick_calculator():
    
    ans = (73.8 /1000.0) * 3.154 / 3.086
    ans = 3.0 * ans * ans / (8.0 * mt.pi)
    
    print ans
    
    ans = 200.0 * ans * 4 * mt.pi / 3
    
    print ans 
# # # # # # # # # # # # # # # # # # # # # #    
def main():
    standard_run()
    
    if(test_mixed_dwarf_switch):
        test_mixed_dwarf()
        
    if(charles):
        for_charles()
    
    if(make_some_hists_switch):
        make_some_hists()
    
    if(stabity_test_switch):
        stabity_test()
    
    if(velocity_disp_switch):
        velocity_dispersion()
    
    if(lb_plot_switch):
        lb_plot(output)
        
    if(hstalt_binswap_switch):
        hstalt_binswap()
        
    if(plot_all_hists_switch):
        plot_all_hists()
    
    if(plot_n_ofhist_switch):
        plot_n_ofhist()
    
    if(orbit_location_switch):
        orbit_location()
        
    if(check_hist_likes_switch):
        check_hist_likes()
    clean()
    
    if(check_timestep_switch):
        check_timestep()
        
    if(pots_dens_plot_switch):
        pots_dens_plot();
    
    if(quick_calculator_switch):
        quick_calculator()
    
main()
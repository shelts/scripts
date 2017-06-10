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
from mpl_toolkits.mplot3d import Axes3D
import math as mt
import matplotlib.patches as mpatches
import random
random.seed(a = 12345678)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
#args_run_comp = [3.764300006400000, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run_comp = [4.037308903030000, 0.98, 0.2, 0.2, 12, 0.2]
args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 
args_run_comp = [3.95, 0.98, 0.2, 0.5, 12, 0.5] 
#args_run_comp = [2.08, 0.98, 0.2, 0.3, 12, 0.45] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#              Standard Run switches          #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = n                 #
match_histograms          = y                 #
run_and_compare           = n                 #
run_from_checkpoint       = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
#              Hist Plot Switches             #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_hists                = n                 #
plot_veldisp_switch       = n                 #
vlos_plot_switch          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
#              Non-Hist Plot Switches         #
# # # # # # # # # # # # # # # # # # # # # # # #
lb_plot_switch            = n                 #
lambda_beta_plot_switch   = n                 #

plot_adjacent             = y                 #
plot_overlapping          = y                 #
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#              possible tests                 #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_disp_switch      = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_some_hists_switch    = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
stabity_test_switch       = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
test_vel_theta_binning_switch = n
ridge_probe_switch        = n
plot_all_hists_switch     = n                 #
check_timestep_switch     = n                 #
quick_calculator_switch   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Circuitry           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Histogram names      #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'

#    histograms for runs  #
correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_postchange'
run_test = 'run_test_postchange'

#correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_postchange'
#run_test = 'run_test_postchange'

#    hist to match against for compare after run  #
correct_hist = correct

#    hist name for the nbody run   #
histogram_for_nbody_run = correct
histogram_for_nbody_run_and_compare = run_test

#    if you are just matching, these are the two hists #
match_hist_correct = histogram_for_nbody_run
match_hist_compare = histogram_for_nbody_run_and_compare
plot_name = histogram_for_nbody_run

match_hist_correct = histogram_for_nbody_run
match_hist_compare = histogram_for_nbody_run_and_compare

output = histogram_for_nbody_run
output_run_compare = histogram_for_nbody_run_and_compare
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#    run specfics   #
#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
lua = "full_control.lua"
#lua = "EMD_v164.lua"

#    pathways  #
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
    if(remake):
        make_nbody()
        
    if(run_nbody):
        nbody(args_run, lua, histogram_for_nbody_run, histogram_for_nbody_run, version, False)
    
    if(run_and_compare):
        compare_after_run(args_run_comp, lua, correct_hist, histogram_for_nbody_run_and_compare, output_run_compare, version)
    
    if(match_histograms):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(plot_hists):
        plot(match_hist_correct , match_hist_compare, plot_name, '1', '2')
        
    if(plot_veldisp_switch):
        plot_veldisp(match_hist_correct , match_hist_compare, plot_name + "_velDisp", '1', '2')
    
    
    if(vlos_plot_switch):
        vlos_plot(match_hist_correct, match_hist_compare)
        
    return 0
# #        
def make_nbody():
        os.chdir("./")
        #-DCMAKE_C_COMPILER=/usr/bin/cc 
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")

# #    
def nbody(paras, lua_file, hist, out, ver, should_pipe):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    
    if(not run_from_checkpoint and should_pipe == False):
        print('running nbody1 ')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -u -b -P  -i --no-clean-checkpoint " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
    if(run_from_checkpoint and should_pipe == False):
        print('running nbody from checkpoint')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b  -P --no-clean-checkpoint --checkpoint=nbody_checkpoint_correct_parameter_sweep " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
    
    if(should_pipe == True):
        print('running nbody')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 12 -b -P  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " \
         2>> " + out + "_piped.out")
     
     
     
    #os.chdir("../")
    os.chdir(path)
# #     
def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
          + " -S " + path + "quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0
# # 
def match_hists_pipe(hist1, hist2, ver, pipe_name):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "" + hist1 + '.hist'
          + " -S " + path + "" + hist2 + '.hist' + " 2>>" + pipe_name], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0
# # 
def compare_after_run(paras, lua_file, correct, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    if(not run_from_checkpoint):
        print('running nbody 2')
        os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -h " + path + "quick_plots/hists/" + correct + ".hist \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b -P -i --no-clean-checkpoint " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
    
    if(run_from_checkpoint):#this is the version that will run from a checkpoint
        print 'running from checkpoint'
        os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -h " + path + "quick_plots/hists/" + correct + ".hist \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b -P --no-clean-checkpoint --checkpoint=nbody_checkpoint_parameter_sweep_ft_4p03730890303 " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
# # 
# # # # # # # # # # # # # # # # # # # # # #
#        histogram plot                   #
# # # # # # # # # # # # # # # # # # # # # #
# # 
def plot(hist1, hist2, name, label1, label2):
    ylimit = 1.0
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    #folder = 'like_surface/'
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
        plt.xlabel('Lambda')
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
        plt.xlabel('Lambda')

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
# # 
def plot_veldisp(hist1, hist2, name, label1, label2):
    ylimit = 100
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    #folder = 'like_surface/'
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
    velD1 = []
    #Ncount1 = []
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
                velD1.append(float(ss[5]))
                #Ncount1.append(float(ss[4]))


    read_data = False
    lbins2 = []
    velD2 = []
    #Ncount2 = []
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
                velD2.append(float(ss[5]))
                #Ncount2.append(float(ss[4]))
            
    if(plot_overlapping):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(lbins1, velD1, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, velD2, width = w_overlap, color='r', alpha=0.75, label= label2)
        #plt.bar(lbins2, Ncount1, width = w_overlap, color='black', alpha=0.75, label= label2)
        #plt.bar(lbins2, Ncount2, width = w_overlap, color='b', alpha=0.75, label= label2)
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        plt.clf()
        #plt.show()
        
    if(plot_adjacent):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(lbins1, velD1, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.xlabel('Lambda')

        plt.subplot(212)
        plt.bar(lbins2, velD2, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('vel disp')
        plt.xlabel('Lambda')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        plt.clf()
        #plt.show()
        return 1
# # 
# # # # # # # # # # # # # # # # # # # # # #
#        NON-histogram plot               #
# # # # # # # # # # # # # # # # # # # # # #
# #
def convert_to_Lambda_Beta(x1, x2, x3, cartesian):
    phi   = mt.radians(128.79)
    theta = mt.radians(54.39)
    psi   = mt.radians(90.70)
    
    if(cartesian):
        x_coor = x1
        y_coor = x2
        z_coor = x3
        x_coor += 8.0 #convert to solar centric
    else:
        l = mt.radians(x1)
        b = mt.radians(x2)
        r = x3
        
        x_coor = r * mt.cos(l) * mt.cos(b) #this is solar centered x
        y_coor = r * mt.sin(l) * mt.cos(b)
        z_coor = r * mt.sin(b)
    
    #A = MB
    B = [x_coor, y_coor, z_coor]
    M_row1 = [mt.cos(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.sin(psi),
               mt.cos(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.sin(psi),
               mt.sin(psi) * mt.sin(theta)]
    
    M_row2 = [-mt.sin(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.cos(psi),
               -mt.sin(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.cos(psi),
               mt.cos(psi) * mt.sin(theta)]
    
    M_row3 = [mt.sin(theta) * mt.sin(phi), 
               -mt.sin(theta) * mt.cos(phi),
               mt.cos(theta)]
    
    A1 = M_row1[0] * B[0] + M_row1[1] * B[1] + M_row1[2] * B[2]
    A2 = M_row2[0] * B[0] + M_row2[1] * B[1] + M_row2[2] * B[2]
    A3 = M_row3[0] * B[0] + M_row3[1] * B[1] + M_row3[2] * B[2]
    
    beta = mt.asin(-A3 / mt.sqrt(A1 * A1 + A2 * A2 + A3 * A3))
    lamb = mt.atan2(A2, A1)
    
    beta = mt.degrees(beta)
    lamb = mt.degrees(lamb)
    
    return lamb, beta

def binner_vlos(lcoors, bcoors, rcoors, vloss, angle_cuttoffs):
    lambda_coors = []
    beta_coors   = []
    
    bin_size = abs(angle_cuttoffs[0] - angle_cuttoffs[1]) / angle_cuttoffs[2]
    mid_bins = []
    which_bin = []
    which_lambda = []
    which_vlos = []
    which_beta = []
    #setting up the mid bin coordinates
    for i in range(0, angle_cuttoffs[2]):
        mid_bin = angle_cuttoffs[0] + i * bin_size + bin_size / 2.0
        mid_bins.append(mid_bin)
        
    #transform to lambda beta coordinates from lbr
    for i in range(0, len(lcoors)):
        lambda_tmp, beta_tmp = convert_to_Lambda_Beta(lcoors[i], bcoors[i], rcoors[i], False)
        lambda_coors.append(lambda_tmp)
        beta_coors.append(beta_tmp)
        

    for i in range(0, len(lambda_coors)):#go through the different lambda coordinates
        if(beta_coors[i] >= angle_cuttoffs[3] and beta_coors[i] <= angle_cuttoffs[4]):#if it is between the beta cuttoffs
            for j in range(0, len(mid_bins)):#go through the bin coordinates
                left_edge  = mid_bins[j] - bin_size / 2.0 #edges of the bin
                right_edge = mid_bins[j] + bin_size / 2.0 #edges of the bin
                
                if(lambda_coors[i] >= left_edge and lambda_coors[i] <= right_edge):#check if the lambda coor falls in the bin
                    which_bin.append(mid_bins[j])#which mid bin it should be 
                    which_lambda.append(lambda_coors[i])#the coordinate that was put there
                    which_vlos.append(vloss[i])#the line of sight vel
                    which_beta.append(beta_coors[i])
                    break 
                
    
    #for i in range(0, len(which_bin)):
        #if(which_bin[i] == 15.0):
            #print which_bin[i], which_vlos[i], which_lambda[i], which_beta[i]
    return which_bin, which_vlos

def vlos_plot(file1, file2):
    ylimit = 100
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    
    print "plot histogram 1: ", file1
    print "plot histogram 2: ", file2
    
    plot_hist1 = file1 + ".hist"
    plot_hist2 = file2 + ".hist"
    
    label1 = '1'
    label2 = '2'
    
    name = 'vlos_plots'
    print("plotting histograms\n")
    
    #this is the reading of the of the counts, raw counts, vel disp from hist 1
    read_data = False
    lbins1 = []
    velD1 = []
    Ncount1 = []
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
                Ncount1.append(float(ss[4]))
                velD1.append(float(ss[5]))



    #this is the reading of the of the counts, raw counts, vel disp from hist 2
    read_data = False
    lbins2 = []
    velD2 = []
    Ncount2 = []
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
                Ncount2.append(float(ss[4]))
                velD2.append(float(ss[5]))
     
     
    #reading the vLOS and lbr from the output files. 
    angle_cuttoffs = [-150.0, 150.0, 50, -15.0, 15.0, 1]
    folder = 'quick_plots/outputs/'
    output1 = file1 + ".out"
    output2 = file2 + ".out"
    read_data = False
    lcoors = []
    bcoors = []
    rcoors = []
    vloss  = []
    lines = open(folder + output1, 'r')
    for line in lines:
        if (line.startswith("# ignore")):
            read_data = True
            continue
        if(read_data):
            ss = line.split(',')
            if(line.startswith("\n")):
                continue
            elif(float(ss[0]) == 0):
                lcoors.append(float(ss[4]))
                bcoors.append(float(ss[5]))
                rcoors.append(float(ss[6]))
                vloss.append(float(ss[11]))     
     
    which_bin1 = []
    which_vlos1 = []
    which_bin1, which_vlos1 = binner_vlos(lcoors, bcoors, rcoors, vloss, angle_cuttoffs)

    read_data = False
    lcoors = []
    bcoors = []
    rcoors = []
    vloss  = []
    lines = open(folder + output2, 'r')
    for line in lines:
        if (line.startswith("# ignore")):
            read_data = True
            continue
        if(read_data):
            ss = line.split(',')
            if(line.startswith("\n")):
                continue
            elif(float(ss[0]) == 0):
                lcoors.append(float(ss[4]))
                bcoors.append(float(ss[5]))
                rcoors.append(float(ss[6]))
                vloss.append(float(ss[11]))     
     
    which_bin2 = []
    which_vlos2 = []
    vel_disps2 = []
    which_bin2, which_vlos2 = binner_vlos(lcoors, bcoors, rcoors, vloss, angle_cuttoffs)
    
    vel_disps1 = []
    vel_disps2 = []
    #vel_disps1 = calc_vel_disps(which_bin1, which_vlos1)
    #vel_disps2 = calc_vel_disps(which_bin2, which_vlos2)
    
    
    if(plot_adjacent):
        count_y_limit = 0.4
        rawcount_y_limit = 2000
        vel_disp_ylimit = 100
        
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        #plt.subplots(4, sharex = True, sharey = True)
        ax1 = plt.subplot(421)
        plt.bar(lbins1, counts1, width = w_adjacent, color='b')
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.ylabel('counts')

        ax2 = plt.subplot(422)
        plt.bar(lbins2, counts2, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.yticks([])

        ax5 = plt.subplot(423)
        plt.bar(lbins1, Ncount1, width = w_adjacent, color='b')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.ylabel('raw count')
        #plt.xlabel('Lambda')

        ax6 = plt.subplot(424)
        plt.bar(lbins2, Ncount2, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.yticks([])
        #plt.xlabel('Lambda')
        
        ax3 = plt.subplot(425)
        #plt.subplots(2, sharex = True, sharey = False)
        plt.bar(lbins1, velD1, width = w_adjacent, color='b')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')

        ax4 = plt.subplot(426)
        plt.bar(lbins2, velD2, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.yticks([])
        
        ax3 = plt.subplot(427)
        #plt.subplots(2, sharex = True, sharey = False)
        plt.scatter(which_bin1, which_vlos1, color='b', s=.5, marker= 'o')
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')

        ax4 = plt.subplot(428)
        plt.scatter(which_bin2, which_vlos2, color='k', s=.5, marker= 'o', )
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.yticks([])
        plt.savefig(save_folder_adj + name + '.png', format='png', dpi=1000)
        
        
    if(plot_overlapping):
        count_y_limit = 0.4
        rawcount_y_limit = 2000
        vel_disp_ylimit = 100
        
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)

        ax1 = plt.subplot(411)
        plt.bar(lbins1, counts1, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, counts2, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.ylabel('counts')
        plt.legend()
        
        ax3 = plt.subplot(412)
        plt.bar(lbins1, Ncount1, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, Ncount2, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.ylabel('raw count')
        plt.xlabel('Lambda')
        plt.legend()
        
        ax2 = plt.subplot(413)
        plt.bar(lbins1, velD1, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(lbins2, velD2, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        
        ax2 = plt.subplot(414)
        plt.scatter(which_bin1, which_vlos1, s=1, marker= '.',  color='red', alpha=1,label= label1, edgecolors='none')
        plt.scatter(which_bin2, which_vlos2, s=1, marker= '.', color='blue', alpha=1, label= label2, edgecolors='none')
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png', dpi=1000)
        #plt.clf()
        #plt.show()
        
        
        
        
        return 1
 
def lambda_beta_plot(file_name):
    path_charles = 'quick_plots/outputs/'
    path = 'quick_plots/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = n
    plot_dm_alone = n
    
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
    light_l , light_b , light_r = ([] for i in range(3))
    dark_l , dark_b , dark_r = ([] for i in range(3))

    for line in lines:
        if(line.startswith("</bodies>")):
            break
        tokens = line.split(', ')
        isDark = int(tokens[0])
        l = float(tokens[4])
        #if(l > 180.0):
            #l = l - 360.0
        b = float(tokens[5])
        r = float(tokens[6])
        if(isDark == 0):
            light_l.append(l)
            light_b.append(b)
            light_r.append(r)
        if(isDark == 1):
            dark_l.append(l)
            dark_b.append(b)
            dark_r.append(r)
    

    #converting to lambda beta
    for i in range(0, len(light_l)):
        light_l[i], light_b[i] = convert_to_Lambda_Beta(light_l[i], light_b[i], light_r[i], False)
        dark_l[i], dark_b[i]   = convert_to_Lambda_Beta(dark_l[i],  dark_b[i],  dark_r[i],  False)

    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr):
        plt.figure(figsize=(20, 20))
        xlower = -360.0
        xupper = 360.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel('lambda')
        plt.ylabel('beta')
        plt.title('lambda vs beta')
        #default to just plot lm
        plt.plot(light_l, light_b, '.', markersize = 1.75, color = 'b', alpha=1.0, marker = '.')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta', format='png')
        print "plotting:", len(light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('lambda')
            plt.ylabel('beta')
            plt.title('lambda vs beta')
            plt.plot(dark_l, dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta', format='png')
            print "plotting:", len(light_l) + len(dark_l), " points"
        # # # # # # # # # #
        if(plot_dm_alone):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('lambda')
            plt.ylabel('beta')
            plt.title('lambda vs beta')
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lambdabeta_dark', format='png')
            
    return 0 
 
def lb_plot(file_name):
    path_charles = 'quick_plots/outputs/'
    path = 'quick_plots/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = y
    plot_dm = n
    plot_xyz = n
    plot_orbit = n
    
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
    if(plot_lbr):
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
        plt.plot(light_l, light_b, '.', markersize = 1.75, color = 'b', alpha=1.0, marker = '.')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
        print "plotting:", len(light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
            print "plotting:", len(light_l) + len(dark_l), " points"
        # # # # # # # # # #
        if(plot_orbit):
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
        if(plot_dm):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_dark', format='png')
            
    if(plot_xyz):
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
# #
# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
# #
def velocity_dispersion():
    args = [3.95, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = 'nbody1'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    nbody(args, l, file_name, file_name, version, False)
    #lb_plot(file_name)
    os.system("./scripts/velocity_dispersion.py " + file_name)
# # 
# # # # # # # # # # # # # # # # # # # # # #
#               MISC                      #
# # # # # # # # # # # # # # # # # # # # # #
# #
def test_vel_theta_binning():
    pathway = './data_testing/sim_outputs/'
    file_name = pathway + 'output_plummer_plummer_0gy.out'
    vxs = []
    vys = []
    vzs = []
    ms = []
    g = open(file_name, 'r')
    num = 1
    for line in g:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    g.close()
    
    line_n = 0
    lines = open(file_name, 'r')
    print num
    for line in lines:
        if(line_n < num):
            line_n += 1
            continue
        
        tt = line.split(', ')
        ty = float(tt[0])
        vx = float(tt[7])
        vy = float(tt[8])
        vz = float(tt[9])
        m  = float(tt[10])
        vxs.append(vx)
        vys.append(vy)
        vzs.append(vz)
        ms.append(m)
        
    lines.close()
    N = len(vxs)
    
    
    
    #cm correction
    cmx = 0.
    cmy = 0.
    cmz = 0.
    mtot = 0
    for i in range(0,N):
        cmx += ms[i] * vxs[i]
        cmy += ms[i] * vys[i]
        cmz += ms[i] * vzs[i]
        mtot += ms[i]
    cmx = cmx / mtot
    cmy = cmy / mtot
    cmz = cmz / mtot
    
    for i in range(0, N):
        vxs[i] -= cmx
        vys[i] -= cmy
        vzs[i] -= cmz
    
    thetas = []
    vs = []
    for i in range(0,len(vxs)):
        v = mt.sqrt( vxs[i] * vxs[i] + vys[i] * vys[i] + vzs[i] * vzs[i])
        theta = mt.acos( vzs[i] / v)
        thetas.append(theta)
        vs.append(v)
        
    print vs
    
    
    #binning
    binN = 1000
    binwidth = 0.1
    upper = binN * binwidth
    
    bins = []
    bin_ranges = []
    for k in range(0, binN):
        bins.append(0)
        bin_ranges.append(0)
        
        
    tmp = thetas
    #print tmp
    for i in range(0, N):
        bin_range = 0
        
        for j in range(0, binN):
            if( (bin_range + binwidth) < upper):
                if(tmp[i] >= bin_range and tmp[i] < (bin_range + binwidth)):
                    bins[j] += 1
                    break
                bin_range += binwidth
            elif( ( bin_range + binwidth) == upper):
                if( tmp[i] >= bin_range and tmp[i] <= (bin_range + binwidth)):
                    bins[j] += 1
                    break
                bin_range += binwidth

        
    bin_range = 0
    for k in range(0, binN):
        bin_ranges[k] = bin_range
        bin_range += binwidth
    #print bins

    plt.bar(bin_ranges, bins, width = .05 , color = 'r', edgecolor = 'k')
    plt.xlim(-3, 5)
    plt.show()
# #
def ridge_probe():
    rl = 0.2
    ml = 12
    rr_range = [0.1, 0.5]
    mr_range = [0.01, 0.95]
    
    rr = 0.2
    mr = 0.2
    
    rscale_t = rl / (rr)
    rd = rscale_t * (1.0 - rr)
    
    dwarfmass = ml / mr
    md = dwarfmass * (1.0 - mr)
    
    f = open("ridge_data.txt", 'w')
    print rd, md
    
    rr = rr_range[0]
    mr = mr_range[0]
    ratios = []
    density1s = []
    density2s = []
    
    rrs = []
    mrs = []
    while(1):
        mr = mr_range[0]
        while(1):
            rscale_t = rl / (rr)
            rd = rscale_t * (1.0 - rr)
        
            dwarfmass = ml / mr
            md = dwarfmass * (1.0 - mr)
            
            ratio = md / rd
            density1 = md / (4.0 * mt.pi * rd**3)
            density2 = rd**2 * density1
            
            rrs.append(rr)
            mrs.append(mr)
            ratios.append(ratio)
            density1s.append(density1)
            density2s.append(density2)
            
            f.write("%0.15f\t %0.15f\t%0.15f\t%0.15f\t%0.15f\n" % (rr, mr, ratio, density1, density2))
            
            
            if(mr > mr_range[1]):
                break
            else:
                mr += 0.01
                
        if(rr > rr_range[1]):
            break
        else:
            rr += 0.001
    f.close()
    
    gnu_args = ['reset',
                'set terminal wxt persist',
                'set key off',
                "set xlabel 'rrs' ",
                "set ylabel 'mrs' ",
                "set zlabel 'ratio' ",
                "set xrange[0.1: 0.5]",
                "set yrange[0.01:0.95]",
                "set zrange[0:100]"]
                
                
    g = open("ridge_probe.gnu", 'w')
    for i in range(0, len(gnu_args)):
        g.writelines(gnu_args[i] + "\n")
    g.write("splot 'ridge_data.txt' using 1:2:4 with points palette pointtype 5 ps 0.5\n")
    g.close()
    os.system("gnuplot ridge_probe.gnu 2>>piped_output.txt")
    
    return 0
# #
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
# # 
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
# # 
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
# #
def check_timestep():
    rl = [0.05, 0.5]
    rr = [0.1, 0.5]
    ml = [1, 50]
    mr = [0.01, 0.95]
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
# # 
def stabity_test():
    args = [0.0001, 0.9862, 0.2, 0.5, 24, .5]
    #args = [0.0001, 0.9862, 0.2, 0.2, 24, .2]
    sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
    ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
    N               = 1
    M               = 0
    
    make_nbody()
    
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
# # 
def clean():
    os.system("rm boinc_*")
# #      
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Generator           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
def main():
    standard_run()
    
    if(test_vel_theta_binning_switch):
        test_vel_theta_binning()
        
    if(make_some_hists_switch):
        make_some_hists()
    
    if(stabity_test_switch):
        stabity_test()
    
    if(velocity_disp_switch):
        velocity_dispersion()
    
    if(lb_plot_switch):
        lb_plot(output)
    
    if(lambda_beta_plot_switch):
        lambda_beta_plot(output)
        
        
    if(plot_all_hists_switch):
        plot_all_hists()
    
    if(ridge_probe_switch):
        ridge_probe()
    
    
    if(check_timestep_switch):
        check_timestep()
        
    if(quick_calculator_switch):
        quick_calculator()
        
# spark plug #
main()

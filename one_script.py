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
from nbody_functional import *
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
#args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run = [3.95, 0.98, 0.2, 0.2, 12, 1.43] 
args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
args_run_comp = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run_comp = [3.28828657813, 0.98, 0.2, 0.2, 12, 0.2]

#args_run_comp = [2.08, 0.98, 0.2, 0.3, 12, 0.45] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#              Standard Run switches          #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = y                 #
match_histograms          = n                 #
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
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Circuitry           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Histogram names      #
histogram_v166 = 'hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17'

#    histograms for runs  #
#correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_mw'
correct1 = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_diff_seed'

#    hist to match against for compare after run  #
correct_hist = 'test'
compare_hist = 'test2'

#    hist name for the nbody run   #
correctans_hist = correct_hist
comparison_hist = compare_hist

plot_name = compare_hist



#    run specfics   #
#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
lua = "full_control.lua"
#lua = "manual_body_input.lua"
#lua = "halo_object_dev.lua"
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
    nbody = nbody_running_env(lua, version, path)
    
    if(remake):
        nbody.build(False)#true for complete rebuild
        
    if(run_nbody):
        nbody.run(args_run, correctans_hist)
    
    if(run_and_compare):
        nbody.run(args_run_comp, correctans_hist, comparison_hist)
    
    if(match_histograms):
        nbody.match_hists(correctans_hist, comparison_hist)
        
    if(plot_hists):
        plot(correctans_hist , comparison_hist, plot_name, '1', '2')
        
    if(plot_veldisp_switch):
        plot_veldisp(correctans_hist , comparison_hist, plot_name + "_velDisp", '1', '2')
    
    
    if(vlos_plot_switch):
        vlos_plot(correctans_hist, comparison_hist)
        vlos_plot_single(correctans_hist)
        
    return 0
# #        



# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
# #

# # # # # # # # # # # # # # # # # # # # # #
#               MISC                      #
# # # # # # # # # # # # # # # # # # # # # #
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
    
    
    if(lb_plot_switch):
        lb_plot(output)
    
    if(lambda_beta_plot_switch):
        lambda_beta_plot(output)
        
        
    if(half_mass_radius_switch):
        half_mass_radius()
        
        
    if(chi_sq_dist_plot_switch):
        chi_sq_dist_plot()
# spark plug #
main()

#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import sys
from subprocess import call
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib import cm
import math
args = sys.argv;
#This script plots two histograms next to each other and also produces their matching likelihood
#-It also plots their distribution heat maps 
#######################################################################
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
y = True
n = False

hist_from_MW = 'tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_10_20_15.hist'
hist_from_MW_new = 'tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16.hist'

hist_20k_seed1 = 'data_1d.hist'
hist_20k_seed2 = 'data_2d.hist'

best_fit = 'best_fit_parameter_hist.hist'


hist1 = hist_from_MW
hist2 = hist_from_MW_new

#    SWITCHES  #
plot_nbody_hist      = y
plot_distruption_map = n

if(len(sys.argv) == 3):
    hist1 = str(args[1])
    hist2 = str(args[2])
print "plot histogram 1: ", hist1
print "plot histogram 2: ", hist2
    


#    Histogram names     #
plot_hist1 = hist1
plot_hist2 = hist2

disruption_hist1 = hist1
disruption_hist2 = hist2

match_hist_correct = hist1
match_hist_compare = hist2


ylimit = 0.4
xlower = 50
xupper = -75
w = 1.5
#the current working directory is in the folder of the script that calls this
folder = 'quick_plots/hists'
name = 'comparison_hists'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
if(plot_nbody_hist == True):
    print("plotting histograms\n")
    lines = []
    lines = open(folder + '/' + plot_hist1).readlines();
    lines = lines[40:len(lines)]
    sim_l = []
    sim_n = []
    for line in lines:
        tokens = line.split();
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            cts = float(tokens[3])
            sim_l.append(lda)
            sim_n.append(cts)

    lines = []
    lines = open(folder + '/' + plot_hist2).readlines();
    lines = lines[40:len(lines)]
    data_l = []
    data_n = []
    for line in lines:
        tokens = line.split()
        if tokens:
            dat_l = float(tokens[1])
            dat_n = float(tokens[3])
            data_l.append(dat_l)
            data_n.append(dat_n)
    
    
    #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
    plt.subplot(211)
    plt.bar(sim_l, sim_n, width = w, color='b')
    plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
    plt.title('Histogram of Light Matter Distribution After 4 Gy')
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit))
    plt.ylabel('counts')
    
    plt.subplot(212)
    plt.bar(data_l, data_n, width = w, color='k')
    plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit))
    plt.xlabel('l')
    plt.ylabel('counts')
    #f.subplots_adjust(hspace=0)
    plt.savefig('quick_plots/' + name + '.png', format='png')
    #plt.show()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_distruption_map == True):
    print("plotting distruption map")
    f = open('~/Desktop/research/quick_plots/histogram_distrupt.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'beta'\n")
    f.write("set xlabel 'lambda'\n")
    f.write("set xrange[180:-180]\n")
    f.write("set yrange[-20:20]\n\n\n")
    f.write("set pm3d map\n")
    f.write("set output \"~/Desktop/research/quick_plots/distruption1.png\" \n")
    f.write("set title 'Histogram of Light Matter Distribution After 4 Gy' \n")
    f.write("plot '~/Desktop/research/" + folder + "/" + disruption_hist1 + "' using 2:3:4 with image \n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")
    f.write("set output \"~/Desktop/research/quick_plots/distruption2.png\" \n")
    f.write("set title 'Histogram of Light Matter Distribution After 4 Gy' \n")
    f.write("plot '~/Desktop/research/" + folder + "/" + disruption_hist2 + "' using 2:3:4 with image \n\n")
    
    f.close()
    
    os.system("gnuplot ~/Desktop/research/quick_plots/histogram_distrupt.gnuplot")
    os.system("rm ~/Desktop/research/quick_plots/histogram_distrupt.gnuplot")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
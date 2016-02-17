#! /usr/bin/python
import os
import sys
from subprocess import call
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib import cm
import math

args = sys.argv;

def __main__(arg):
    #######################################################################
    #This script plots two histograms next to each other and also produces their matching likelihood
    #It also plots their distribution heat maps 
    #    LIBRARY   #
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
    match_histograms     = y
    
    if(len(sys.argv) == 3):
        hist1     = str(args[1])
        hist2     = str(args[2])
        match_histograms = n
    print "histogram 1: ", hist1
    print "histogram 2: ", hist2
        


    #    Histogram names     #
    plot_hist1 = hist1
    plot_hist2 = hist2

    disruption_hist1 = hist1
    disruption_hist2 = hist2

    match_hist_correct = hist1
    match_hist_compare = hist2

    folder = 'quick_plots/hists_outputs'

    #######################################################################
    if(match_histograms == True):
        os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -h ~/Desktop/research/" + folder + "/" + match_hist_correct + "\
        -s ~/Desktop/research/" + folder + "/" + match_hist_compare)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
    if(plot_nbody_hist == True):
        print("making histogram")
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
        plt.bar(sim_l, sim_n, width=1, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label='MW')])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((140, -140))
        plt.ylim((0.0, 0.25))
        plt.ylabel('counts')
        
        plt.subplot(212)
        plt.bar(data_l, data_n, width=1, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label='New')])
        plt.xlim((140, -140))
        plt.ylim((0.0, 0.25))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig('quick_plots/comparison_hists_mw_new', format='png')
        #plt.show()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
__main__(args);
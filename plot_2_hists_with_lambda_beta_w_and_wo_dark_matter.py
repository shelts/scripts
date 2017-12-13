#! /usr/bin/python
#/* Copyright (c) 2017 Siddhartha Shelton */
import os
import subprocess
from subprocess import call
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import math as mt
from nbody_functional import *





def plot_hist_lambda_beta(file1, file2, file_name = None):
    path = 'quick_plots/'
    hist = path + 'hists/'
    outs = path + 'outputs/'
    
    out1 = nbody_outputs(outs + file1 + ".out")
    out2 = nbody_outputs(outs + file2 + ".out")
    
    hist1 = nbody_histograms(hist + file1 + ".hist")
    hist2 = nbody_histograms(hist + file2 + ".hist")
    
    w_overlap = 2.5
    w_adjacent = 1.5
    count_y_limit = 0.4
    out1.dark_light_split()
    out1.convert_lambda_beta(True)
    
    out2.dark_light_split()
    out2.convert_lambda_beta(True)
    xlower = -180.0
    xupper = 180.0
    ylower = -80
    yupper = 80
    
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    f.subplots_adjust(hspace=0)
    f.subplots_adjust(wspace=0)
    plt.figure(figsize=(20, 10))
    ax1 = plt.subplot(221)
    plt.xlim((xlower, xupper))
    plt.ylim((ylower, yupper))
    plt.ylabel(r'$\beta$')
    plt.title(r'$\Lambda$ vs $\beta$')
    #default to just plot lm
    if(not file_name):
        plt.plot(out1.dark_lambda, out1.dark_beta, '.', markersize = .5, color = 'black', alpha=.75, marker = '.', label = 'dark matter')
    plt.plot(out1.light_lambda, out1.light_beta, '.', markersize = .75, color = 'b', alpha=1.0, marker = '.', label = 'baryons')
    plt.legend()
    #plt.subplots(4, sharex = True, sharey = True)
    
    
    ax2 = plt.subplot(222)
    plt.xlim((xlower, xupper))
    plt.ylim((ylower, yupper))
    plt.xlabel(r'$\Lambda$')
    #plt.ylabel(r'$\beta$')
    plt.title(r'$\Lambda$ vs $\beta$')
    if(not file_name):
        plt.plot(out2.dark_lambda, out2.dark_beta, '.', markersize = .5, color = 'black', alpha=.75, marker = '.', label = 'dark matter')
    plt.plot(out2.light_lambda, out2.light_beta, '.', markersize = .75, color = 'b', alpha=1.0, marker = '.',label = 'baryons')
    
    ax5 = plt.subplot(223)
    plt.bar(hist1.lbins, hist1.counts, width = w_adjacent, color='b')
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, count_y_limit))
    plt.xlabel(r'$\Lambda$')
    plt.ylabel('counts')
    
    #plt.legend()
    
    
    ax6 = plt.subplot(224)
    plt.bar(hist2.lbins, hist2.counts, width = w_adjacent, color='k')
    plt.xlim((xlower, xupper))
    plt.xlabel(r'$\Lambda$')
    plt.ylim((0.0, count_y_limit))
    plt.ylabel('counts')
    #plt.yticks([])
    
    #plt.show()
    if(not file_name):
        plt.savefig('/home/sidd/Desktop/research/quick_plots/lambda_beta_with_dark', format='png')
    else:
        plt.savefig('/home/sidd/Desktop/research/quick_plots/lambda_beta_without_dark', format='png')
            
    return 0 


def main():
    file1 = 'hist_v166_3p95_0p2_0p2_12_0p2__12_5_17'
    file2 = 'mw@h_best_fit'
    
    plot_hist_lambda_beta(file1, file2)
    
    plot_hist_lambda_beta(file1, file2, True)
    
    return 0 

main()



#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
import os
from mpl_toolkits.mplot3d import Axes3D
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from curve_fit import *

class bin_betas:#class to make histogram of betas in each bin
    def __init__(self, beta_coors_ON, beta_coors_OFF, lmda_bnd):#(on field beta coordinates, Off field beta coordinates, lambda bin parameters)
        self.binned_coors_ON  = []
        self.binned_coors_OFF = []
        
        # bin the on and off field seperately so you can adjust it until they have same number of bins #
        # these parameters should be kept the same. But the option is there.
        self.beta_Nbins_OFF = 30
        self.lower_OFF  = -5.0
        self.upper_OFF = 5.0
        
        self.beta_Nbins_ON = 30
        self.lower_ON = -5.0
        self.upper_ON = 5.0
        
        self.bin_width_ON    = abs(self.lower_ON - self.upper_ON) / self.beta_Nbins_ON
        self.bin_width_OFF   = abs(self.lower_OFF - self.upper_OFF) / self.beta_Nbins_OFF
        self.bin_centers_ON  = []
        self.bin_centers_OFF = []
        
        
        # initialize the beta bin centers ON field #
        center  = self.lower_ON + self.bin_width_ON / 2.0
        for i in range(0, self.beta_Nbins_ON): # initial beta bin centers On field
            self.bin_centers_ON.append(center)
            center += self.bin_width_ON
        
        # initialize the beta bin centers OFF field #
        center = self.lower_OFF + self.bin_width_OFF / 2.0
        for i in range(0, self.beta_Nbins_OFF): # initial beta bin centers off field
            self.bin_centers_OFF.append(center)
            center += self.bin_width_OFF
        
        # create array for storing beta count data #
        for i in range(0, lmda_bnd.Nbins):  
            self.binned_coors_ON.append([]) # empty vessel for each Lambda bin for the beta bins
            self.binned_coors_OFF.append([])
            
            # initialize the counts to zero in each bin ON field #
            for j in range(0, self.beta_Nbins_ON): # for each beta bins
                self.binned_coors_ON[i].append(0.0) # initialize the counts for the beta bins
            
            # initialize the counts to zero in each bin OFF field #
            for j in range(0, self.beta_Nbins_OFF):
                self.binned_coors_OFF[i].append(0.0)
                
            # send the beta coors for this lambda bin for binning #    
            self.binner(i, beta_coors_ON[i], beta_coors_OFF[i]) 

        # print (self.binned_coors_OFF)
        del beta_coors_ON, beta_coors_OFF # free up some space
        #self.plot_3d(lmda_bnd.Nbins, lmda_bnd.count_lda) # make one 3D plot of the stream
        
        self.off_field_average(lmda_bnd)# does a simple ave of the off field counts.
        #self.correction(lmda_bnd) # substract the simple ave from the off and on fields
        self.combine(lmda_bnd) # combin the two fields in one histogram to fit the data
        self.plot_each_bin(lmda_bnd.Nbins) # plot each lambda bin seperately
        
    def combine(self, lmda_bnd):
        self.binned_combined = []
        for i in range(0, lmda_bnd.Nbins):
            self.binned_combined.append([])
            for j in range(0, len(self.bin_centers_ON)):
                self.binned_combined[i].append(0)
                self.binned_combined[i][j] = (self.binned_coors_ON[i][j] + self.binned_coors_OFF[i][j])
        #print self.binned_combined
        return 0
    
    def binner(self, lmbda_bin, coors_ON, coors_OFF): # (current lambda bin, beta coors on field, beta coors off field)
        for j in range(0, len(coors_ON)): # for each beta coordinate in the lmda bin
            for k in range(0, self.beta_Nbins_ON): # for each beta bin
                lower_bound = (self.bin_centers_ON[k] - self.bin_width_ON / 2.0) # bin bounds
                upper_bound = (self.bin_centers_ON[k] + self.bin_width_ON / 2.0)
                
                if(coors_ON[j] >= lower_bound  and coors_ON[j] <= upper_bound): # check if beta coor is in the bin
                    self.binned_coors_ON[lmbda_bin][k] += 1.0
        
        for j in range(0, len(coors_OFF)): # for each beta coordinate in the lmda bin
            for k in range(0, self.beta_Nbins_OFF): # for each beta bin
                lower_bound = (self.bin_centers_OFF[k] - self.bin_width_OFF / 2.0)
                upper_bound = (self.bin_centers_OFF[k] + self.bin_width_OFF / 2.0)
                #print lower_bound, upper_bound
                if(coors_OFF[j] >= lower_bound  and coors_OFF[j] <= upper_bound):
                    self.binned_coors_OFF[lmbda_bin][k] += 1.0
    
    def plot_each_bin(self, lmda_Nbin):
        w = 0.25
        os.system("rm -r quick_plots/stream_beta_plots/lamb*")
        #test_dat = test_data()
        for i in range(0, lmda_Nbin):
            fit = diff_evo(self.bin_centers_ON , self.binned_combined[i] )
            fit_xs, fit_fs = fit.generate_plot_points()
            fit_paras = fit.pop.cur_pop[fit.best_index]
            print fit_paras
            plt.figure()
            plt.xlim(self.lower_OFF, self.upper_OFF)
            plt.ylim(0, 400)
            plt.ylabel("counts")
            plt.xlabel(r"$\beta_{Orphan}$")
            plt.plot(fit_xs,  fit_fs, color='m',linewidth = 2, alpha = 1., label = 'paras = ' + str(round(fit_paras[0], 2)) + ' ' + str(round(fit_paras[1], 2)) + ' ' + str(round(fit_paras[2], 2)) + ' ' + str(round(fit_paras[3], 2)) + ' ' + str(round(fit_paras[4], 2)) )
            plt.bar(self.bin_centers_OFF, self.binned_coors_OFF[i], width=w, color='r', alpha = 0.75, label = 'OFF')
            plt.bar(self.bin_centers_ON,  self.binned_coors_ON[i], width=w, color='b', alpha = 0.75, label = 'ON')
            #plt.scatter(test_dat.xs, test_dat.fs, s = 0.9, color = 'k')
            plt.legend()
            plt.savefig('quick_plots/stream_beta_plots/lambda_bin_' + str(i) + '.png', format = 'png')
            plt.close()
            #plt.clf()
        os.system("xdg-open quick_plots/stream_beta_plots/lambda_bin_0.png")
        return 0
    
    def plot_3d(self, lmda_Nbins,lmda_centers):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        w = 0.25
        ax.set_xlabel(r"$\beta_{Orphan}$")
        ax.set_zlabel("counts")
        ax.set_ylabel(r"$\Lambda_{Orphan}$")
        for i in range(0, lmda_Nbins):
            ax.bar(self.bin_centers_OFF, self.binned_coors_OFF[i], width=w,zs=lmda_centers[i], zdir='y', color='r', alpha = 0.75)
            ax.bar(self.bin_centers_ON, self.binned_coors_ON[i], width=w, zs=lmda_centers[i], zdir='y',  color='b', alpha = 0.5, )
        plt.savefig('quick_plots/stream_beta_plots/lambda_beta_bins.png', format = 'png')
        plt.show()
        
        return 0
    
    def off_field_average(self, lmda_bnd):
        self.bin_off_field_aves = []
        bins_with_counts = []
        for i in range(0, lmda_bnd.Nbins): # for each lambda bin
            off_field_ave = 0.0
            bns = 0.0
            for j in range(0, self.beta_Nbins_OFF): # for each of the beta bins
                if(self.binned_coors_OFF[i][j] > 0.0): # make sure ave includes only bins with counts
                    off_field_ave += self.binned_coors_OFF[i][j]
                    bns += 1.0
            bins_with_counts.append(bns)
            self.bin_off_field_aves.append(off_field_ave)
        
        #print bin_off_field_aves
        for i in range(0, lmda_bnd.Nbins):
            if(float(bins_with_counts[i]) > 0.0):
                self.bin_off_field_aves[i] = self.bin_off_field_aves[i] / float(bins_with_counts[i])
        return 0
    
    def correction(self, lmda_bnd):
        for i in range(0, lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins_ON):
                if(self.binned_coors_ON[i][j] > 0.0):
                    self.binned_coors_ON[i][j] -= self.bin_off_field_aves[i] * .75

        for i in range(0, lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins_OFF):
                if(self.binned_coors_OFF[i][j] > 0.0):
                    self.binned_coors_OFF[i][j] -= self.bin_off_field_aves[i] * .75
        return 0
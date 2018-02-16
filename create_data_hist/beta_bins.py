#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # #
#   This File Works For create_data_hist.py #
# # # # # # # # # # # # # # # # # # # # # # #
import os
from mpl_toolkits.mplot3d import Axes3D
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from differential_evolution import *

class bin_betas:#class to make histogram of betas in each bin
    def __init__(self, beta_coors_ON, beta_coors_OFF, lmda_bnd):#(on field beta coordinates, Off field beta coordinates, lambda bin parameters)
        self.binned_beta_ON  = []
        self.binned_beta_OFF = []
        self.lmda_bnd = lmda_bnd
        del lmda_bnd
        
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
        
        self.initialize_beta_bins(beta_coors_ON, beta_coors_OFF) # sets up the beta bins
        del beta_coors_ON, beta_coors_OFF # free up some space
        
        self.off_field_star_density()
        self.den_correction()
        #self.off_field_average()# does a simple ave of the off field counts.
        #self.correction() # substract the simple ave from the off and on fields
        self.combine() # combin the two fields in one histogram to fit the data
        
        #self.plot_3d() # make one 3D plot of the stream
        self.optimize()
        #self.plot_each_bin()
    def initialize_beta_bins(self, beta_coors_ON, beta_coors_OFF):
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
        for i in range(0, self.lmda_bnd.Nbins):  
            self.binned_beta_ON.append([]) # empty vessel for each Lambda bin for the beta bins
            self.binned_beta_OFF.append([])
            
            # initialize the counts to zero in each bin ON field #
            for j in range(0, self.beta_Nbins_ON): # for each beta bins
                self.binned_beta_ON[i].append(0.0) # initialize the counts for the beta bins
            
            # initialize the counts to zero in each bin OFF field #
            for j in range(0, self.beta_Nbins_OFF):
                self.binned_beta_OFF[i].append(0.0)
                
            # send the beta coors for this lambda bin for binning #    
            self.binner(i, beta_coors_ON[i], beta_coors_OFF[i]) 

    def combine(self):
        self.binned_combined = []
        for i in range(0, self.lmda_bnd.Nbins):
            self.binned_combined.append([])
            #print len(self.binned_beta_ON[i]), len(self.binned_beta_OFF[i])
            for j in range(0, len(self.bin_centers_ON)):
                self.binned_combined[i].append(0)
                self.binned_combined[i][j] = (self.binned_beta_ON[i][j] + self.binned_beta_OFF[i][j])
                #print i, self.binned_beta_ON[i][j], self.binned_beta_OFF[i][j], self.binned_combined[i][j]
        #print self.binned_combined
        return 0
    
    def binner(self, lmbda_bin, coors_ON, coors_OFF): # (current lambda bin, beta coors on field, beta coors off field)
        for j in range(0, len(coors_ON)): # for each beta coordinate in the lmda bin
            for k in range(0, self.beta_Nbins_ON): # for each beta bin
                lower_bound = (self.bin_centers_ON[k] - self.bin_width_ON / 2.0) # bin bounds
                upper_bound = (self.bin_centers_ON[k] + self.bin_width_ON / 2.0)
                
                if(coors_ON[j] >= lower_bound  and coors_ON[j] <= upper_bound): # check if beta coor is in the bin
                    self.binned_beta_ON[lmbda_bin][k] += 1.0
        
        for j in range(0, len(coors_OFF)): # for each beta coordinate in the lmda bin
            for k in range(0, self.beta_Nbins_OFF): # for each beta bin
                lower_bound = (self.bin_centers_OFF[k] - self.bin_width_OFF / 2.0)
                upper_bound = (self.bin_centers_OFF[k] + self.bin_width_OFF / 2.0)
                #print lower_bound, upper_bound
                if(coors_OFF[j] >= lower_bound  and coors_OFF[j] <= upper_bound):
                    self.binned_beta_OFF[lmbda_bin][k] += 1.0
    
    def optimize(self):
        iters = 40000
        os.system("rm -r stream_beta_plots/lamb*")
        for i in range(0, self.lmda_bnd.Nbins):
            self.fit = diff_evo(self.bin_centers_ON , self.binned_combined[i], iters )
            self.fit_paras = self.fit.pop.cur_pop[self.fit.best_index]
            print self.fit_paras
            self.plot_each_bin(i) # plot each lambda bin seperately
            os.system('xdg-open stream_beta_plots/lambda_bin_' + str(0) + '_' + str(self.lmda_bnd.bin_centers[0]) + '.png')
        
        
    def plot_each_bin(self, i = None):
        w = 0.25
        #test_dat = test_data()
        plt.figure()
        plt.xlim(self.lower_OFF, self.upper_OFF)
        plt.ylim(0, 400)
        plt.ylabel("counts")
        plt.xlabel(r"$\beta_{Orphan}$")
        
        # this is sloppy.
        if(i != None):
            fit_paras = self.fit_paras
            fit_xs, fit_fs = self.fit.generate_plot_points()
            plt.plot(fit_xs,  fit_fs, color='k',linewidth = 2, alpha = 1., label = 'paras = ' + str(round(fit_paras[0], 2)) + ' ' + str(round(fit_paras[1], 2)) + ' ' + str(round(fit_paras[2], 2)) + ' ' + str(round(fit_paras[3], 2)) + ' ' + str(round(fit_paras[4], 2)) )
            plt.bar(self.bin_centers_OFF, self.binned_combined[i], width=w, color='m', alpha = 1., label = 'C')
            plt.bar(self.bin_centers_OFF, self.binned_beta_OFF[i], width=w, color='r', alpha = 0.5, label = 'OFF')
            plt.bar(self.bin_centers_ON,  self.binned_beta_ON[i], width=w, color='b', alpha = 0.5, label = 'ON')
            plt.legend()
            plt.savefig('stream_beta_plots/lambda_bin_' + str(i) + '_' + str(self.lmda_bnd.bin_centers[i]) + '.png', format = 'png')
            plt.close()
        else:
            os.system("rm -r stream_beta_plots/lamb*")
            for i in range(0, self.lmda_bnd.Nbins):
                plt.figure()
                plt.xlim(self.lower_OFF, self.upper_OFF)
                plt.ylim(0, 400)
                plt.ylabel("counts")
                plt.xlabel(r"$\beta_{Orphan}$")
                plt.bar(self.bin_centers_OFF, self.binned_combined[i], width=w, color='m', alpha = 1., label = 'C')
                plt.bar(self.bin_centers_OFF, self.binned_beta_OFF[i], width=w, color='r', alpha = 0.5, label = 'OFF')
                plt.bar(self.bin_centers_ON,  self.binned_beta_ON[i], width=w, color='b', alpha = 0.5, label = 'ON')
                #plt.scatter(test_dat.xs, test_dat.fs, s = 0.9, color = 'k')
                plt.legend()
                plt.savefig('stream_beta_plots/lambda_bin_' + str(i) + '_' + str(self.lmda_bnd.bin_centers[i]) + '.png', format = 'png')
                plt.close()
                os.system('xdg-open stream_beta_plots/lambda_bin_' + str(0) + '_' + str(self.lmda_bnd.bin_centers[0]) + '.png')
        #plt.clf()
        
        return 0
    
    def plot_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        w = 0.25
        ax.set_xlabel(r"$\beta_{Orphan}$")
        ax.set_zlabel("counts")
        ax.set_ylabel(r"$\Lambda_{Orphan}$")
        for i in range(0, self.lmda_bnd.Nbins):
            ax.bar(self.bin_centers_OFF, self.binned_beta_OFF[i], width=w,zs=self.lmda_bnd.bin_centers[i], zdir='y', color='r', alpha = 0.75)
            ax.bar(self.bin_centers_ON, self.binned_beta_ON[i], width=w,  zs=self.lmda_bnd.bin_centers[i], zdir='y',  color='b', alpha = 0.5, )
        plt.savefig('stream_beta_plots/lambda_beta_bins.png', format = 'png')
        plt.show()
        
        return 0
    
    def off_field_average(self):
        self.bin_off_field_aves = []
        bins_with_counts = []
        for i in range(0, self.lmda_bnd.Nbins): # for each lambda bin
            off_field_ave = 0.0
            bns = 0.0
            for j in range(0, self.beta_Nbins_OFF): # for each of the beta bins
                if(self.binned_beta_OFF[i][j] > 0.0): # make sure ave includes only bins with counts
                    off_field_ave += self.binned_beta_OFF[i][j]
                    bns += 1.0
            bins_with_counts.append(bns)
            self.bin_off_field_aves.append(off_field_ave)
        
        for i in range(0, self.lmda_bnd.Nbins):
            if(float(bins_with_counts[i]) > 0.0):
                self.bin_off_field_aves[i] = self.bin_off_field_aves[i] / float(bins_with_counts[i])
        #print self.bin_off_field_aves
        return 0
    
    def correction(self):
        for i in range(0, self.lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins_ON):
                if(self.binned_beta_ON[i][j] > 0.0):
                    self.binned_beta_ON[i][j] -= self.bin_off_field_aves[i] * 1.
                    if(self.binned_beta_ON[i][j] < 0.0):
                        self.binned_beta_ON[i][j] = 0

        for i in range(0, self.lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins_OFF):
                if(self.binned_beta_OFF[i][j] > 0.0):
                    self.binned_beta_OFF[i][j] -= self.bin_off_field_aves[i] * 1.
                    if(self.binned_beta_OFF[i][j] < 0.0):
                        self.binned_beta_OFF[i][j] = 0
        return 0
    
    def den_correction(self):
        for i in range(0, self.lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins_ON):
                if(self.binned_beta_ON[i][j] > 0.0):
                    self.binned_beta_ON[i][j] -= self.star_density[i] * 1.
                    if(self.binned_beta_ON[i][j] < 0.0):
                        self.binned_beta_ON[i][j] = 0

        for i in range(0, self.lmda_bnd.Nbins):
            #print self.binned_beta_OFF[i]
            for j in range(0, self.beta_Nbins_OFF):
                if(self.binned_beta_OFF[i][j] > 0.0):
                    self.binned_beta_OFF[i][j] -= self.star_density[i] * 1.
                    if(self.binned_beta_OFF[i][j] < 0.0):
                        self.binned_beta_OFF[i][j] = 0
            #print self.binned_beta_OFF[i], '\n'
        return 0
    
    def off_field_star_density(self):
        self.star_density = []
        length = abs(self.lower_OFF - self.upper_OFF) # length of each beta bin
        for i in range(0, self.lmda_bnd.Nbins):
            width = abs(self.lmda_bnd.bin_uppers[i] - self.lmda_bnd.bin_lowers[i]) #width of each lambda bin
            area = width * length
            self.star_density.append(0)
            for j in range(0, self.beta_Nbins_OFF):
                if(self.binned_beta_OFF[i][j] > 0):
                    self.star_density[i] += self.binned_beta_OFF[i][j]
            self.star_density[i] = self.star_density[i] / area
        #print star_density
        
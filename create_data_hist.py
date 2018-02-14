#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
# Algorithm to take in stream data and create a milkyway@home compatible histogram
import os
from mpl_toolkits.mplot3d import Axes3D
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from curve_fit import *

class vel_data:     # place to store the velocity data. Makes it a little easier to keep track of the variables
    def __init__(self):
        self.los = []; self.lda = []; self.err = []; 
        self.disp = []; self.disp_err = []; 
        self.bnd_N = [];
        
class beta_data:
    def __init__(self):
        self.sums = []; self.sqsums = []
        self.disp = []; self.disp_err = []
        self.binN = []
        self.beta_coors = []
        
class binned_data:                          # class to store binned data
    def __init__(self):
        self.counts = []
        self.err = []
        
class bin_parameters:                       # class to store binner parameters
    def __init__(self, file_name = None):   # init the data bins since its common between star counts and vgsr disp.
        self.bin_lowers = []                # the lower coordinates for each bin 
        self.bin_uppers = []                # the upper coordinates for each bin
        self.bin_N = []                     # to store the counts from Yannys data to compare with out own binned counts
        self.count_lda = []                 # to store the bin centers for plotting
        self.Nbins = None                   # the number of bins
        
        if(file_name):                      # if there is a data file with bin beginnings and endings then we can use that
            file_name = open(file_name, "r")
            for line in file_name:
                ss = line.split(" ")
                bn_lower = float(ss[0])             # read the lower and upper bin coordinates from file
                bn_upper = float(ss[1])
                bn_n     = float(ss[3])
                self.bin_lowers.append(bn_lower)    # store bin upper and lower coordinates
                self.bin_uppers.append(bn_upper)
                self.bin_N.append(bn_n)
                self.count_lda.append(bn_lower + (bn_upper - bn_lower) / 2.0) # center of the bin which is what we will plot
                
            self.Nbins = len(self.bin_lowers) 
            
        else: # regularly size the bins automatically if we don't use Yanny's bin coordinates
            self.Nbins = 10 
            self.bin_start = -30.0
            self.bin_end   = 30.0
            self.bin_size = (abs(self.bin_start - self.bin_end) / self.Nbins)
            self.count_lda = []
            for i in range(0, self.Nbins):
                self.count_lda.append(self.bin_start + self.bin_size * (0.5  + i) ) # middle bin coordinates

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
            plt.bar(fit_xs,  fit_fs, width=w, color='m', alpha = 1., label = 'paras = ' + str(round(fit_paras[0], 2)) + ' ' + str(round(fit_paras[1], 2)) + ' ' + str(round(fit_paras[2], 2)) + ' ' + str(round(fit_paras[3], 2)) + ' ' + str(round(fit_paras[4], 2)) )
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

class data:#class system for reading in data and making a data histogram
    def __init__(self, vgsr_file, on_field_counts_file, off_field_counts_file):
        self.vgsr_file = vgsr_file
        self.on_field_counts_file = on_field_counts_file
        self.off_field_counts_file = off_field_counts_file
        
        self.ON_count_err = []
        self.OFF_count_err = []
        
        self.read_vgsr()
        self.read_counts()
        
        
        
    def read_vgsr(self):
        self.vel = vel_data()
        #self.vel_los = []; self.vel_los_lda = []; self.vel_los_err = []
        
        
        f = open(self.vgsr_file, 'r')
        read_data = False
        for line in f:
            if(line.startswith("#")):
                read_data = False
                continue
            else: 
                read_data = True
                
            if(read_data):
                ss = line.split(" ")
                v_disp_lda  = float(ss[50])
                v_disp      = float(ss[29])
                v_err       = float(ss[17])
                #print v_disp, v_err, v_disp_lda
                self.vel.los.append(v_disp)
                self.vel.lda.append(v_disp_lda)
                self.vel.err.append(v_err)
                
        f.close()
        
    def read_counts(self):
        self.ON_star_N_lbda = []; self.OFF_star_N_lbda = [];
        self.ON_star_N_beta = []; self.OFF_star_N_beta = [];
        self.beta_ON  = beta_data()
        self.beta_OFF = beta_data()
        self.bin_ON   = binned_data()
        self.bin_OFF  = binned_data()
        
        f = open(self.on_field_counts_file, 'r')
        g = open(self.off_field_counts_file, 'r')
        read_data = False
        for line in f:
            if(line.startswith("#")):
                read_data = False
                continue
            else: 
                read_data = True
                
            if(read_data):
                line = line.strip(" ")#remove the leading and trailing empty space
                line = line.replace('   ', ' ')#the data is not regularly spaced
                line = line.replace('  ', ' ')

                ss = line.split(" ")
                #print ss
                str_N_lbda  = float(ss[0])
                str_N_beta  = float(ss[1])
                if(len(ss) > 1):
                    str_N       = float(ss[3])
                
                self.ON_star_N_lbda.append(str_N_lbda)
                self.ON_star_N_beta.append(str_N_beta)
        read_data = False
        for line in g:
            if(line.startswith("#")):
                read_data = False
                continue
            else: 
                read_data = True
                
            if(read_data):
                line = line.strip(" ")#remove the leading and trailing empty space
                line = line.replace('   ', ' ')#the data is not regularly spaced
                line = line.replace('  ', ' ')

                ss = line.split(" ")
                str_N_lbda  = float(ss[0])
                str_N_beta  = float(ss[1])
                if(len(ss) > 1):
                    str_N       = float(ss[3])
                
                self.OFF_star_N_lbda.append(str_N_lbda)
                self.OFF_star_N_beta.append(str_N_beta)
        f.close()
        g.close()
    
    
    
    def bin_counts(self, star_N_lbda, star_N_beta, field):#need to bin the data into regularly sized bins
        bnd_counts = []
        beta_sums = []; beta_sqsums = []; beta_binN = []
        
        #obs = [[]]#for debugging
        bin_lower = None
        bin_upper = None
        
        if(self.bnd.bin_lowers):
            bin_upper_init = self.bnd.bin_uppers[0]
            bin_lower_init = self.bnd.bin_lowers[0]
        else:
            bin_upper_init = self.bnd.bin_start + self.bnd.bin_size     #reinitiaze the bin search brackets
            bin_lower_init = self.bnd.bin_start
        
        
        for i in range(0, self.bnd.Nbins):
            bnd_counts.append(0.0)
            beta_sums.append(0.0)
            beta_sqsums.append(0.0)
            beta_binN.append(0.0)
            if(field == "ON"):
                self.beta_ON.beta_coors.append([])
            else:
                self.beta_OFF.beta_coors.append([])
        
            #obs.append([])#for debugging
            
        for i in range(0, len(star_N_lbda)):        #go through all the stars
            bin_upper = bin_upper_init              #restart at the beginning of the histogram
            bin_lower = bin_lower_init
            
            #print bin_lower, bin_upper
            for j in range(0, self.bnd.Nbins):
                if(self.bnd.bin_lowers):
                    bin_lower = self.bnd.bin_lowers[j]       #current lower bin
                    bin_upper = self.bnd.bin_uppers[j]       #current upper bin
                
                if(star_N_lbda[i] >= bin_lower and star_N_lbda[i] < bin_upper):
                    bnd_counts[j]      += 1.0

                    beta_sums[j]       += star_N_beta[i]
                    beta_sqsums[j]     += star_N_beta[i]**2.
                    beta_binN[j]       += 1.0
                    
                    if(field == "ON"):
                        self.beta_ON.beta_coors[j].append(star_N_beta[i])
                    elif(field == "OFF"):
                        self.beta_OFF.beta_coors[j].append(star_N_beta[i])
                        
                    #obs[j].append(star_N_lbda[i])  #for debugging
                    break                           #if bin found no need to keep searching

                if(not self.bnd.bin_lowers):                 #if it is standard binning, advance the bins
                    bin_lower = bin_upper           #shift the search brackets by 1 bin
                    bin_upper = bin_lower + self.bnd.bin_size
                #print bin_lower, bin_upper
        if(field == "ON"):
            self.bin_ON.counts  = bnd_counts
            self.beta_ON.sums   = beta_sums
            self.beta_ON.sqsums = beta_sqsums
            self.beta_ON.binN   = beta_binN
            #print self.beta_ON.beta_coors
        elif(field == "OFF"):
            self.bin_OFF.counts  = bnd_counts
            self.beta_OFF.sums   = beta_sums
            self.beta_OFF.sqsums = beta_sqsums
            self.beta_OFF.binN   = beta_binN
            #print self.beta_OFF.beta_coors
        
        del star_N_lbda, bnd_counts, star_N_beta, beta_sums, beta_sqsums, beta_binN
        
        return 0
    
    
    def bin_vgsr(self, bin_lowers = None, bin_uppers = None):       #need to bin the data into regularly sized bins
        bnd_vel_sum     = []
        bnd_vel_sqsum   = []
        bnd_vgsr_counts = []
        velDisp_err     = []
        bnd_vel_disp    = []
        vsq_sumerr = []
        v_sumerr = []
        
        if(bin_lowers):
            bin_upper_init = bin_uppers[0]
            bin_lower_init = bin_lowers[0]
        else:
            bin_upper_init = self.bnd.bin_start + self.bnd.bin_size # reinitialize the bin search brackets
            bin_lower_init = self.bnd.bin_start
        
        #obs = [[]]#for debugging
        
        for i in range(0, self.bnd.Nbins):
            bnd_vgsr_counts.append(0.0)
            bnd_vel_sum.append(0.0)
            bnd_vel_sqsum.append(0.0)
            bnd_vel_disp.append(0.0)
            velDisp_err.append(0.0)
            vsq_sumerr.append(0.0)
            v_sumerr.append(0.0)
            
            #obs.append([])#for debugging
        
        for i in range(0, len(self.vel.lda)):     # for every vel coordinate 
            bin_upper = bin_upper_init            # restart at the beginning of the histogram
            bin_lower = bin_lower_init
            
            for j in range(0, self.bnd.Nbins):
                if(bin_lowers):                   # if the bin coordinates were already given then iterate through them #
                    bin_lower = bin_lowers[j]     # current lower bin. determined from given coordinates #
                    bin_upper = bin_uppers[j]     # current upper bin #
                    
                if(self.vel.lda[i] >= bin_lower and self.vel.lda[i] < bin_upper):       # check if coordinate is in bin
                    vsq = self.vel.los[i] * self.vel.los[i]
                    
                    bnd_vel_sum[j]     += self.vel.los[i]                               # needed to calculate the vel dispersion. sum of the vels#
                    bnd_vel_sqsum[j]   += vsq                                           # also needed for vel dispersion. sum of the sqrs of the vels #
                    bnd_vgsr_counts[j] += 1.0                                           # increase the counts in each bin. #
                    
                    ersq = self.vel.err[i] * self.vel.err[i] 
                    v_sumerr[j]   += ersq                                               # propagating the error for the v summation    
                    vsq_sumerr[j] += 4.0 * ersq * vsq                                   # propagating the error for the v sqr summation. its (2*error*v)^2
                    
                    #obs[j].append(self.vel_los[i]) #for debugging
                    #self.bnd_counts[j] += self.star_N[i]
                    
                    break #if bin found no need to keep searching

                if(not bin_lowers):         # if it is standard binning, advance the bins. i.e. bin coordinates were not given
                    bin_lower = bin_upper   # shift the search brackets by 1 bin
                    bin_upper = bin_lower + self.bnd.bin_size

        for i in range(0, self.bnd.Nbins):                                  # go through the bins
            v_sumerr[i]   = v_sumerr[i] ** 0.5                              # error is the square root of the sums
            vsq_sumerr[i] = vsq_sumerr[i] ** 0.5
            
            if(bnd_vgsr_counts[i] > 1):                                     # only calc vel disp if it makes sense to do so.
                N1 = (bnd_vgsr_counts[i] - 1.0)                             # reduced count    
                N2 = (bnd_vgsr_counts[i])                                   # total count
                
                a = bnd_vel_sqsum[i] / N1                                   # coeff1 of vel dispersion equation
                a_err = vsq_sumerr[i] / N1                                  # error gets divided by constant as well    
                
                b = N2 / N1                                                 # coeff 2
                
                c = bnd_vel_sum[i] / N2                                     # coeff 3
                c_err = v_sumerr[i] / N2                                    # error gets divided by constant as well 

                bnd_vel_disp[i] = ( a - b * c * c ) ** 0.5                  # vel dispersion equation rewritten for computational ease 
                
                cc_err = 2.0 * c_err * c                                    # error in the c * c part
                
                bcc_err = cc_err * b                                        # error is multiplied by constant
                
                a_min_b_err = ( a_err * a_err + bcc_err * bcc_err)**0.5     # error in the difference, a - bcc
                #print N1, '\t', N2, '\t', b,'\t',  a, '\t',   a_err, '\t',b, '\t', c, '\t', c_err, '\t',  cc_err, '\t',  bcc_err, '\t', bnd_vel_disp[i], '\t', a_min_b_err
                
                #velDisp_err[i] = a_min_b_err * a_min_b_err / (4.0 * bnd_vel_disp[i])                    # error due to square root. error formula for smething to a power of .5
                velDisp_err[i] = (N2**0.5 / N1 ) * bnd_vel_disp[i]
                #Nerr1 = (bnd_vgsr_counts[i] - 1.0) ** 0.5               # error for reduced count
                #Nerr2 = (bnd_vgsr_counts[i]) ** 0.5                     # error in total count
                #a_err = a * ( (vsq_sumerr[i] / bnd_vel_sqsum[i])**2.0 + (Nerr1 / N1)**2  ) **0.5       # error due to division of two things with error for coeff1
                #b_err = b * ( (Nerr1 / N1 )**2.0 + (Nerr2 / N2)**2 )**0.5                               # error due to division of two things with error for coeff2  
                #c_err = c * ( (v_sumerr[i] / bnd_vel_sum[i])**2.0 + (Nerr2 / N2)**2  ) **0.5           # error due to division of two things with error for coeff3
                #bcc_err = b * c * c * ( (cc_err / (c * c))**2.0 + (b_err / b)**2.0 )**0.5               # error in the b * cc part
                
                
            else:                                                       # if too few items in the bin:
                bnd_vel_disp[i] = -1                               # mark the bin off as negative to be skipped when comparing histograms
        
        self.vel.disp = bnd_vel_disp
        self.vel.disp_err = velDisp_err
        self.vel.bnd_N = bnd_vgsr_counts
        return 0
    
    def binned_diff(self):                                                                          # take the difference between the on and off fields.
        self.beta_diff = beta_data()
        self.bin_diff = binned_data()

        if(len(self.bin_ON.counts) > 0 and len(self.bin_OFF.counts) > 0):
            for i in range(0, len(self.bin_ON.counts)):
                self.bin_diff.counts.append(abs(self.bin_ON.counts[i] - self.bin_OFF.counts[i]))           # find the difference in the on and off field in each bin
                self.bin_diff.err.append( (self.bin_ON.counts[i] + self.bin_OFF.counts[i])**0.5)    # error in the difference. The error in the counts is the sq root of the counts. The sum of the squares is then this.    
                
                #self.beta_diff.sums.append(  (self.beta_ON.sums[i]   - self.beta_OFF.sums[i]))
                #self.beta_diff.sqsums.append((self.beta_ON.sqsums[i] - self.beta_OFF.sqsums[i]))
                #self.beta_diff.binN.append(  abs(self.beta_ON.binN[i]   - self.beta_OFF.binN[i]))
                
                self.beta_diff.sums.append(  (self.beta_ON.sums[i]))
                self.beta_diff.sqsums.append((self.beta_ON.sqsums[i] ))
                self.beta_diff.binN.append(  abs(self.beta_ON.binN[i]))
    
    def beta_dispersion(self):
        #print self.beta_diff.sums
        #print self.beta_diff.sqsums
        for i in range(0, len(self.beta_diff.sums)):
            sums = self.beta_diff.sums[i]
            sqsums = self.beta_diff.sqsums[i]
            
            N = self.beta_diff.binN[i]
            if(N > 2):
                dispsq = sqsums / (N - 1.)
                #print dispsq, sqsums, sums**2.
                dispsq -= ( N / (N - 1.) ) * (sums / N)**2.
                #print dispsq, ( N / (N - 1.) ) * (sums / N)**2., N, '\n'
                dispsq = dispsq**0.5
                self.beta_diff.disp.append(dispsq)
                
                
                
                
            else:
                self.beta_diff.disp.append(-1)
                
        #print self.beta_diff.disp
    
    def normalize_counts(self, N, Nerr):# need to normalize counts in the mw@home data histogram
        self.bin_normed = binned_data()
        f_turn_offs = 7.5
        self.mass_per_count = 1.0 / 222288.47   # each count represents about 5 solar masses #
        total = 0.0
        total_error = 0.0
        
        for i in range(0, len(N)):
            N[i] *= f_turn_offs
            Nerr[i] *= f_turn_offs
            total += N[i]                       # calc the total counts #
            total_error +=  Nerr[i] * Nerr[i]   # total error is sum in quadrature of each error #
        total_error = total_error **0.5         # take the sqr root #
        
        self.total_count = total                # for use when printing the histogram
        c2 = total_error / total                # coeff for use later #
        for i in range(0, len(N)):
            self.bin_normed.counts.append(N[i] / total)  # normalized counts #
            
            if(N[i] > 0):                       # error for bins with counts in them #
                c1 = Nerr[i] / N[i]             # another coeff #     
                er = (N[i] / total) * (c1 * c1 + c2 *c2)**0.5 # follows the error formula for division of two things with error, in this case the individual count and the total #
                self.bin_normed.err.append(er)
                ###self.N_error.append( (N[i]**0.5) / total)
            else:
                self.bin_normed.err.append(1.0 / total)              # if there is no counts, then the error is set to this default #


    def plot_vgsr(self):
        f, ((ax1, ax2, ax3)) = plt.subplots(3, sharex='col')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        w = 3
        ax1 = plt.subplot(311)
        plt.xlim(40, -50)
        plt.ylim(-300, 300)
        plt.ylabel("v$_{gsr}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50], alpha = 0)
        plt.scatter(self.vel.lda, self.vel.los, s = .5, marker = "o", color = "k", alpha = 1)
        
        ax2 = plt.subplot(312)
        plt.xlim(40, -50)
        plt.ylim(0, 18)
        plt.ylabel("$\sigma$")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50], alpha = 0)
        plt.bar(self.bnd.count_lda, self.vel.disp, width = w, color = "w", edgecolor = "k", alpha = 1)
        
        ax3 = plt.subplot(313)
        plt.xlim(40, -50)
        #plt.ylim(0, 18)
        plt.ylabel("N")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        plt.bar(self.bnd.count_lda, self.vel.bnd_N, width = w, color = "w", edgecolor = "k", alpha = 1)
        
        plt.savefig('figure6_recreation.png', format='png')             
        

        plt.savefig('figure6_recreation.png', format='png')        
        plt.clf()
        
    def plot_counts(self):
        plt.xlim(50, -50)
        plt.ylim(0, 1500)
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.ylabel("N")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        #plt.tick_params(which='minor', length=4, color='r')
        w = 2.6
        if(len(self.bin_ON.counts) > 0):
            plt.bar(self.bnd.count_lda, self.bin_ON.counts, width = w, color = "w", edgecolor = "k", alpha = 1)
        if(len(self.bin_OFF.counts) > 0):
            plt.bar(self.bnd.count_lda, self.bin_OFF.counts, width = w, color = "w", edgecolor = "r", alpha = 0.5)
        
        if(len(self.bin_diff.counts) > 0):
            plt.bar(self.bnd.count_lda, self.bin_diff.counts, width = w, color = "b", edgecolor = "b", alpha = 0.5)
            plt.bar(self.bnd.count_lda, self.bnd.bin_N, width = w, color = "k", edgecolor = "b", alpha = 0.5)
        plt.savefig('figure5_recreation.png', format='png')
        plt.clf()
        #plt.show()
    
    def plot_simN_normed(self):
        plt.xlim(50, -50)
        #plt.ylim(0, 1500)
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.ylabel("N")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        #plt.tick_params(which='minor', length=4, color='r')
        w = 2.6
        plt.bar(self.bnd.count_lda, self.bin_normed.counts, width = w, color = "b", edgecolor = "b", alpha = 0.5)
        plt.savefig('figure5_simunits_normed.png', format='png')
        plt.clf()
        #plt.show()   
        
        
    def make_mw_hist(self):
        hist = open("data_hist_fall_2017.hist", "w")
        hist.write("# Orphan Stream histogram \n# Generated from data from Dr. Yanny from Orphan stream paper\n# format is same as other MW@Home histograms\n#\n#\n")
        hist.write("n = %i\n" % (int(self.total_count)))
        hist.write("massPerParticle = %.15f\n" % (self.mass_per_count))
        hist.write("lambdaBins = %i\nbetaBins = 1\n" % (len(self.bnd.count_lda)))
        for i in range(0, len(self.bnd.count_lda)):
            hist.write("1 %.15f %.15f %.15f %.15f %.15f %.15f\n" % (self.bnd.count_lda[i], 0, self.bin_normed.counts[i], self.bin_normed.err[i],  self.vel.disp[i], self.vel.disp_err[i]))
        
    def data_clear(self, stage):
        if(stage == 'data lists'):      # first stage of deletion. Deletes stored data
            del self.ON_star_N_lbda     # delets the on and off field data when no longer needed #
            del self.OFF_star_N_lbda
            del self.ON_star_N_beta
            del self.OFF_star_N_beta
            del self.vel.los            # dels the line of sight vels #
            del self.vel.lda            # dels the coordinates for the line of sight vels #
            del self.vel.err            # dels the errors for the line of sight vels
        if(stage == 'binned counts'):   # stage deletes the binned data for each field
            del self.bin_ON
            del self.bin_OFF
            del self.beta_ON
            del self.beta_OFF
        if(stage == 'binned diff'):     # deletes binned data of the difference between fields after normalization
            del self.bin_diff
            del self.bnd.bin_N

    
def main():
    # name of the data files # 
    vgsr_file = "my16lambet2bg.specbhb.dist.lowmet.stream"
    on_field_counts_file = "l270soxlbfgcxNTbcorr.newon"
    off_field_counts_file = "l270soxlbfgcxNTbcorr.newoff"
    bin_data = "data_from_yanny.dat"
    
    
    # get the data  #
    dat = data(vgsr_file, on_field_counts_file, off_field_counts_file)
    
    # initiaze bins parameters #
    #dat.bnd = bin_parameters(bin_data)
    dat.bnd = bin_parameters()
    
    # bin the star counts #
    dat.bin_counts(dat.ON_star_N_lbda,  dat.ON_star_N_beta,  "ON" )
    dat.bin_counts(dat.OFF_star_N_lbda, dat.OFF_star_N_beta, "OFF")

    
    # bin the vgsr los, and vel disp #
    #dat.bin_vgsr(dat.bnd.bin_lowers, dat.bnd.bin_uppers)
    
    # plot the vgsr points #
    #dat.plot_vgsr()                                         
    
    # clears the data lists, only need binned data #
    dat.data_clear('data lists')                            
    
    
    # get the binned diff of the two fields. also the error in the difference #
    dat.binned_diff()      
    
    
    # plot the binned counts #
    #dat.plot_counts()                                       
    
    # bin the beta counts #
    betas = bin_betas(dat.beta_ON.beta_coors, dat.beta_OFF.beta_coors, dat.bnd)
    
    
    # deletes the on and off field bin data. only need bin diff data # 
    dat.data_clear('binned counts')                         
    
    # calculate beta dispersion # 
    #dat.beta_dispersion()
    
    # normalize the binned counts #
    #dat.normalize_counts(dat.bin_diff.counts, dat.bin_diff.err)
    
    #dat.plot_simN_normed()  
    
    # deletes binned diff. only need converted #
    dat.data_clear('binned diff')
    
    # makes the actual mw@h histogram #
    #dat.make_mw_hist()
    
main()
    
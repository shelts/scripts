#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

class data:#class system for reading in data and making a data histogram
    def __init__(self, vgsr_file, on_field_counts_file, off_field_counts_file):
        self.vgsr_file = vgsr_file
        self.on_field_counts_file = on_field_counts_file
        self.off_field_counts_file = off_field_counts_file
        
        self.star_N = []
        self.bnd_counts_ON = []
        self.bnd_counts_OFF = []
        self.bnd_diff = []
        self.bnd_vel_disp = []
        self.bnd_vgsr_counts = []
        
        self.read_vgsr()
        self.read_counts()
        
    def read_vgsr(self):
        self.vel_los = []; self.vel_los_lda = []
        
        
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
                
                self.vel_los.append(v_disp)
                self.vel_los_lda.append(v_disp_lda)
                
        f.close()
        
    def read_counts(self):
        self.ON_star_N = []; self.OFF_star_N = []; self.ON_star_N_lbda = []; self.star_N_err = []; self.OFF_star_N_lbda = [];
        
        
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
                str_N_lbda  = float(ss[0])
                if(len(ss) > 1):
                    str_N       = float(ss[3])
                #str_N_err   = float(ss[2])
                
                self.ON_star_N_lbda.append(str_N_lbda)
                if(len(ss) > 1):
                    self.ON_star_N.append(str_N); 
                #self.star_N_err.append(str_N_err)
        
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
                if(len(ss) > 1):
                    str_N       = float(ss[3])
                #str_N_err   = float(ss[2])
                
                self.OFF_star_N_lbda.append(str_N_lbda)
                if(len(ss) > 1):
                    self.OFF_star_N.append(str_N); 
                #self.star_N_err.append(str_N_err)
        f.close()
        g.close()
    
    def convert_strN_simN(self):#data is in solar masses. need to convert to simulation units
        self.N_sim_units = []
        for i in range(0, len(self.star_N)):
            n = self.star_N[i] * 5.0 / 222288.24 #each count is fturn off star which reps about a cluster of 5 solar masses
            self.N_sim_units.append(n)
            
    def normalize_counts(self):#need to normalize counts in the mw@home data histogram
        total = 0.0
        self.N_normed = []
        for i in range(0, len(self.N_sim_units)):
            total = total + self.N_sim_units[i]
            
        for i in range(0, len(self.N_sim_units)):
            self.N_normed.append(self.N_sim_units[i] / total)
    
    
    def init_bins(self):
        self.bin_size = 4.0
        self.bin_start = -50.0
        self.bin_end   = 50.0
        self.Nbins = int( abs(self.bin_start - self.bin_end) / self.bin_size)
        self.bnd_count_lda = []
        
        for i in range(0, self.Nbins):
            self.bnd_count_lda.append(self.bin_start + self.bin_size * (0.5  + i) )#middle bin coordinates
        
    
    
    def bin_counts(self, star_N_lbda, field):#need to bin the data into regularly sized bins
        bnd_counts = []
        bin_upper = self.bin_start + self.bin_size #initiaze the bin search brackets
        bin_lower = self.bin_start
        #obs = [[]]#for debugging
        
        for i in range(0, self.Nbins):
            bnd_counts.append(0.0)
            #obs.append([])#for debugging
        
        for i in range(0, len(star_N_lbda)):
            bin_upper = self.bin_start + self.bin_size#reinitiaze the bin search brackets
            bin_lower = self.bin_start
            
            for j in range(0, self.Nbins):
                if(star_N_lbda[i] >= bin_lower and star_N_lbda[i] < bin_upper):
                    #print bin_lower, bin_upper
                    #print star_N_lbda[i]
                    bnd_counts[j] += 1.0
                    
                    #obs[j].append(star_N_lbda[i]) #for debugging
                    #self.bnd_counts[j] += self.star_N[i]
                    
                    break
                
                bin_lower = bin_upper#shift the search brackets by 1 bin
                bin_upper = bin_lower + self.bin_size

        if(field == "ON"):
            self.bnd_counts_ON = bnd_counts
        elif(field == "OFF"):
            self.bnd_counts_OFF = bnd_counts

        del star_N_lbda, bnd_counts
        
        return 0
    
    
    def bin_vgsr(self):#need to bin the data into regularly sized bins
        bnd_vel_sum     = []
        bnd_vel_sqsum   = []
        bnd_vgsr_counts = []
        
        bin_upper = self.bin_start + self.bin_size #initiaze the bin search brackets
        bin_lower = self.bin_start
        #obs = [[]]#for debugging
        
        for i in range(0, self.Nbins):
            bnd_vgsr_counts.append(0.0)
            bnd_vel_sum.append(0.0)
            bnd_vel_sqsum.append(0.0)
            self.bnd_vel_disp.append(0.0)
            #obs.append([])#for debugging
        
        for i in range(0, len(self.vel_los_lda)):
            bin_upper = self.bin_start + self.bin_size#reinitiaze the bin search brackets
            bin_lower = self.bin_start
            
            for j in range(0, self.Nbins):
                if(self.vel_los_lda[i] >= bin_lower and self.vel_los_lda[i] < bin_upper):
                    bnd_vel_sum[j]     += self.vel_los[i]
                    bnd_vel_sqsum[j]   += self.vel_los[i] * self.vel_los[i]
                    bnd_vgsr_counts[j] += 1.0
                    
                    #obs[j].append(self.vel_los[i]) #for debugging
                    #self.bnd_counts[j] += self.star_N[i]
                    
                    break

                bin_lower = bin_upper#shift the search brackets by 1 bin
                bin_upper = bin_lower + self.bin_size

        
        for i in range(0, self.Nbins):
            if(bnd_vgsr_counts[i] > 1):
                a = bnd_vel_sqsum[i] / (bnd_vgsr_counts[i] - 1.0)
                b = bnd_vgsr_counts[i] / (bnd_vgsr_counts[i] - 1.0)
                c = bnd_vel_sum[i] / bnd_vgsr_counts[i]
                self.bnd_vel_disp[i] = ( a - b * c * c ) ** 0.5
            else:
                self.bnd_vel_disp[i] = -1
        self.bnd_vgsr_counts = bnd_vgsr_counts
        #print bnd_vgsr_counts
        #print bnd_vel_disp 
        #print obs
        return 0
    
    
    
    def binned_diff(self):
        if(len(self.bnd_counts_ON) > 0 and len(self.bnd_counts_OFF) > 0):
            for i in range(0, len(self.bnd_counts_ON)):
                self.bnd_diff.append(self.bnd_counts_ON[i] - self.bnd_counts_OFF[i])
    
    def plot_vgsr(self):
        f, ((ax1, ax2, ax3)) = plt.subplots(3, sharex='col')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        
        ax1 = plt.subplot(311)
        plt.xlim(40, -50)
        plt.ylim(-300, 300)
        plt.ylabel("v$_{gsr}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50], alpha = 0)
        plt.scatter(self.vel_los_lda, self.vel_los, s = .5, marker = "o", color = "k", alpha = 1)
        
        ax2 = plt.subplot(312)
        plt.xlim(40, -50)
        plt.ylim(0, 18)
        plt.ylabel("$\sigma$")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50], alpha = 0)
        plt.bar(self.bnd_count_lda, self.bnd_vel_disp, width = 4, color = "w", edgecolor = "k", alpha = 1)
        
        ax3 = plt.subplot(313)
        plt.xlim(40, -50)
        #plt.ylim(0, 18)
        plt.ylabel("N")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        plt.bar(self.bnd_count_lda, self.bnd_vgsr_counts, width = 4, color = "w", edgecolor = "k", alpha = 1)
        
        plt.savefig('figure6_recreation.png', format='png')             
        

        plt.savefig('figure6_recreation.png', format='png')        
        plt.clf()
        
    def plot_counts(self):
        plt.xlim(50, -50)
        plt.ylim(0, 2000)
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.ylabel("N")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        #plt.tick_params(which='minor', length=4, color='r')
        if(len(self.bnd_counts_ON) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_counts_ON, width = 4, color = "w", edgecolor = "k", alpha = 1)
        if(len(self.bnd_counts_OFF) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_counts_OFF, width = 4, color = "w", edgecolor = "r", alpha = 0.5)
        
        if(len(self.bnd_diff) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_diff, width = 4, color = "b", edgecolor = "b", alpha = 0.5)
        plt.savefig('figure5_recreation.png', format='png')
        plt.clf()
        #plt.show()
    
    
    def data_clear(self):
        del self.ON_star_N_lbda
        del self.OFF_star_N_lbda
    
def main():
    vgsr_file = "my16lambet2bg.specbhb.dist.lowmet.stream"
    on_field_counts_file = "l270soxlbfgcxNTbcorr.newonR"
    off_field_counts_file = "l270soxlbfgcxNTbcorr.newoffR"

    # get the data #
    dat = data(vgsr_file, on_field_counts_file, off_field_counts_file)
    
    # initiaze bins #
    dat.init_bins()
    
    # bin the on field #
    #dat.bin_counts(dat.ON_star_N_lbda, "ON")
    # bin the off field #
    #dat.bin_counts(dat.OFF_star_N_lbda, "OFF")
    
    #clears the data lists, only need binned #
    dat.data_clear()

    # get the binned diff #
    dat.binned_diff()
    
    # plot the binned counts #
    #dat.plot_counts()
    
    dat.bin_vgsr()
    
    # plot the vgsr points #
    dat.plot_vgsr()
main()
    
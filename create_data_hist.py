#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

class data:#class system for reading in data and making a data histogram
    def __init__(self, vgsr_file, counts_file):
        self.vgsr_file = vgsr_file
        self.counts_file = counts_file
        self.read_vgsr()
        self.read_counts()
        
    def read_vgsr(self):
        self.vel_disp = []; self.vel_disp_lda = []
        
        
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
                
                self.vel_disp.append(v_disp)
                self.vel_disp_lda.append(v_disp_lda)
                
        f.close()
        
    def read_counts(self):
        self.star_N = []; self.star_N_lbda = []; self.star_N_err = [];
        
        
        f = open(self.counts_file, 'r')
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
                #str_N       = float(ss[3])
                #str_N_err   = float(ss[2])
                
                #self.star_N.append(str_N); 
                self.star_N_lbda.append(str_N_lbda)
                #self.star_N_err.append(str_N_err)
                
        f.close()
    
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
    
    
    def bin_counts(self):#need to bin the data into regularly sized bins
        bin_size = 4.0
        bin_start = -50.0
        bin_end   = 50.0
        #bin_middle = 2.0 #should be half the bin size. Put this instead in
        Nbins = int( abs(bin_start - bin_end) / bin_size)
        
        self.bnd_counts = []
        self.bnd_count_lda = []
        
        bin_upper = bin_start + bin_size #initiaze the bin search brackets
        bin_lower = bin_start
        
        for i in range(0, Nbins):
            self.bnd_count_lda.append(bin_start + bin_size * (0.5  + i) )#middle bin coordinates
            self.bnd_counts.append(0.0)
        #print int(Nbins)
        #print self.bnd_count_lda
        #print len(self.bnd_count_lda)
        
        for i in range(0, len(self.star_N_lbda)):
            bin_upper = bin_start + bin_size#reinitiaze the bin search brackets
            bin_lower = bin_start
            
            for j in range(0, Nbins):
                if(self.star_N_lbda[i] >= bin_lower and self.star_N_lbda[i] < bin_upper):
                    self.bnd_counts[j] += 1.0 #self.star_N[i]
                bin_lower = bin_upper#shift the search brackets by 1 bin
                bin_upper = bin_lower + bin_size
            #print bin_lower, bin_upper, "\n"
        print self.bnd_counts
        del self.star_N_lbda, self.star_N
        
        return 0
            
    def plot_vgsr(self):
        plt.xlim(40, -50)
        plt.ylim(-300, 300)
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.ylabel("v$_{gsr}$")
        plt.scatter(self.vel_disp_lda, self.vel_disp, s = .25, marker = ".", color = "k", alpha = 1)
        plt.show()
        
        
    def plot_counts(self):
        plt.xlim(50, -50)
        #plt.ylim(0, 1500)
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.ylabel("N")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        #plt.tick_params(which='minor', length=4, color='r')
        plt.bar(self.bnd_count_lda, self.bnd_counts, width = 4, color = "w", edgecolor = "k", alpha = 1)
        plt.show()
    
def main():
    vgsr_file = "my16lambet2bg.specbhb.dist.lowmet.stream"
    counts_file = "l270soxlbfgcxNTbcorr.newonR"
    dat = data(vgsr_file, counts_file)
    #print dat.vel_disp, '\n'
    #print dat.vel_disp_lda, '\n'
    dat.bin_counts()
    dat.plot_counts()
    #print dat.star_N
main()
    
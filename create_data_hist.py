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
        
        self.ON_count_err = []
        self.OFF_count_err = []
        
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
    
    def init_bins(self, file_name = None):#init the data bins.
        if(file_name):#if there is a data file with bin beginnings and endings then we can use that
            file_name = open(file_name, "r")
            self.bin_lowers = []
            self.bin_uppers = []
            self.bin_N = []
            self.bnd_count_lda = []
            test_l = []
            test_u = []
            for line in file_name:
                ss = line.split(" ")
                bn_lower = float(ss[0])
                bn_upper = float(ss[1])
                bn_n     = float(ss[3])
                self.bin_lowers.append(bn_lower)
                self.bin_uppers.append(bn_upper)
                self.bin_N.append(bn_n)
                self.bnd_count_lda.append( bn_lower + (bn_upper - bn_lower) / 2.0 )
                
            self.Nbins = len(self.bin_lowers) 
            
        else:
            self.bin_size = 4.0
            self.bin_start = -50.0
            self.bin_end   = 50.0
            self.Nbins = int( abs(self.bin_start - self.bin_end) / self.bin_size)
            self.bnd_count_lda = []
            for i in range(0, self.Nbins):
                self.bnd_count_lda.append(self.bin_start + self.bin_size * (0.5  + i) )#middle bin coordinates
        
        return 0
        
    
    
    def bin_counts(self, star_N_lbda, field, bin_lowers = None, bin_uppers = None):#need to bin the data into regularly sized bins
        bnd_counts = []
        #obs = [[]]#for debugging
        bin_lower = None
        bin_upper = None
        if(bin_lowers):
            bin_upper_init = bin_uppers[0]
            bin_lower_init = bin_lowers[0]
        else:
            bin_upper_init = self.bin_start + self.bin_size#reinitiaze the bin search brackets
            bin_lower_init = self.bin_start
        
        
        for i in range(0, self.Nbins):
            bnd_counts.append(0.0)
            #obs.append([])#for debugging
            
        for i in range(0, len(star_N_lbda)):#go through all the stars
            bin_upper = bin_upper_init#restart at the beginning of the histogram
            bin_lower = bin_lower_init
            
            #print bin_lower, bin_upper
            for j in range(0, self.Nbins):
                if(bin_lowers):
                    bin_lower = bin_lowers[j]#current lower bin
                    bin_upper = bin_uppers[j]#current upper bin
                
                if(star_N_lbda[i] >= bin_lower and star_N_lbda[i] < bin_upper):
                    #print star_N_lbda[i]
                    bnd_counts[j] += 1.0
                    #obs[j].append(star_N_lbda[i]) #for debugging
                    break#if bin found no need to keep searching

                if(not bin_lowers):#if it is standard binning, advance the bins
                    bin_lower = bin_upper#shift the search brackets by 1 bin
                    bin_upper = bin_lower + self.bin_size
                #print bin_lower, bin_upper

        if(field == "ON"):
            self.bnd_counts_ON = bnd_counts
        elif(field == "OFF"):
            self.bnd_counts_OFF = bnd_counts
        
        del star_N_lbda, bnd_counts
        
        return 0
    
    
    def bin_vgsr(self, bin_lowers = None, bin_uppers = None):#need to bin the data into regularly sized bins
        bnd_vel_sum     = []
        bnd_vel_sqsum   = []
        bnd_vgsr_counts = []
        
        if(bin_lowers):
            bin_upper_init = bin_uppers[0]
            bin_lower_init = bin_lowers[0]
        else:
            bin_upper_init = self.bin_start + self.bin_size#reinitiaze the bin search brackets
            bin_lower_init = self.bin_start
        
        #obs = [[]]#for debugging
        
        for i in range(0, self.Nbins):
            bnd_vgsr_counts.append(0.0)
            bnd_vel_sum.append(0.0)
            bnd_vel_sqsum.append(0.0)
            self.bnd_vel_disp.append(0.0)
            #obs.append([])#for debugging
        
        for i in range(0, len(self.vel_los_lda)):
            bin_upper = bin_upper_init#restart at the beginning of the histogram
            bin_lower = bin_lower_init
            
            for j in range(0, self.Nbins):
                if(bin_lowers):
                    bin_lower = bin_lowers[j]#current lower bin
                    bin_upper = bin_uppers[j]#current upper bin
                if(self.vel_los_lda[i] >= bin_lower and self.vel_los_lda[i] < bin_upper):
                    bnd_vel_sum[j]     += self.vel_los[i]
                    bnd_vel_sqsum[j]   += self.vel_los[i] * self.vel_los[i]
                    bnd_vgsr_counts[j] += 1.0
                    
                    #obs[j].append(self.vel_los[i]) #for debugging
                    #self.bnd_counts[j] += self.star_N[i]
                    
                    break #if bin found no need to keep searching

                if(not bin_lowers):#if it is standard binning, advance the bins
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
    
    
    
    def binned_diff(self):#take the difference between the on and off fields.
        self.bnd_diff_err = []
        if(len(self.bnd_counts_ON) > 0 and len(self.bnd_counts_OFF) > 0):
            for i in range(0, len(self.bnd_counts_ON)):
                self.bnd_diff.append(abs(self.bnd_counts_ON[i] - self.bnd_counts_OFF[i]))
                self.bnd_diff_err.append( (self.bnd_counts_ON[i] + self.bnd_counts_OFF[i])**0.5)
    

    
    def normalize_counts(self, N, Nerr):#need to normalize counts in the mw@home data histogram
        self.mass_per_count = 5.0 / 222288.47 
        total = 0.0
        total_error = 0.0
        self.N_normed = []
        self.N_error = []
        for i in range(0, len(N)):
            total += N[i]
            total_error +=  Nerr[i] * Nerr[i]
        total_error = total_error **0.5
        
        self.total = total
        c2 = total_error / total
        for i in range(0, len(N)):
            self.N_normed.append(N[i] / total)
            
            if(N[i] > 0):
                c1 = Nerr[i] / N[i]
                er = (N[i] / total) * (c1 * c1 + c2 *c2)**0.5
                self.N_error.append(er)
                #self.N_error.append( (N[i]**0.5) / total)
            else:
                self.N_error.append(1.0 / total)

    def vel_disp_error(self):
        self.vel_disp_err = []
        for i in range(0, len(self.bnd_vel_disp)):
            if(self.bnd_vel_disp[i] > 0):
                coeff = self.bnd_vgsr_counts[i]**0.5 / (self.bnd_vgsr_counts[i] - 1.0)
                #print self.bnd_vgsr_counts[i]
                self.vel_disp_err.append(coeff * self.bnd_vel_disp[i])
            else:
                self.vel_disp_err.append(0)
                    


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
        plt.scatter(self.vel_los_lda, self.vel_los, s = .5, marker = "o", color = "k", alpha = 1)
        
        ax2 = plt.subplot(312)
        plt.xlim(40, -50)
        plt.ylim(0, 18)
        plt.ylabel("$\sigma$")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50], alpha = 0)
        plt.bar(self.bnd_count_lda, self.bnd_vel_disp, width = w, color = "w", edgecolor = "k", alpha = 1)
        
        ax3 = plt.subplot(313)
        plt.xlim(40, -50)
        #plt.ylim(0, 18)
        plt.ylabel("N")
        plt.xlabel("$\Lambda_{Orphan}$")
        plt.xticks( [50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])
        plt.bar(self.bnd_count_lda, self.bnd_vgsr_counts, width = w, color = "w", edgecolor = "k", alpha = 1)
        
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
        if(len(self.bnd_counts_ON) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_counts_ON, width = w, color = "w", edgecolor = "k", alpha = 1)
        if(len(self.bnd_counts_OFF) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_counts_OFF, width = w, color = "w", edgecolor = "r", alpha = 0.5)
        
        if(len(self.bnd_diff) > 0):
            plt.bar(self.bnd_count_lda, self.bnd_diff, width = w, color = "b", edgecolor = "b", alpha = 0.5)
            plt.bar(self.bnd_count_lda, self.bin_N, width = w, color = "k", edgecolor = "b", alpha = 0.5)
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
        plt.bar(self.bnd_count_lda, self.N_normed, width = w, color = "b", edgecolor = "b", alpha = 0.5)
        plt.savefig('figure5_simunits_normed.png', format='png')
        plt.clf()
        #plt.show()   
        
        
    def make_mw_hist(self):
        hist = open("data_hist_fall_2017.hist", "w")
        hist.write("# Orphan Stream histogram \n# Generated from data from Dr. Yanny from Orphan stream paper\n# format is same as other MW@Home histograms\n#\n#\n")
        hist.write("n = %i\n" % (int(self.total)))
        hist.write("massPerParticle = %.15f\n" % (self.mass_per_count))
        hist.write("lambdaBins = %i\nbetaBins = 1\n" % (len(self.bnd_count_lda)))
        for i in range(0, len(self.bnd_count_lda)):
            hist.write("1 %.15f %.15f %.15f %.15f %.15f %.15f\n" % (self.bnd_count_lda[i], 0, self.N_normed[i], self.N_error[i],  self.bnd_vel_disp[i], self.vel_disp_err[i]))
        
    def data_clear(self, stage):
        if(stage == 'data lists'):
            del self.ON_star_N_lbda
            del self.OFF_star_N_lbda
            del self.vel_los
            del self.vel_los_lda
        if(stage == 'binned counts'):
            del self.bnd_counts_ON
            del self.bnd_counts_OFF
        if(stage == 'binned diff'):
            del self.bnd_diff
            del self.bnd_diff_err
            del self.bin_N

    
def main():
    vgsr_file = "my16lambet2bg.specbhb.dist.lowmet.stream"
    on_field_counts_file = "l270soxlbfgcxNTbcorr.newonR"
    off_field_counts_file = "l270soxlbfgcxNTbcorr.newoffR"
    bin_data = "data_from_yanny.dat"
    # get the data #
    dat = data(vgsr_file, on_field_counts_file, off_field_counts_file)
    
    # initiaze bins #
    dat.init_bins(bin_data)
    
    
    dat.bin_counts(dat.ON_star_N_lbda, "ON", dat.bin_lowers, dat.bin_uppers)    # bin the on field #
    dat.bin_counts(dat.OFF_star_N_lbda, "OFF", dat.bin_lowers, dat.bin_uppers, )  # bin the off field #

    dat.bin_vgsr(dat.bin_lowers, dat.bin_uppers)    #bin the vgsr los, and vel disp
    dat.plot_vgsr()     # plot the vgsr points #
    
    
    
    dat.data_clear('data lists')   #clears the data lists, only need binned #

    dat.binned_diff()   # get the binned diff #
    #print dat.bnd_diff_err
    
    dat.plot_counts()   # plot the binned counts #
    dat.data_clear('binned counts')   #deletes the on and off field bin data. only need diff
    
    #dat.convert_strN_simN()
    #dat.plot_simN()

    
    dat.normalize_counts(dat.bnd_diff, dat.bnd_diff_err)   #normalizes the counts
    dat.plot_simN_normed()
    dat.vel_disp_error()
    
    dat.data_clear('binned diff')   #deletes binned diff. only need converted
   
    
    dat.make_mw_hist()
    
main()
    
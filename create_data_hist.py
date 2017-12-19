#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

class vel_data:     # place to store the velocity data. Makes it a little easier to keep track of the variables
    def __init__(self):
        self.los = []; self.lda = []; self.err = []; 
        self.disp = []; self.disp_err = []; 
        self.bnd_N = [];
        

class binned_data:                          # class to store binned data and binner parameters
    def __init__(self, file_name = None):   # init the data bins since its common between star counts and vgsr disp.
        self.counts_ON = []                 # to store the binned on and off field counts
        self.counts_OFF = []
        self.diff = []                      # to store the binned difference between the two fields
        self.diff_err = []                  # error in each bin of the binned difference
        self.vel_disp = []                  # to store the binned velocity dispersion after binning the velocities 
        self.vgsr_counts = []               # to store the number of objects in the velocity bins
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
                self.count_lda.append( bn_lower + (bn_upper - bn_lower) / 2.0 ) # center of the bin which is what we will plot
                
            self.Nbins = len(self.bin_lowers) 
            
        else: # regularly size the bins automatically if we don't use Yanny's bin coordinates
            self.bin_size = 4.0
            self.bin_start = -50.0
            self.bin_end   = 50.0
            self.Nbins = int( abs(self.bin_start - self.bin_end) / self.bin_size)
            self.count_lda = []
            for i in range(0, self.Nbins):
                self.count_lda.append(self.bin_start + self.bin_size * (0.5  + i) ) # middle bin coordinates
        
        
    

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
                v_err       = float(ss[30])
                
                self.vel.los.append(v_disp)
                self.vel.lda.append(v_disp_lda)
                self.vel.err.append(v_err)
                
        f.close()
        
    def read_counts(self):
        self.ON_star_N_lbda = []; self.OFF_star_N_lbda = [];
        
        
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
                
                self.OFF_star_N_lbda.append(str_N_lbda)
        f.close()
        g.close()
    
    
    
    def bin_counts(self, star_N_lbda, field, bin_lowers = None, bin_uppers = None):#need to bin the data into regularly sized bins
        bnd_counts = []
        #obs = [[]]#for debugging
        bin_lower = None
        bin_upper = None
        if(bin_lowers):
            bin_upper_init = bin_uppers[0]
            bin_lower_init = bin_lowers[0]
        else:
            bin_upper_init = self.bnd.bin_start + self.bnd.bin_size     #reinitiaze the bin search brackets
            bin_lower_init = self.bnd.bin_start
        
        
        for i in range(0, self.bnd.Nbins):
            bnd_counts.append(0.0)
            #obs.append([])#for debugging
            
        for i in range(0, len(star_N_lbda)):        #go through all the stars
            bin_upper = bin_upper_init              #restart at the beginning of the histogram
            bin_lower = bin_lower_init
            
            #print bin_lower, bin_upper
            for j in range(0, self.bnd.Nbins):
                if(bin_lowers):
                    bin_lower = bin_lowers[j]       #current lower bin
                    bin_upper = bin_uppers[j]       #current upper bin
                
                if(star_N_lbda[i] >= bin_lower and star_N_lbda[i] < bin_upper):
                    #print star_N_lbda[i]
                    bnd_counts[j] += 1.0
                    #obs[j].append(star_N_lbda[i]) #for debugging
                    break                           #if bin found no need to keep searching

                if(not bin_lowers):                 #if it is standard binning, advance the bins
                    bin_lower = bin_upper           #shift the search brackets by 1 bin
                    bin_upper = bin_lower + self.bin_size
                #print bin_lower, bin_upper

        if(field == "ON"):
            self.bnd.counts_ON = bnd_counts
        elif(field == "OFF"):
            self.bnd.counts_OFF = bnd_counts
        
        del star_N_lbda, bnd_counts
        
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
                
                velDisp_err[i] = a_min_b_err * a_min_b_err / (4.0 * bnd_vel_disp[i])                    # error due to square root. error formula for smething to a power of .5
            
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
        #print bnd_vgsr_counts
        #print bnd_vel_disp 
        #print obs
        return 0
    
    
    
    def binned_diff(self):                                                                          # take the difference between the on and off fields.
        if(len(self.bnd.counts_ON) > 0 and len(self.bnd.counts_OFF) > 0):
            for i in range(0, len(self.bnd.counts_ON)):
                self.bnd.diff.append(abs(self.bnd.counts_ON[i] - self.bnd.counts_OFF[i]))           # find the difference in the on and off field in each bin
                self.bnd.diff_err.append( (self.bnd.counts_ON[i] + self.bnd.counts_OFF[i])**0.5)    # error in the difference. The error in the counts is the sq root of the counts. The sum of the squares is then this.    
    

    
    def normalize_counts(self, N, Nerr):# need to normalize counts in the mw@home data histogram
        self.mass_per_count = 5.0 / 222288.47   # each count represents about 5 solar masses #
        total = 0.0
        total_error = 0.0
        self.N_normed = []
        self.N_error = []
        for i in range(0, len(N)):
            total += N[i]                       # calc the total counts #
            total_error +=  Nerr[i] * Nerr[i]   # total error is sum in quadrature of each error #
        total_error = total_error **0.5         # take the sqr root #
        
        self.total = total
        c2 = total_error / total                # coeff for use later #
        for i in range(0, len(N)):
            self.N_normed.append(N[i] / total)  # normalized counts #
            
            if(N[i] > 0):                       # error for bins with counts in them #
                c1 = Nerr[i] / N[i]             # another coeff #     
                er = (N[i] / total) * (c1 * c1 + c2 *c2)**0.5 # follows the error formula for division of two things with error, in this case the individual count and the total #
                self.N_error.append(er)
                #self.N_error.append( (N[i]**0.5) / total)
            else:
                self.N_error.append(1.0 / total)              # if there is no counts, then the error is set to this default #


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
        if(len(self.bnd.counts_ON) > 0):
            plt.bar(self.bnd.count_lda, self.bnd.counts_ON, width = w, color = "w", edgecolor = "k", alpha = 1)
        if(len(self.bnd.counts_OFF) > 0):
            plt.bar(self.bnd.count_lda, self.bnd.counts_OFF, width = w, color = "w", edgecolor = "r", alpha = 0.5)
        
        if(len(self.bnd.diff) > 0):
            plt.bar(self.bnd.count_lda, self.bnd.diff, width = w, color = "b", edgecolor = "b", alpha = 0.5)
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
        plt.bar(self.bnd.count_lda, self.N_normed, width = w, color = "b", edgecolor = "b", alpha = 0.5)
        plt.savefig('figure5_simunits_normed.png', format='png')
        plt.clf()
        #plt.show()   
        
        
    def make_mw_hist(self):
        hist = open("data_hist_fall_2017.hist", "w")
        hist.write("# Orphan Stream histogram \n# Generated from data from Dr. Yanny from Orphan stream paper\n# format is same as other MW@Home histograms\n#\n#\n")
        hist.write("n = %i\n" % (int(self.total)))
        hist.write("massPerParticle = %.15f\n" % (self.mass_per_count))
        hist.write("lambdaBins = %i\nbetaBins = 1\n" % (len(self.bnd.count_lda)))
        for i in range(0, len(self.bnd.count_lda)):
            hist.write("1 %.15f %.15f %.15f %.15f %.15f %.15f\n" % (self.bnd.count_lda[i], 0, self.N_normed[i], self.N_error[i],  self.vel.disp[i], self.vel.disp_err[i]))
        
    def data_clear(self, stage):
        if(stage == 'data lists'):      # first stage of deletion. Deletes stored data
            del self.ON_star_N_lbda     # delets the on and off field data when no longer needed #
            del self.OFF_star_N_lbda
            del self.vel.los            # dels the line of sight vels #
            del self.vel.lda            # dels the coordinates for the line of sight vels #
            del self.vel.err            # dels the errors for the line of sight vels
        if(stage == 'binned counts'):   # stage deletes the binned data for each field
            del self.bnd.counts_ON      
            del self.bnd.counts_OFF
        if(stage == 'binned diff'):     # deletes binned data of the difference between fields after normalization
            del self.bnd.diff
            del self.bnd.diff_err
            del self.bnd.bin_N

    
def main():
    vgsr_file = "my16lambet2bg.specbhb.dist.lowmet.stream"
    on_field_counts_file = "l270soxlbfgcxNTbcorr.newonR"
    off_field_counts_file = "l270soxlbfgcxNTbcorr.newoffR"
    bin_data = "data_from_yanny.dat"
    # get the data #
    dat = data(vgsr_file, on_field_counts_file, off_field_counts_file)
    
    # initiaze bins #
    dat.bnd = binned_data(bin_data)                         # initialize the bin parameters
    #print dat.bnd.count_lda
    
    dat.bin_counts(dat.ON_star_N_lbda, "ON", dat.bnd.bin_lowers, dat.bnd.bin_uppers)        # bin the on field #
    dat.bin_counts(dat.OFF_star_N_lbda, "OFF", dat.bnd.bin_lowers, dat.bnd.bin_uppers, )    # bin the off field #

    dat.bin_vgsr(dat.bnd.bin_lowers, dat.bnd.bin_uppers)    #bin the vgsr los, and vel disp
    dat.plot_vgsr()                                         # plot the vgsr points #
    #print dat.vel.los
    
    
    dat.data_clear('data lists')                            #clears the data lists, only need binned data #

    dat.binned_diff()                                       # get the binned diff of the two fields. also the error in the difference#
    #print dat.bnd.diff_err
    
    dat.plot_counts()                                       # plot the binned counts #
    dat.data_clear('binned counts')                         # deletes the on and off field bin data. only need bin diff data#
    
    #dat.convert_strN_simN()
    #dat.plot_simN()

    #print dat.bnd.diff
    dat.normalize_counts(dat.bnd.diff, dat.bnd.diff_err)   # normalizes the counts #
    dat.plot_simN_normed()  
    #dat.vel_disp_error()
    
    dat.data_clear('binned diff')                          #deletes binned diff. only need converted
   
    
    dat.make_mw_hist()
    
main()
    
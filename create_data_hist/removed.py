    
    def off_field_average(self):
        self.bin_off_field_aves = []
        bins_with_counts = []
        for i in range(0, self.lmda_bnd.Nbins): # for each lambda bin
            off_field_ave = 0.0
            bns = 0.0
            for j in range(0, self.beta_Nbins): # for each of the beta bins
                if(self.binned_beta_OFF[i][j] > 0.0): # make sure ave includes only bins with counts
                    off_field_ave += self.binned_beta_OFF[i][j]
                    bns += 1.0
            bins_with_counts.append(bns)
            self.bin_off_field_aves.append(off_field_ave)
            if(float(bins_with_counts[i]) > 0.0):
                self.bin_off_field_aves[i] = self.bin_off_field_aves[i] / float(bins_with_counts[i])
        
        return 0
    
    def correction(self):
        for i in range(0, self.lmda_bnd.Nbins):
            for j in range(0, self.beta_Nbins):
                self.binned_beta_ON[i][j]  -= self.bin_off_field_aves[i] * 1.
                self.binned_beta_OFF[i][j] -= self.bin_off_field_aves[i] * 1.
                
                if(self.binned_beta_ON[i][j] < 0.0):
                    self.binned_beta_ON[i][j] = 0
                if(self.binned_beta_OFF[i][j] < 0.0):
                    self.binned_beta_OFF[i][j] = 0

        return 0
    
    
    
    def plot_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        w = 0.25
        ax.set_xlabel(r"$\beta_{Orphan}$")
        ax.set_zlabel("counts")
        ax.set_ylabel(r"$\Lambda_{Orphan}$")
        for i in range(0, self.lmda_bnd.Nbins):
            ax.bar(self.bin_centers, self.binned_beta_OFF[i], width=w,zs=self.lmda_bnd.bin_centers[i], zdir='y', color='r', alpha = 0.75)
            ax.bar(self.bin_centers, self.binned_beta_ON[i], width=w,  zs=self.lmda_bnd.bin_centers[i], zdir='y',  color='b', alpha = 0.5, )
        plt.savefig('stream_beta_plots/lambda_beta_bins.png', format = 'png')
        plt.show()
        
        return 0



    def beta_dispersion(self):
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
                
                
                
    def den_correction(self):
        for i in range(0, self.lmda_bnd.Nbins):
            width = abs(self.lmda_bnd.bin_uppers[i] - self.lmda_bnd.bin_lowers[i]) #width of each lambda bin
            for j in range(0, self.beta_Nbins):
                area = self.bin_width * width
                interlopers = self.star_density[i] * area
                self.binned_beta_combined[i][j] -= interlopers
                    
                #if(self.binned_beta_combined[i][j] < 0.0):
                    #self.binned_beta_combined[i][j] = 0.0
                #print '\t\t\t\t', self.binned_beta_ON[i][j], self.binned_beta_OFF[i][j], self.binned_beta_combined[i][j], interlopers

        return 0
    
    def off_field_star_density(self):
        self.star_density = []
        length = abs(self.lower - self.upper) # length of each beta bin
        for i in range(0, self.lmda_bnd.Nbins):
            width = abs(self.lmda_bnd.bin_uppers[i] - self.lmda_bnd.bin_lowers[i]) #width of each lambda bin
            self.star_density.append(0.0)
            area = 0.0
            
            for j in range(0, self.beta_Nbins):
                if(self.binned_beta_OFF[i][j] > 0):
                    self.star_density[i] += float(self.binned_beta_OFF[i][j]) # add the counts of the bin to the total count
                    area += self.bin_width # sum of the lengths of off field with stars of the bins that had counts
            area = area * width # get the area
            if(self.star_density[i] > 0):#if there was counts then divide the area. if no counts then density is zero anyway
                self.star_density[i] = float(self.star_density[i]) / area
        
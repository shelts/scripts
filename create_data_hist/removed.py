    
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

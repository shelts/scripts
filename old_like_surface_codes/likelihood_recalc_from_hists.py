#! /usr/bin/python
#/* Copyright (c) 2018 Siddhartha Shelton */
import os
from subprocess import call
import matplotlib.pyplot as plt



class reval:
    def __init__(self, folder_name, sweeps):
        self.folder_name        = folder_name
        self.sweeps             = sweeps

    def get_likes(self):
        for i in range(0,len(self.sweeps)):
            sweep = self.sweeps[i]
            f = open(self.folder_name + sweep + "_hist_names.txt", 'r')
            data = self.folder_name + 'data_hist_fall_2017_2.hist'
            for line in f:
                line = line.split("\n")
                hist = self.folder_name + sweep + "_hists/" + line[0]
                call(["~/Desktop/research/nbody_test/bin/milkyway_nbody" +
                    " -h " + data +
                    " -S " + hist 
                    + " 2>>" + self.folder_name + "new_vals/" + sweep + "_data_vals_new.txt"], shell=True)
            f.close()
    def clear_data(self):
        os.system('rm ' +  self.folder_name + "new_vals/*_new.txt")
    
    def parse(self):
        emds = []; coss = []; vels = []; liks = []; vals = []
        for i in range(0, len(self.sweeps)):
            emds = []; coss = []; vels = []; liks = []; vals = []
            f = open(self.folder_name + 'new_vals/' + self.sweeps[i] + '_data_vals_new.txt', 'r')
            for line in f:
                if(line.startswith("<search_likelihood_all>")):
                    line = line.split("<search_likelihood_all>")
                    line = line[1].split("\t")
                    line[3] = line[3].strip("\n")
                    emd  = float(line[0])
                    cos  = float(line[1])
                    vel  = float(line[2])
                    lik  = float(line[3])
                    
                    emds.append(emd)
                    coss.append(cos)
                    vels.append(vel)
                    liks.append(lik)
            f.close()
            
            f = open(self.folder_name + 'new_vals/' + self.sweeps[i] + '_data_vals.txt', 'r')
            for line in f:
                line = line.split("\t")
                line = line[0]
                #print line
                vals.append(float(line))
            f.close()    
            self.plot(emds, coss, vels, liks, self.sweeps[i], vals)
            
    def plot(self, emds, coss, vels, liks, sweep, vals):
        plt.ylabel("Likelihood")
        plt.xlabel(sweep)
        #print sweep
        #print liks
        plt.ylim(-750, 0)
        plt.plot(vals, emds, markersize = 4, color = 'black', alpha=.5, marker = '.', linestyle='-', label = 'emd')
        plt.plot(vals, coss, markersize = 4, color = 'blue', alpha=.5, marker = '.', linestyle='-', label = 'coss')
        plt.plot(vals, vels, markersize = 4, color = 'pink', alpha=.5, marker = '.', linestyle='-', label = 'vels')
        plt.plot(vals, liks, markersize = 4, color = 'red', alpha=.75, marker = '.', linestyle='-', label = 'liks')
        plt.legend()
        plt.savefig(self.folder_name + "new_vals/" + sweep, format='png')
        plt.clf()    
def main():
    folder_name = 'parameter_sweeps_actual_data_hists_24dec2017_nbody_version166_theoretical_vel_error_2/'
    sweeps = ['ft', 'r', 'rr', 'm', 'mr']
    
    new = reval(folder_name, sweeps)
    
    new.clear_data()
    new.get_likes()
    new.parse()
    
    
main()
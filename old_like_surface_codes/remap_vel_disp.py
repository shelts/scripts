#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import math as mt
import matplotlib.pyplot as plt

#this is code that will take the output from the parameter sweeps, reverse engineer the components of the likelihood used to calculate it and 
#recalculate the components using new functions, specifically for the velocity dispersion component.

data_file = 'likelihood_data_rand_iter_6_29_2017_new_vel_disp_comparison_singularity_limit_removed/'
#sweep_file = 'parameter_sweeps_6_29_2017_new_vel_disp_comparison_singularity_limit_removed/'
sweep_file = 'parameter_sweeps_7_13_2017_new_vel_disp_comparison_singularity_limit_removed_rescaled/'
updated = 'updated/'
parameters = ['ft', 'r', 'rr', 'm', 'mr']


class like_group:
    def __init__(self):
        self.emds = []; self.coss = []; self.vdss = []; self.liks = [];
        
    def add_values(self, emd, cos, vds, lik):
        self.emds.append(emd)
        self.coss.append(cos)
        self.vdss.append(vds)
        self.liks.append(lik)
        
    def reset(self):
        self.emds = []; self.coss = []; self.vdss = []; self.liks = [];

    def print_vals(self):
        for i in range(0, len(self.liks)):
            print("%.15f\t%.15f\t%.15f\t%.15f\n" % (self.emds[i], self.coss[i], self.vdss[i], self.liks[i]))
        
        
    def get_new_nsgma_sq(self, old_val):
        x = 1.0
        threshold = 0.001
        while(1):
            if(abs(old_val) > 0.0):
                func = (24.0) * mt.log(x) - (x / 2.0)
            else:
                func = 0.0
            
            if(func < (old_val + threshold) and func > (old_val - threshold)):
                break
            else:
                x += threshold
                
        sigma_sq = x
        #print (24.0) * mt.log(sigma_sq) - (sigma_sq / 2.0)
        #print old_val, func, old_val - func
        new_func_val = self.new_func(sigma_sq)
        return new_func_val
    
    def new_func(self, x):
        cutoff = 48.0
        #print x
        if(x <= cutoff):
            func = 0.0
        else:#this is a negative value function. The negative sign negates that and returns a positive val
            func =  (24.0 * mt.log(x) - ( x / 2.0 )  - (24.0) * (mt.log(2.0) + mt.log(24.0) - 1.0))
            #func =  ((24.0) * mt.log(x) - (x / 2.0)- (24.0) * (mt.log(2.0) + mt.log(24.0) - 1.0))
        return func
    
    
    def fix_vel_disps(self):
        for i in range(0, len(self.vdss)):
            self.vdss[i] = self.get_new_nsgma_sq(self.vdss[i])
            self.liks[i] = self.emds[i] + self.coss[i] + self.vdss[i]#positive valued likihoods
            
    def vel_disp_sign_switch(self):
        for i in range(0, len(self.vdss)):
            self.vdss[i] *= -1.0
            self.liks[i] = self.emds[i] + self.coss[i] + self.vdss[i]#positive valued likihoods
            
    def write(self, file_name):
        file_name.write('Using OpenMP 10 max threads on a system with 8 processors\n')
        
        for i in range(0, len(self.vdss)):
            file_name.write("%.15f\t%.15f\t%.15f\t%.15f\n" % (self.emds[i], self.coss[i], self.vdss[i], self.liks[i]))
            
        file_name.write('<search_likelihood>-%0.15f</search_likelihood>\n' % (self.best_like))
        
        
    def get_best_like(self):
        best_like = 99999999.99999999
        
        for i in range(0, len(self.liks)):
            if(abs(self.liks[i]) < best_like):
                best_like = self.liks[i]
                
        self.best_like = best_like
    
        
def read_and_fix(para):
    f = open(sweep_file + sweep_file + para + '.txt', 'r')
    g = open(sweep_file + updated + para + '.txt', 'w')
    
    paras = like_group()
    counter = 0 
    for line in f:
        if line.startswith('Using'):
            paras.reset()
            continue
        
        if line.startswith('<search_likelihood>'):
            #paras.print_vals()
            print 'doing set ', counter
            #paras.fix_vel_disps()
            paras.vel_disp_sign_switch()
            paras.get_best_like()
            paras.write(g)
            counter += 1
            continue
        
        
        ss = line.split("\t")
        paras.add_values(float(ss[0]), float(ss[1]), float(ss[2]), float(ss[3]))
        
            
            
    f.close()
    g.close()
            
def plot_funcs():
    paras = like_group()
    x = 0.05
    xs = []
    funcs = []
    for i in range(0, 10000):
        funcs.append(paras.new_func(x))
        xs.append(x)
        x += 0.05
        
    plt.plot(xs, funcs, '.', markersize = 1.5, color = 'purple', alpha = 1.0, marker = '.')
    plt.show()
    

def main():
    #plot_funcs()
    read_and_fix('ft')
    read_and_fix('r')
    read_and_fix('rr')
    read_and_fix('m')
    read_and_fix('mr')
    
main()
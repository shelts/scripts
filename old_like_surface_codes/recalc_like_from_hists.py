#! /usr/bin/python
#/* Copyright (c) 2017 Siddhartha Shelton */
import os
from subprocess import call

args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]

ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])

class hists:
    def __init__(self, file_path, hist_dir, parameter1, parameter2):
        self.hist_dir = hist_dir

        self.ft_c       = ft_c 
        self.bt_c       = bt_c
        self.r_c        = r_c
        self.rr_c       = rr_c
        self.m_c        = m_c
        self.mr_c       = mr_c
        self.parameter1 = parameter1    #first sweep parameter
        self.parameter2 = parameter2    #second sweep parameter. 
        self.file_path  = file_path
        
        self.ft_tmp       = ft_c 
        self.bt_tmp       = bt_c
        self.r_tmp        = r_c
        self.rr_tmp       = rr_c
        self.m_tmp        = m_c
        self.mr_tmp       = mr_c
        self.hist_dir     = hist_dir
    
    def set_parameter(self, parameter, value):
        if(parameter == 'ft'):#initializes the needed parameter to the value
            self.ft_tmp = str(value)
        
        elif(parameter == 'bt'):
            self.bt_tmp = str(value)
        
        elif(parameter == 'r'):
            self.r_tmp = str(value)
        
        elif(parameter == 'rr'):
            self.rr_tmp = str(value)
        
        elif(parameter == 'm'):
            self.m_tmp = str(value)
        
        elif(parameter == 'mr'):
            self.mr_tmp = str(value)
    
    def parameter_reset(self):
        self.ft_tmp       = self.ft_c 
        self.bt_tmp       = self.bt_c
        self.r_tmp        = self.r_c
        self.rr_tmp       = self.rr_c
        self.m_tmp        = self.m_c
        self.mr_tmp       = self.mr_c
        self.hist_tmp     = self.hist_dir
        
    def hist_correct_set(self):
        #self.hist_correct = self.hist_dir + "arg_" + self.ft_c + "_" + self.bt_c + "_" + self.r_c + "_" + self.rr_c + "_" + self.m_c + "_" + self.mr_c + "_correct.hist"
        self.hist_correct = self.hist_dir + "arg_" + self.ft_c + "_" + self.bt_c + "_" + self.r_c + "_" + self.rr_c + "_" + self.m_c + "_" + self.mr_c + "_correct_diff_seed.hist"

    def set_hist(self):
        self.hist_tmp = self.hist_dir + "arg_"  + self.ft_tmp + "_" + self.bt_tmp + "_" + self.r_tmp + "_" + self.rr_tmp + "_" + self.m_tmp + "_" + self.mr_tmp + ".hist"
        
    def write_parameters(self, f, parameter1, parameter2):
        if(parameter1 == 'ft'):#initializes the needed parameter to the value
            name1 = self.ft_tmp
        
        elif(parameter1 == 'bt'):
            name1 = self.bt_tmp
        
        elif(parameter1 == 'r'):
            name1 = self.r_tmp 
        
        elif(parameter1 == 'rr'):
            name1 = self.rr_tmp
        
        elif(parameter1 == 'm'):
            name1 = self.m_tmp 
        
        elif(parameter1 == 'mr'):
            name1 = self.mr_tmp
            
            
        if(parameter2 == 'ft'):#initializes the needed parameter to the value
            name2 = self.ft_tmp
        
        elif(parameter2 == 'bt'):
            name2 = self.bt_tmp
        
        elif(parameter2 == 'r'):
            name2 = self.r_tmp 
        
        elif(parameter2 == 'rr'):
            name2 = self.rr_tmp
        
        elif(parameter2 == 'm'):
            name2 = self.m_tmp 
        
        elif(parameter2 == 'mr'):
            name2 = self.mr_tmp
            
        f.write("%s\t%s\n" % (name1, name2))
        
        
    def match(self, pipe_name):
        hist1 = self.hist_correct
        hist2 = self.hist_tmp
        path  = self.file_path
        
        call([" " + path + "nbody_test/bin/milkyway_nbody"  
          + " -h " + hist1 
          + " -S " + hist2 + " 2>>" + pipe_name], shell=True)
        #print hist1, "\n", hist2
        os.system('ls ' + hist2)
       
       
    
    
    
    
    
    
def recalc():
    file_path = '/home/sidd/Desktop/research/'
    like_path = 'like_surface/2D_like_surface/'
    hist_dir = file_path + like_path + "2d_sweep_hists/"
    data_dir = file_path + like_path + "parameter_sweeps_2d_rand_iter/"
    
    para1 = 'rr'
    para2 = 'mr'
    
    hist = hists(file_path, hist_dir, para1, para2)
    hist.hist_correct_set()
    
    data = open(hist_dir + 'hist_names.txt', 'r')
    new_data = open(data_dir + para1 + '_' + para2  + '_vals_corrected.txt', 'w')
    new_likes = data_dir + para1 + '_' + para2 + '_corrected.txt'
    counter = 0
    for line in data:
        line = line.replace('\n', '')
        line = line.replace('arg_', '')
        line = line.replace('.hist', '')
        ss = line.split('_')
        
        rr = ss[3]
        mr = ss[5]
        
        counter += 1
        hist.set_parameter(para1, rr)
        hist.set_parameter(para2, mr)
        
        hist.set_hist()
        hist.match(new_likes)
        hist.write_parameters(new_data, para1, para2)
        
    data.close()
    new_data.close()
    
def main():
    recalc()
main()
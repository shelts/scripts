#! /usr/bin/python
#/* Copyright (c) 2017 Siddhartha Shelton */
import os
from subprocess import call
import random
random.seed(a = 12345678)
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
ft_cn  = (args[0])#cn for correct number
bt_cn  = (args[1])
r_cn   = (args[2])
rr_cn  = (args[3])
m_cn   = (args[4])
mr_cn  = (args[5])



ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])



lmc_dir = '/home/shelts/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = sid_dir

folder        = path + "like_surface/2d_sweep_hists/"
binary        = path + "nbody_test/bin/milkyway_nbody"
lua           = path + "/lua/full_control.lua"
seed          = "98213548"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"


#parameter = [start, end, increment]
ft         = [3.0, 4.0, 0.001]#
#bt         = [0.97, 1.08, 0.02]#
bt         = [0.97, 1.08, 0.02]#
r          = [0.1, 0.4, 0.2]#
rr         = [0.1, 0.4, 0.2]#
m          = [1.0, 7.0, 2.0]#
mr         = [0.150, 0.35, 0.1]#

ft_s, ft_e, ft_in = ft[0], ft[1], ft[2]
bt_s, bt_e, bt_in = bt[0], bt[1], bt[2]
r_s,  r_e,  r_in  = r[0],  r[1],  r[2]
rr_s, rr_e, rr_in = rr[0], rr[1], rr[2]
m_s,  m_e,  m_in  = m[0],  m[1],  m[2]
mr_s, mr_e, mr_in = mr[0], mr[1], mr[2]

ft_N = 25
bt_N = 25
r_N  = 4
rr_N = 50
m_N  = 4
mr_N = 50



y = True
n  = False


#choose what to run.
make_folders              = y
rebuild_binary            = n
make_correct_answer_hist  = n
run_regular_iteration     = n
run_random_iteration      = n
run_truly_random_iter     = y


run_ft_v_bt = n
run_ft_v_r  = n
run_ft_v_rr = n
run_ft_v_m  = n
run_ft_v_mr = n

run_bt_v_r  = n
run_bt_v_rr = n
run_bt_v_m  = n
run_bt_v_mr = n

run_r_v_rr  = n
run_r_v_m   = n
run_r_v_mr  = n

run_rr_v_m  = n
run_rr_v_mr = n

run_m_v_mr  = n
#--------------------------------------------------------------------------------------------------
class parameters:
    def __init__(self, ft_c, bt_c, r_c, rr_c, m_c, mr_c, hist_path, sweep_type, sweep_variables, data_val_file_name, parameter1, parameter2):
        self.ft_c       = ft_c 
        self.bt_c       = bt_c
        self.r_c        = r_c
        self.rr_c       = rr_c
        self.m_c        = m_c
        self.mr_c       = mr_c
        self.hist_path  = hist_path     #used for naming the histograms and placing them in the correct folder
        self.sweep_type = sweep_type    #extension for the sweep folder name describing the type of sweep (2D, random iteration etc)
        self.sweep_variables  = sweep_variables     #parameters over which you are sweeping.
        self.data_val_file_name  = data_val_file_name     #name of the file where data is written to.
        self.parameter1 = parameter1    #first sweep parameter
        self.parameter2 = parameter2    #second sweep parameter. 
        
        self.ft_tmp       = ft_c 
        self.bt_tmp       = bt_c
        self.r_tmp        = r_c
        self.rr_tmp       = rr_c
        self.m_tmp        = m_c
        self.mr_tmp       = mr_c
        self.hist_tmp     = hist_path
    
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
        self.hist_tmp     = self.hist_path


    def set_correct(self, parameter):
        if(parameter == 'ft'):#initializes the needed parameter to the value
            self.ft_tmp = self.ft_c 

        elif(parameter == 'bt'):
            self.bt_tmp = self.bt_c
        
        elif(parameter == 'r'):
            self.r_tmp  = self.r_c
        
        elif(parameter == 'rr'):
            self.rr_tmp = self.rr_c
        
        elif(parameter == 'm'):
            self.m_tmp  = self.m_c
        
        elif(parameter == 'mr'):
            self.mr_tmp = self.mr_c
            

    def set_hist(self):
        self.hist_tmp = self.hist_path + self.ft_tmp + "_" + self.bt_tmp + "_" + self.r_tmp + "_" + self.rr_tmp + "_" + self.m_tmp + "_" + self.mr_tmp + ".hist"
        
    def run_nbody(self):
        output_hist = self.hist_tmp
        ft          = self.ft_tmp
        bt          = self.bt_tmp
        r           = self.r_tmp
        rr          = self.rr_tmp
        m           = self.m_tmp
        mr          = self.mr_tmp
        sweep_type  = self.sweep_type
        data_val_file_name   = self.sweep_variables
        
        os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 14 -b -e " + seed + " -i " + ft + " " + bt + " " + r + " " + rr + " " + m + " " + mr + " \
                2>>" + folder + "parameter_sweeps" + sweep_type + "/" + data_val_file_name + ".txt")

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
            
        f.write("%s\t%s \n" % (name1, name2))
        
    def check_interval(self, parameter, counter, interval):
        if(parameter == 'ft'):
            correct = ft_cn
        elif(parameter == 'bt'):
            correct = bt_cn
        elif(parameter == 'r'):
            correct = r_cn
        elif(parameter == 'rr'):
            correct = rr_cn
        elif(parameter == 'm'):
            correct = m_cn
        elif(parameter == 'mr'):
            correct = mr_cn
        
        
        if(counter < correct and counter + interval > correct):
            return True
        else:
            return False
            
            
            
    def run_system(self):
        self.set_hist()
        #self.run_nbody()
        self.write_parameters(self.data_val_file_name, self.parameter1, self.parameter2)

def rebuild():#rebuilds nbody
    os.chdir(".")
    #os.system("rm -r ~/research/nbody_test")
    #os.system("mkdir ~/research/nbody_test")
    os.chdir("../nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../like_surface")

def make_correct(): #makes the correct answer histogram
    os.system(" " + binary + " \
        -f " + lua + " \
        -z " + input_hist + " \
        -b -e " + seed + " -i "+ ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )

def run_sweep(start1, end1, intv1, para1, start2, end2, intv2, para2):#this is a parameter sweep with a regular interval
    counter1 = start1
    counter2 = start2
    name1 = str(counter1)
    name2 = str(counter2)
   
    sweep_type = ""  #sweep name
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_type)
    sweep_variables = para1 + "_" + para2  #name of the files
    hist_path = folder + sweep_variables + "_hists/" + "arg_"
    data_vals   = folder + "parameter_sweeps" + sweep_type + "/" + sweep_variables + "_vals.txt"
    f = open(data_vals, 'w')
    
    do_correct1 = False
    do_correct2 = False
    
    para = parameters(ft_c, bt_c, r_c, rr_c, m_c, mr_c, hist_path, sweep_type, sweep_variables, f, para1, para2)
    
    while counter1 < end1 + intv1:  #this iterates over one parameter on the outside and another on the inside
        para.set_parameter(para1, counter1)

        
        counter2 = start2  #restart the inner parameter iteration from beginning
        while counter2 < end2 + intv2:  #inner loop.
            para.set_parameter(para2, counter2)
            para.run_system()
            
            do_correct2 = para.check_interval(para2, counter2, intv2)#check if correct answer falls between loop intervals
            
            if(do_correct2):  #if the correct answer is between the interval for the inner loop, run the correct answer
                para.set_correct(para2)
                para.run_system()
            
            
            counter2 += intv2  #increment the inner loop value
        
        do_correct1 = para.check_interval(para1, counter1, intv1)
        if(do_correct1):  #if the outer loop correct answer was found in the interval
            para.set_correct(para1)
                
            
            counter2 = start2  #run the same inner loop as above
            while counter2 < end2 + intv2:
                para.set_parameter(para2, counter2)
                para.run_system()
                
                do_correct2 = para.check_interval(para2, counter2, intv2)
                if(do_correct2):  #if the correct answer for the inner loop was found 
                    para.set_correct(para2)
                    para.run_system()
                
                counter2 += intv2  #iterates the inner loop value
        
        counter1 += intv1  #iterates the outer loop value
    f.close()#close the files
    return 0

def random_iteration_sweep(start1, end1, N1, para1, start2, end2, N2, para2):
    counter1 = 0.0
    counter2 = 0.0
    #sweep name
    sweep_type = "_2d_rand_iter"
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_type)
    #name of the files
    sweep_variables = para1 + "_" + para2
    hist_path = folder + sweep_variables + "_hists/" + "arg_"
    data_vals   = folder + "parameter_sweeps" + sweep_type + "/" + sweep_variables + "_vals.txt"
    f = open(data_vals, 'w')
    
    #initialize the parameter class with the correct values
    para = parameters(ft_c, bt_c, r_c, rr_c, m_c, mr_c, hist_path, sweep_type, sweep_variables, f, para1, para2)
    
     #this iterates over one parameter on the outside and another on the inside
    while counter1 < N1:
        
        if(counter1 == 0.0):#since this has random iteration, put the para1 correct value first
            counter2 = 0.0#reset the inner loop counter
            
            while counter2 < N2:#runs the inner loop iteration
                
                if(counter2 == 0.0):#put the correct value for the inner loop first
                    para.run_system()#put para2 correct value first
                
                
                value = random.uniform(0.0, 1.0) * (end2 - start2) + start2  #randomly select a value in the sweep range of inner loop parameter
                
                para.set_parameter(para2, value)#set the second parameter to a random parameter
                para.run_system()#sets the name of the histogram, runs the nbody and writes the parameters used
                
                counter2 += 1 #iterate counter. want a certain number of points
        
        value = random.uniform(0.0, 1.0) * (end1 - start1) + start1  #after putting correct answer, randomly select value from sweep range for outer loop parameter
        
        para.set_parameter(para1, value)
        
        counter2 = 0.0  #reset the counter for the inner loop
        while counter2 < N2:
            if(counter2 == 0.0):#put the correct value for the inner loop first
                para.set_correct(para2)#set the para2 to correct value
                
                para.run_system()
            
            value = random.uniform(0.0, 1.0) * (end2 - start2) + start2 #randomly select a value within the sweep range for the inner loop
           
            para.set_parameter(para2, value)
            para.run_system()
            
            counter2 += 1
        counter1 +=1
        
    f.close()
    return 0



def truly_random_sweep(start1, end1, N1, para1, start2, end2, N2, para2):
    counter = 0.0
    #sweep name
    sweep_type = "_2d_rand_iter"
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_type)
    #name of the files
    sweep_variables = para1 + "_" + para2
    hist_path = folder + sweep_variables + "_hists/" + "arg_"
    
    os.system("mkdir " + folder + "parameter_sweeps" + sweep_type)
    data_vals   = folder + "parameter_sweeps" + sweep_type + "/" + sweep_variables + "_vals.txt"
    f = open(data_vals, 'w')
    
    N = (N1 * N2) 
    para = parameters(ft_c, bt_c, r_c, rr_c, m_c, mr_c, hist_path, sweep_type, sweep_variables, f, para1, para2)
    #run the correct answer first
    para.run_system()
    
    #this iterates over one parameter on the outside and another on the inside
    while counter < N:
        
        value1 = random.uniform(0.0, 1.0) * (end1 - start1) + start1 #randomly select a value within the sweep range for parameter1
        value2 = random.uniform(0.0, 1.0) * (end2 - start2) + start2 #randomly select a value within the sweep range for parameter2
        
        #set both parameters to correct answer
        para.parameter_reset()
        
        
        #set first parameter to random value keeping second as correct
        para.set_parameter(para1, value1)
        para.run_system()
        
        
        #set both parameters to random numbers
        para.set_parameter(para2, value2)
        para.run_system()
        
        #set the first to correct and the second to the random number
        para.set_correct(para1)
        para.run_system()
        
        counter += 1
        
    f.close()
    return 0

def mk_dirs():
    names = [ 'ft_bt', 'ft_rad', 'ft_rr', 'ft_m', 'ft_mr', 'bt_r', 'bt_rr', 'bt_m', 'bt_mr', 'r_rr', 'r_m', 'r_mr', 'rr_m', 'rr_mr', 'm_mr']
    os.system("mkdir 2d_sweep_hists")
    for i in range(0, len(names)):
        os.system("mkdir 2d_sweep_hists/" + names[i] + "_hists")
    return 0


def main():
    if(make_folders):
        mk_dirs()
        
    if(rebuild_binary):
        rebuild()
        
    if(make_correct_answer_hist):
        make_correct()
    
    
    if(run_regular_iteration):
        if(run_ft_v_bt):
            run_sweep(ft_s, ft_e, ft_in, 'ft', bt_s, bt_e, bt_in, 'bt')
        if(run_ft_v_r ):
            run_sweep(ft_s, ft_e, ft_in, 'ft', r_s,  r_e,  r_in,  'r')
        if(run_ft_v_rr):
            run_sweep(ft_s, ft_e, ft_in, 'ft', rr_s, rr_e, rr_in, 'rr')
        if(run_ft_v_m ):
            run_sweep(ft_s, ft_e, ft_in, 'ft', m_s,  m_e,  m_in,  'm')
        if(run_ft_v_mr):
            run_sweep(ft_s, ft_e, ft_in, 'ft', mr_s, mr_e, mr_in, 'mr')
            
        if(run_bt_v_r  ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', r_s,  r_e,  r_in,  'r')
        if(run_bt_v_rr ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', rr_s, rr_e, rr_in, 'rr')
        if(run_bt_v_m  ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', m_s,  m_e,  m_in,  'm')
        if(run_bt_v_mr ):
            run_sweep(bt_s, bt_e, bt_in, 'bt', mr_s, mr_e, mr_in, 'mr')
            
            
        if(run_r_v_rr  ):
            run_sweep(r_s,  r_e,  r_in,  'r',  rr_s, rr_e, rr_in, 'rr')
        if(run_r_v_m   ):
            run_sweep(r_s,  r_e,  r_in,  'r',  m_s,  m_e,  m_in,  'm')
        if(run_r_v_mr  ):
            run_sweep(r_s,  r_e,  r_in,  'r',  mr_s, mr_e, mr_in, 'mr')
            
        if(run_rr_v_m  ):
            run_sweep(rr_s, rr_e, rr_in, 'rr', m_s,  m_e,  m_in,  'm')
        if(run_rr_v_mr ):
            run_sweep(rr_s, rr_e, rr_in, 'rr', mr_s, mr_e, mr_in, 'mr')
            
        if(run_m_v_mr  ):
            run_sweep(m_s,  m_e,  m_in,  'm',  mr_s, mr_e, mr_in, 'mr')
    
    if(run_random_iteration):
        if(run_ft_v_bt):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', bt_s, bt_e, bt_N, 'bt')
        if(run_ft_v_r ):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', r_s,  r_e,  r_N,  'r')
        if(run_ft_v_rr):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', rr_s, rr_e, rr_N, 'rr')
        if(run_ft_v_m ):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', m_s,  m_e,  m_N,  'm')
        if(run_ft_v_mr):
            random_iteration_sweep(ft_s, ft_e, ft_N, 'ft', mr_s, mr_e, mr_N, 'mr')
            
        if(run_bt_v_r  ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', r_s,  r_e,  r_N,  'r')
        if(run_bt_v_rr ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', rr_s, rr_e, rr_N, 'rr')
        if(run_bt_v_m  ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', m_s,  m_e,  m_N,  'm')
        if(run_bt_v_mr ):
            random_iteration_sweep(bt_s, bt_e, bt_N, 'bt', mr_s, mr_e, mr_N, 'mr')
            
            
        if(run_r_v_rr  ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  rr_s, rr_e, rr_N, 'rr')
        if(run_r_v_m   ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  m_s,  m_e,  m_N,  'm')
        if(run_r_v_mr  ):
            random_iteration_sweep(r_s,  r_e,  r_N,  'r',  mr_s, mr_e, mr_N, 'mr')
            
        if(run_rr_v_m  ):
            random_iteration_sweep(rr_s, rr_e, rr_N, 'rr', m_s,  m_e,  m_N,  'm')
        if(run_rr_v_mr ):
            random_iteration_sweep(rr_s, rr_e, rr_N, 'rr', mr_s, mr_e, mr_N, 'mr')
            
        if(run_m_v_mr  ):
            random_iteration_sweep(m_s,  m_e,  m_N,  'm',  mr_s, mr_e, mr_N, 'mr')
     
     
     
    if(run_truly_random_iter):
        truly_random_sweep(rr_s, rr_e, rr_N, 'rr', mr_s, mr_e, mr_N, 'mr')
        
    tmp_sweep_correction()
main()
            
        
#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
from subprocess import call
import random
random.seed(a = 12345678)#lmc
#random.seed(a = 687651463)#teletraan
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])

lmc_dir = '/home/shelts/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = lmc_dir

folder        = path + "like_surface/hists/"
binary        = path + "nbody_test/bin/milkyway_nbody"
#lua           = path + "lua/EMD_v162_bestlike.lua"
lua           = path + "lua/full_control.lua"
seed          = "98213548"

input_hist    = folder + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_correct.hist"
#output_hist   = folder + "histogram_out_20kEMD_sweep.hist"
#parameter    = [start, end, increment]
ft_rg         = [3.0, 5.0, 0.1]#20
bt_rg         = [0.8, 1.2, 0.04]#10
r_rg          = [0.05, 0.5, 0.06]#20
rr_rg         = [0.05, 0.5, 0.05]#17
m_rg          = [1., 60.0, 5]#23
mr_rg         = [.01, .95, .05]#18


ft_N = 50
bt_N = 50
r_N  = 50
rr_N = 50
m_N  = 50
mr_N = 50

y = True
n = False

#choose what to run
make_folders              = y
rebuild_binary            = n
make_correct_answer_hist  = y
run_regular_iteration     = n
run_random_iteration      = y

run_forward_evole_time    = y
run_backward_evolve_ratio = n
run_radius                = y
run_radius_ratio          = y
run_mass                  = y
run_mass_ratio            = y
#--------------------------------------------------------------------------------------------------

def rebuild():
    os.chdir(".")
    #os.system("rm -r ~/research/nbody_test")
    #os.system("mkdir ~/research/nbody_test")
    os.chdir("../nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../like_surface")

#this makes a comparison histogram
def make_correct():
    os.system(" " + binary + " \
        -f " + lua + " \
        -z " + input_hist + " \
        -n 10 -b -e " + seed + " -i "+ ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )

def nbody(output_hist, ft, bt, r, rr, m, mr, file_name, sweep_name):
    os.system(" " + binary + " \
                -f " + lua + " \
                -h " + input_hist + " \
                -z " + output_hist + " \
                -n 10 -b -e " + seed + " -i " + ft + " " + bt + " " + r + " " + rr + " " + m + " " + mr + " \
                2>>" + folder + "parameter_sweeps" + sweep_name + "/" + file_name + ".txt")
    return 0
    
def run_sweep(start, end, intv, para):
    counter = start
    name = str(counter)
    sweep_name = ""
    os.system("mkdir hists/parameter_sweeps" + sweep_name)
    data_vals   = "hists/parameter_sweeps" + sweep_name + "/" + para + "_vals.txt"
    f = open(data_vals, 'a')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    do_correct = False
    
    while counter < end:
        output_hist = folder + para + "_hists/" + "arg_"
        if(para == 'ft'):
            ft_tmp = name
            if(counter < args[0] and counter + intv > args[0]):
                do_correct = True
        elif(para == 'bt'):
            bt_tmp = name
            if(counter < args[1] and counter + intv > args[1]):
                do_correct = True
        elif(para == 'r'):
            r_tmp = name
            if(counter < args[2] and counter + intv > args[2]):
                do_correct = True
        elif(para == 'rr'):
            rr_tmp = name
            if(counter < args[3] and counter + intv > args[3]):
                do_correct = True
        elif(para == 'm'):
            m_tmp = name
            if(counter < args[4] and counter + intv > args[4]):
                do_correct = True
        elif(para == 'mr'):
            mr_tmp = name
            if(counter < args[5] and counter + intv > args[5]):
                do_correct = True
        
        output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
        nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, para, sweep_name)
        f.write("%s \n" % name)
        
        if(do_correct == True):
            output_hist = folder + para + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
            nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, para, sweep_name)
            do_correct = False
            
            if(para == 'ft'):
                f.write("%s \n" % ft_c)
            elif(para == 'bt'):
                f.write("%s \n" % bt_c)
            elif(para == 'r'):
                f.write("%s \n" % r_c)
            elif(para == 'rr'):
                f.write("%s \n" % rr_c)
            elif(para == 'm'):
                f.write("%s \n" % m_c)
            elif(para == 'mr'):
                f.write("%s \n" % mr_c)
                
        counter += intv
        name = str(counter)
    f.close()   
    return 0
        
def run_sweep_random_iter(start, end, N, para):
    counter = 0.0
    sweep_name = "_rand_iter"
    os.system("mkdir " + path + "like_surface/hists/parameter_sweeps" + sweep_name)
    data_vals   = path + "like_surface/hists/parameter_sweeps" + sweep_name + "/" + para + "_vals.txt"
    f = open(data_vals, 'w')
    
    ft_tmp = ft_c
    bt_tmp = bt_c
    r_tmp  = r_c
    rr_tmp = rr_c
    m_tmp  = m_c
    mr_tmp = mr_c
    
    #get the correct answer hist
    output_hist = folder + para + "_hists/" + "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + ".hist"
    nbody(output_hist, ft_c, bt_c, r_c, rr_c, m_c, mr_c, para, sweep_name)
    
    while counter < N:
        output_hist = folder + para + "_hists/" + "arg_"
        name = random.uniform(0.0, 1.0) * (end - start) + start
        name = str(name)
        
        if(para == 'ft'):
            ft_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % ft_c)
        elif(para == 'bt'):
            bt_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % bt_c)
        elif(para == 'r'):
            r_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % r_c)
        elif(para == 'rr'):
            rr_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % rr_c)
        elif(para == 'm'):
            m_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % m_c)
        elif(para == 'mr'):
            mr_tmp = name
            if(counter == 0.0):
                f.write("%s \n" % mr_c)
            
        output_hist += ft_tmp + "_" + bt_tmp + "_" + r_tmp + "_" + rr_tmp + "_" + m_tmp + "_" + mr_tmp + ".hist"
        nbody(output_hist, ft_tmp, bt_tmp, r_tmp, rr_tmp, m_tmp, mr_tmp, para, sweep_name)  
        f.write("%s \n" % name)
        counter += 1
    f.close()    
    return 0

def mk_dirs():
    names   = ['ft', 'bt', 'r', 'rr', 'm', 'mr']
    os.chdir(path + "like_surface")
    os.system("mkdir hists")
    for i in range(0, len(names)):
        os.system("mkdir hists/" + names[i] + "_hists")
    return 0

def main():
    if(make_folders):
        mk_dirs()
    
    if(rebuild_binary):
        rebuild()
        
    if(make_correct_answer_hist):
        make_correct()
    
    
    if(run_regular_iteration):
        if(run_forward_evole_time):
            run_sweep(ft_rg[0], ft_rg[1], ft_rg[2], 'ft')
        
        if(run_backward_evolve_ratio):
            run_sweep(bt_rg[0], bt_rg[1], bt_rg[2], 'bt')
            
        if(run_radius):
            run_sweep(r_rg[0], r_rg[1], r_rg[2], 'r')
            
        if(run_radius_ratio):
            run_sweep(rr_rg[0], rr_rg[1], rr_rg[2], 'rr')
            
        if(run_mass):
            run_sweep(m_rg[0], m_rg[1], m_rg[2], 'm')
            
        if(run_mass_ratio):
            run_sweep(mr_rg[0], mr_rg[1], mr_rg[2], 'mr')
         
         
    if(run_random_iteration):
        if(run_forward_evole_time):
            run_sweep_random_iter(ft_rg[0], ft_rg[1], ft_N, 'ft')
    
        if(run_backward_evolve_ratio):
            run_sweep_random_iter(bt_rg[0], bt_rg[1], bt_N, 'bt')
         
        if(run_radius):
            run_sweep_random_iter(r_rg[0], r_rg[1], r_N, 'r')
         
        if(run_radius_ratio):
            run_sweep_random_iter(rr_rg[0], rr_rg[1], rr_N, 'rr')
         
        if(run_mass):
            run_sweep_random_iter(m_rg[0], m_rg[1], m_N, 'm')
         
        if(run_mass_ratio):
            run_sweep_random_iter(mr_rg[0], mr_rg[1], mr_N, 'mr')
            
    return 0
    
main()
#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # # # #\#
                #    It began with a search.        #
                #\# # # # # # # # # # # # # # # # #/#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import subprocess
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib import cm
import math as mt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np
import scipy
import random
random.seed(a = 12345678)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

args = [3.95, 0.98, 0.2, 0.2, 12, 0.2]

ft_c  = str(args[0])
bt_c  = str(args[1])
r_c   = str(args[2])
rr_c  = str(args[3])
m_c   = str(args[4])
mr_c  = str(args[5])

lmc_dir = '~/research/'
sid_dir = '/home/sidd/Desktop/research/'
path = sid_dir

folder        = path + "like_surface/hists/"
binary        = path + "nbody_test/bin/milkyway_nbody"

correct_hist  = "arg_" + ft_c + "_" + bt_c + "_" + r_c + "_" + rr_c + "_" + m_c + "_" + mr_c + "_2kcorrect"


lua = "EMD_v162.lua"
ver = ""

#switches#
rebuild_binary  = n
make_corr_hist  = n
run_test        = n
run_conj_grad_desc = y


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # #    
def rebuild():
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=ON -DNBODY_STATIC=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
# # # # # # # # # #   


def make_correct():
    os.system(" " + binary + " \
        -f " + path + "lua/" + lua + " \
        -z " + path + "quick_plots/hists/" + correct_hist + " \
        -b -i " + ft_c + " " + bt_c + " " + r_c + " " + rr_c + " " + m_c + " " + mr_c )


def nbody(paras, hist):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
    
    
    os.chdir("nbody_test/bin/")
    os.system("./milkyway_nbody" + ver + " \
        -f " + path + "lua/" + lua + " \
        -h " + path + "quick_plots/hists/" + correct_hist + ".hist \
        -z " + path + "quick_plots/hists/" + hist + ".hist \
        -o " + path + "quick_plots/outputs/" + hist + ".out \
        -n 12 -b -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " \
        2>> " + hist + "_piped.out")
    os.chdir(path)

def get_value(name):
    f = open("nbody_test/bin/" + name + "_piped.out", 'r')
    for line in f:
        if (line.startswith("<")):
            ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
            tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
            l = float(tt[0])
    return l
    
def function(parameters):
    ft = str(parameters[0])
    bt = str(parameters[1])
    r  = str(parameters[2])
    rr = str(parameters[3])
    m  = str(parameters[4])
    mr = str(parameters[5])
    
    name = ft + "_" + bt + "_" + r + "_" + rr + "_" + m + "_" + mr
    nbody(parameters, name)
    val = get_value(name)
    
    return -val


def initial_guess():
    ft_rg         = [3.0, 5.0]
    bt_rg         = [0.8, 1.2]
    r_rg          = [0.1, 1.3]
    rr_rg         = [0.1, .95]
    m_rg          = [1., 120.]
    mr_rg         = [.01, .95]
    
    ft_0 = random.uniform(0.0, 1.0) * (ft_rg[1] - ft_rg[0]) + ft_rg[0]
    bt_0 = random.uniform(0.0, 1.0) * (bt_rg[1] - bt_rg[0]) + bt_rg[0]
    r_0  = random.uniform(0.0, 1.0) * (r_rg[1]  - r_rg[0])  + r_rg[0]
    rr_0 = random.uniform(0.0, 1.0) * (rr_rg[1] - rr_rg[0]) + rr_rg[0]
    m_0  = random.uniform(0.0, 1.0) * (m_rg[1]  - m_rg[0])  + m_rg[0]
    mr_0 = random.uniform(0.0, 1.0) * (mr_rg[1] - mr_rg[0]) + mr_rg[0]
    
    x0 = [ft_0, bt_0, r_0, rr_0, m_0, mr_0]
    return x0
        
def test():
    #val = function(args)
    #print val
    para = [3.40374881598597, 0.932995970998994, 0.283776750505688, 0.804446363133715, 6.9121529340563, 0.714150034261106]
    val = function(para)
    print("%0.15f\n" % val)
    return 0


def f(x, *args):
    u, v = x
    a, b, c, d, e, f = args
    return a*u**2 + b*u*v + c*v**2 + d*u + e*v + f


def main():
    from scipy import optimize
    if(rebuild_binary):
        rebuild()
        
    if(make_corr_hist):
        make_correct()
        
    if(run_conj_grad_desc):
        x0 = initial_guess()
        res1 = scipy.optimize.fmin_cg(function, x0, full_output = True)
        print res1
    
    if(run_test):
        args = (2, 3, 7, 8, 9, 10)
        #test()
        x0 = np.asarray((7, 2))  # Initial guess.
        res1 = optimize.fmin_cg(f, x0, args=args, full_output = True)
        print res1
main()
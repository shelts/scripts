#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#######################################################################
#    LIBRARY   #
#args = [3.945, 0.9862, 0.2, 0.2, 12, 0.2] #for hist with dark matter
args = [4, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

bodies = ['10000', '15000', '20000', '25000', '30000', '35000', '40000', '45000', '50000', '55000', '60000', '65000']
#bodies = ['20000']
N = 12
seeds = ['7539621', '9384671']
n_seeds = 2
y = True
n = False

#    SWITCHES  #
run_nbody = n
remake    = n
match_histograms = n
cross_compare = n
make_plots = y
prefix = "4gy"
lua = "EMD_154_alternating_bodies.lua"
#######################################################################

if(remake == True):
    os.chdir("./")
    os.system("rm -r nbody_test")
    os.system("mkdir nbody_test")
    os.chdir("nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../")
for i in range(0,N):
    if(run_nbody == True):
        print('running nbody')
        for j in range (0,n_seeds):
            histogram_for_nbody_run = prefix + bodies[i] + "_bodies_seed_" + seeds[j] + ".hist"
            
            os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
                -f ~/Desktop/research/lua/" + lua + " \
                -z ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + histogram_for_nbody_run + " \
                -o ~/Desktop/research/quick_plots/hists_outputs_bodytest/out.out \
                -n 8 -e " + seeds[j] + " -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " " + bodies[i] )

    if(match_histograms == True):
        match_hist_correct = prefix + bodies[i] + "_bodies_seed_" + seeds[0] + ".hist"
        match_hist_compare = prefix + bodies[i] + "_bodies_seed_" + seeds[1] + ".hist"
        
        os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -h ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + match_hist_correct + "\
        -s ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + match_hist_compare + "\
        2>>~/Desktop/research/quick_plots/" + prefix + "bodies_seed_test.txt")

if(cross_compare == True):
    for i in range(0,N):
        if(match_histograms == True):
            match_hist_correct = prefix + bodies[i] + "_bodies_seed_" + seeds[0] + ".hist"
            match_hist_compare = prefix + bodies[i] + "_bodies_seed_" + seeds[1] + ".hist"
            
            os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
            -h ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + prefix + "65000_bodies_seed_" + seeds[0] + ".hist \
            -s ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + match_hist_compare + "\
            2>>~/Desktop/research/quick_plots/" + prefix + "bodies_seed_test_compared_to_65k.txt")
            
            os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
            -h ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + prefix + "50000_bodies_seed_" + seeds[0] + ".hist \
            -s ~/Desktop/research/quick_plots/hists_outputs_bodytest/" + match_hist_compare + "\
            2>>~/Desktop/research/quick_plots/" + prefix + "bodies_seed_test_compared_to_50k.txt")
 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(make_plots == True):
    lines = open('./quick_plots/' + prefix + 'bodies_seed_test.txt').readlines()
    lines = lines[0:len(lines)]
    likes = []
    for line in lines:
        tokens = line.split()
        if tokens:
            l = float(tokens[0])
            likes.append(l)
            print(l)


    bods = []    
    for i in range(0,N):
        b = float(bodies[i])
        bods.append(b)
        
    print(len(likes), len(bods))           
    
    plt.plot(bods, likes, label="compared to same bodies")
    legend = plt.legend(loc='upper center', shadow=True)
    plt.title('seed body test')
    plt.xlabel('bodies')
    #plt.ylim((.0002, .002))
    plt.ylabel('likelihood')
    plt.savefig('./quick_plots/' + prefix + 'seed_body_test.png', format='png')


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    lines = open('./quick_plots/' + prefix + 'bodies_seed_test_compared_to_65k.txt').readlines()
    lines = lines[0:len(lines)]
    likes = []
    for line in lines:
        tokens = line.split()
        if tokens:
            l = float(tokens[0])
            likes.append(l)
            print(l)


    bods = []    
    for i in range(0,N):
        b = float(bodies[i])
        bods.append(b)
        
    print(len(likes), len(bods))           
    
    plt.plot(bods, likes, label = "compared to 65k")
    legend = plt.legend(loc='upper right', shadow=True)
    plt.title('seed body test')
    plt.xlabel('bodies')
    #plt.ylim((.0002, .002))
    plt.ylabel('likelihood')
    plt.savefig('./quick_plots/' + prefix + 'seed_body_test_cmp_to_65k.png', format='png')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    lines = open('./quick_plots/' + prefix + 'bodies_seed_test_compared_to_50k.txt').readlines()
    lines = lines[0:len(lines)]
    likes = []
    for line in lines:
        tokens = line.split()
        if tokens:
            l = float(tokens[0])
            likes.append(l)
            print(l)


    bods = []    
    for i in range(0,N):
        b = float(bodies[i])
        bods.append(b)
        
    print(len(likes), len(bods))           
    
    plt.plot(bods, likes, label = "compared to 50k")
    legend = plt.legend(loc='upper right', shadow=True)
    plt.title(' 2D 0gy seed body test')
    plt.xlabel('bodies')
    #plt.ylim((.0002, .002))
    plt.ylabel('likelihood')
    plt.savefig('./quick_plots/' + prefix + 'seed_body_test_cmp_to_50k.png', format='png')
    plt.show()



#os.system("mv ./quick_plots/" + prefix + "bodies_seed_test_compared_to_65k.txt ./quick_plots/" + prefix + "bodies_seed_test_compared_to_50k.txt ./quick_plots/" + prefix + "bodies_seed_test.txt ./quick_plots/hists_outputs_bodytest/2d_4gy")




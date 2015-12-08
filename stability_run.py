#! /usr/bin/python
import os
#from subprocess import call

args = [0.9862, 0.2, 0.25, 60, .2]

sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
N               = 8
M               = 0
back_time       = str(args[0])
r0              = str(args[1])
light_r_ratio   = str(args[2])
mass            = str(args[3])
mass_ratio      = str(args[4])

y = True
n = False

rebuild = n
run = y
if(rebuild == True):
    os.system("rm -r nbody_test")
    os.system("mkdir nbody_test")
    os.chdir("nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../")

if(run == True):
    for i in range(M, N):
        os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
            -f ~/Desktop/research/lua/Null.lua \
            -o ~/Desktop/research/data_testing/sim_outputs/output_" + (ext[i]) + "gy.out \
            -n 8 -x -e 27744245 -i "+ str(sim_time[i]) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )

os.chdir("data_testing")    
os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio)
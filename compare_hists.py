#! /usr/bin/python
import os
#from subprocess import call

args = [1, 0.2, 0.2, 11, 0.2]

sim_time      = [0.0001, 0.0001, 4, 4]
#sim_time      = [4, 4]
N             = 2
back_time     = str(args[0])
r0            = str(args[1])
light_r_ratio = str(args[2])
mass          = str(args[3])
mass_ratio    = str(args[4])


os.system("rm -r nbody_test")
os.system("mkdir nbody_test")
os.chdir("nbody_test")
os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
os.system("make -j ")
os.chdir("../")

#file:///home/sidd/Desktop/research/lua/Null_even.lua
#file:///home/sidd/Desktop/research/lua/EMD_20k_isotropic_1_52.lua
#same seed:
for i in range(0, N):
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/EMD_20k_isotropic_1_52.lua \
        -h ~/Desktop/research/histogram_20kEMD_v150_" + str(i-1) +".hist \
        -z ~/Desktop/research/histogram_20kEMD_v150_" + str(i) +".hist \
        -n 4 -P -x -e  7584962 -i "+ str(sim_time[i]) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
        2>>~/Desktop/research/piped_output.txt")


###diff seed
#for i in range(0, N):
    #os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        #-f ~/Desktop/research/lua/EMD_20k_isotropic_1_52.lua \
        #-h ~/Desktop/research/histogram_20kEMD_v150_" + str(i-1) +".hist \
        #-z ~/Desktop/research/histogram_20kEMD_v150_" + str(i) +".hist \
        #-n 4 -P -x  -i "+ str(sim_time[i]) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio + " \
        #2>>~/Desktop/research/piped_output.txt")


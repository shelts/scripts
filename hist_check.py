#! /usr/bin/python
import os
from subprocess import call

args = [4, 0.6, 0.2, 0.2, 11, 0.2]


sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

print "parameters: ", back_time, r0, light_r_ratio, mass, mass_ratio
run_nbody = False
plot_hist = True

histogram = "tidal_histogram.hist"
data2 = "Orphan_Data_September_2014.hist"
data = "data.hist"
#######################################################################

if(run_nbody == True):
    os.chdir("./")
    os.system("rm -r nbody_test")
    os.system("mkdir nbody_test")
    os.chdir("nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../")
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/EMD_20k_isotropic_1_54.lua \
        -z ~/Desktop/research/quick_plots/" + histogram + " \
        -n 8 -x -e 27744245 -i "+ (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )
    
    
    
if(plot_hist == True):
    f = open('histogram_check.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'beta'\n")
    f.write("set xlabel 'lambda'\n")
    #f.write("set xrange[-50:50]\n")
    #f.write("set yrange[0:.15]\n\n\n")
    f.write("set pm3d map\n")
    f.write("set output \"~/Desktop/research/quick_plots/hist_check.jpeg\" \n")
    f.write("set title 'Histogram of Light Matter Distribution After 4 Gy' \n")
    f.write("splot 'quick_plots/" + histogram + "' using 2:3:4 \n\n") 


    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot histogram_check.gnuplot")
    #os.system("rm histogram_check.gnuplot")
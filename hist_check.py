#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
args = [3.9, 1, 0.2, .2, 60, 0.2]

counts = [150, 0, 0, 0, 275, 150, 100, 75, 110, 110, 100, 110, 100, 120, 110, 150, 130, 75, 150, 100, 50, 50, 0, 20, 20]
sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

print "parameters: ", back_time, r0, light_r_ratio, mass, mass_ratio
y = True
n = False

run_nbody = y
remake    = n

run_single_plum = n
remake_single   = n

plot_hist            = y
plot_distruption_map = y
make_data_hist       = y

histogram = "tidal_histogram.hist"
histogram_single = "tidal_histogram_single_plummer.hist"
data2 = "Orphan_Data_September_2014.hist"
data = "data.hist"
blank = "none.hist"
#######################################################################

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(run_nbody == True):
    print('running nbody')
    if(remake == True):
        os.chdir("./")
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/EMD_20k_isotropic_1_54.lua \
        -z ~/Desktop/research/quick_plots/hists_outputs/" + histogram + " \
        -o ~/Desktop/research/quick_plots/hists_outputs/out.out \
        -n 8 -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if(run_single_plum == True):
    print('running single plummer nbody')
    back_time = "1"
    r0 = "0.2"
    mass = "11"
    if(remake_single == True):
        os.chdir("./")
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
        -f ~/Desktop/research/lua/single_plum_EMD_20k_isotropic_1_54.lua \
        -z ~/Desktop/research/quick_plots/hists_outputs/" + histogram_single + " \
        -n 8 -x -e  961694  -i "+ sim_time + " " + back_time + " " + r0 + " " + mass)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if(make_data_hist == True):
    g = open("quick_plots/hists_outputs/" + data, 'w')
    lamb = 32 + 5
    total = 0.0
    for i in range(0, len(counts)):
        total = total + counts[i]
    total = total * 5.0 / 222288.24  #each count is fturn off star which reps about a cluster of 5 solar masses
    for i in range(0, len(counts)):
        bodies = counts[i] * 5.0 / 222288.24
        g.write("%f \t %f\n" % (lamb, bodies / total ))
        lamb = lamb - 3
    g.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_hist == True):
    lines = []
    lines = open('quick_plots/hists_outputs/' + histogram).readlines();
    lines = lines[40:len(lines)]
    sim_l = []
    sim_n = []
    for line in lines:
        tokens = line.split();
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            cts = float(tokens[3])
            sim_l.append(lda)
            sim_n.append(cts)

    lines = []
    lines = open('quick_plots/hists_outputs/' + data2).readlines();
    lines = lines[5:len(lines)]
    data_l = []
    data_n = []
    for line in lines:
        tokens = line.split()
        if tokens:
            dat_l = float(tokens[1])
            dat_n = float(tokens[3])
            data_l.append(dat_l)
            data_n.append(dat_n)
    
    
    #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
    plt.subplot(211)
    plt.bar(sim_l, sim_n, width=1, color='b')
    plt.legend("sim")
    plt.title('Histogram of Light Matter Distribution After 4 Gy')
    plt.xlim((40, -40))
    plt.ylim((0.0, 0.15))
    plt.ylabel('counts')
    
    plt.subplot(212)
    plt.bar(data_l, data_n, width=1, color='k')
    plt.legend("d")
    plt.xlim((40, -40))
    plt.ylim((0.0, 0.15))
    plt.xlabel('l')
    plt.ylabel('counts')
    #f.subplots_adjust(hspace=0)
    plt.savefig('quick_plots/hist', format='png')
    #plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if(plot_distruption_map == True):
    f = open('quick_plots/histogram_check.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'beta'\n")
    f.write("set xlabel 'lambda'\n")
    f.write("set xrange[180:-180]\n")
    f.write("set yrange[-20:20]\n\n\n")
    f.write("set pm3d map\n")
    f.write("set output \"~/Desktop/research/quick_plots/hist_check.png\" \n")
    f.write("set title 'Histogram of Light Matter Distribution After 4 Gy' \n")
    f.write("plot 'quick_plots/hists_outputs/" + histogram + "' using 2:3:4 with image \n\n") 


    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")

    f.close()
    
    #lines = []
    #lines = open('quick_plots/hists_outputs/' + histogram).readlines();
    #lines = lines[40:len(lines)]
    #sim_l = []
    #sim_b = []
    #sim_n = []
    #for line in lines:
        #tokens = line.split();
        #if tokens: #tests to make sure tokens is not empty
            #lda = float(tokens[1])
            #bta = float(tokens[2])
            #cts = float(tokens[3])
            #sim_l.append(lda)
            #sim_b.append(bta)
            #sim_n.append(cts)
            
    #plt.pcolor(sim_l, sim_b, sim_n, cmap='RdBu')
    #plt.legend("d")
    #plt.xlim((180, -180))
    #plt.ylim((-40, 40))
    #plt.xlabel('l')
    #plt.ylabel('b')
    #plt.colorbar()
    ##f.subplots_adjust(hspace=0)
    #plt.savefig('quick_plots/hist', format='png')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
os.system("gnuplot ./quick_plots/histogram_check.gnuplot")
os.system("rm ./quick_plots/histogram_check.gnuplot")
os.chdir("./quick_plots")
os.system("python lb_plot.py hists_outputs/out.out")
os.chdir("../")
#os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio)
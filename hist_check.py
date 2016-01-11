#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#######################################################################
#    LIBRARY   #
#args = [3.945, 0.9862, 0.2, 0.25, 12, 1]
args = [3.945, 0.9862, 0.2, 0.25, 12, 0.2] #for hist with dark matter
#args = [2.05710712777658, 0.979670310788359, 0.466870336798855, 0.799794703757613, 70.7842113426619, 0.167724983660806]
#data from orphan stream paper. approximate counts
counts = [150, 0, 0, 0, 275, 150, 100, 75, 110, 110, 100, 110, 100, 120, 110, 150, 130, 75, 150, 100, 50, 50, 0, 20, 20]

sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass          = str(args[4])
mass_ratio    = str(args[5])

#print "parameters: ", back_time, r0, light_r_ratio, mass, mass_ratio
y = True
n = False

run_nbody = n
remake    = n

run_single_plum = n
remake_single   = n

plot_nbody_hist      = n
plot_distruption_map = n
make_1d_data_hist    = n
make_2d_data_hist    = n
match_histograms     = y


histogram_all_light_1d = "hist_all_light.hist"
histogram_all_light_2d = "hist_all_light_2d.hist"

histogram_mw_1d_3 = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_ml12_mlmdr0p25.hist" #histogram up on MW_but with different parameter structure
histogram_mw_1d_2 = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_ml12_mr0p2.hist"
histogram_mw_1d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_m60_mr0p2.hist" #histogram up on MW

histogram_mw_2d = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_m60_mr0p2_2D.hist" #histogram up on MW

histogram_best_fit_1d = "best_fit_parameter_hist.hist" #best fit para hist from MW
histogram_best_fit_2d = "best_fit_parameter_hist_2d.hist" #best fit para hist from MW

histogram_2dpara = "histogram_in_seed98213548_20kEMD_2_1_p5_p2_30_p2.hist" #one used in 2d sweeps
#histogram = "tidal_histogram.hist"

data = "Orphan_Data_September_2014.hist"

data_1d = "data_1d.hist"
data_2d = "data_2d.hist"

#names for the histograms below
histogram_for_nbody_run = histogram_mw_1d_2

disruption_hist = histogram_mw_2d

plot_hist1 = histogram_mw_1d
plot_hist2 = data_1d

match_hist_correct = histogram_mw_1d
match_hist_compare = histogram_mw_1d_2

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
        -f ~/Desktop/research/lua/EMD_20k_isotropic_1_54_npa.lua \
        -z ~/Desktop/research/quick_plots/hists_outputs/" + histogram_for_nbody_run + " \
        -o ~/Desktop/research/quick_plots/hists_outputs/out.out \
        -n 8 -e 123124 -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(run_single_plum == True):
    histogram_single = "tidal_histogram_single_plummer.hist"
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

if(make_1d_data_hist == True):
    g = open("quick_plots/hists_outputs/" + data_1d, 'w')
    
    lambda_start = 37 #where the data starts in lambda
    lambda_bin_size = 3.0 #how far apart the data seems
    n_lambda = float(len(counts)) #number of data bins
    n = 50 #number of bins for histrogram file match
    beta_start = -40 #where beta starts for histrogram file
    beta_bin_size = 80#number of bins for histogram match file
    
    total = 0.0
    #get the total counts:
    for i in range(0, int(n_lambda)):
        total = total + counts[i]
    total = total * 5.0 / 222288.24  #each count is fturn off star which reps about a cluster of 5 solar masses
    
    #this follows the format of the histrograms
    g.write("#\n\
# Generated Sun Nov 29 22:13:36 2015\n\
#\n\
# (phi,   theta,  psi) = (128.790000, 54.390000, 90.700000)\n\
# (lambdaStart, lambdaCenter, lambdaEnd) = (" + str(-lambda_start) + ", 0.000000, " + str(lambda_start) + ")\n\
# (betaStart, betaCenter, betaEnd) = (" + str(beta_start) + ", 0.000000, " + str(-beta_start) + ")\n\
# Lambda Bin size = " + str(lambda_bin_size) + "\n\
# Beta Bin size = " + str(beta_bin_size) + "\n\
#\n\
#\n\
# Nbody = 50000\n\
# Evolve time = 3.945000\n\
# Timestep = 0.000514\n\
# Sun GC Dist = 8.000000\n\
# Criterion = NewCriterion\n\
# Theta = 1.000000\n\
# Quadrupole Moments = true\n\
# Eps = 0.000481\n\
#\n\
#\n\
# Potential: (Milkyway@Home N-body potential)\n\
#\n\
# Disk: MiaymotoNagai\n\
#   mass = 445865.888000\n\
#   a = 6.500000\n\
#   b = 0.260000\n\
#\n\
# Halo: Logarithmic\n\
#   vhalo = 73.000000\n\
#   d = 12.000000\n\
#\n\
#\n\
# UseBin  Lambda  Beta  Probability  Error\n\
#\n\
\n\
n = 50000\n\
massPerParticle = 0.0002400000\n\
totalSimulated = 50000\n\
lambdaBins = " + str(n) + "\n\
betaBins = 1\n")
    
    for i in range(0, int(n_lambda)):
        bodies = counts[i] * 5.0 / (222288.24  * total)#this is N
        g.write("%r %f %f %f %f\n" % (1, lambda_start, 0.0, bodies, 0.0))
        lambda_start = lambda_start - lambda_bin_size
        
    g.close()
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     
if(make_2d_data_hist == True):
    g = open("quick_plots/hists_outputs/" + data_2d, 'w')
    
    lambda_start = 37#where the data starts in lambda
    lambda_bin_size = 3.0#how far apart the data seems
    n_lambda = float(len(counts))#number of data bins
    
    stream_width = 5.0 #width of the stream
    beta_start = -(stream_width / 2.0) #where beta starts 
    beta_bin_size = 0.01 #beta bin size
    n_beta = stream_width / beta_bin_size #number of beta bins
    #print(n_beta)
    #Gaussian parameters
    c = 1.0
    b = 0.0

    total = 0.0
    pi = math.pi
    diff = 0.0
    #get the total counts:
    for i in range(0, int(n_lambda)):
        total = total + counts[i]
    total = total * 5.0 / 222288.24  #each count is fturn off star which reps about a cluster of 5 solar masses
    #this follows the format of the histrograms
    g.write("#\n\
# Generated Sun Nov 29 22:13:36 2015\n\
#\n\
# (phi,   theta,  psi) = (128.790000, 54.390000, 90.700000)\n\
# (lambdaStart, lambdaCenter, lambdaEnd) = (" + str(-lambda_start) + ", 0.000000, " + str(lambda_start) + ")\n\
# (betaStart, betaCenter, betaEnd) = (" + str(beta_start) + ", 0.000000, " + str(-beta_start) + ")\n\
# Lambda Bin size = " + str(lambda_bin_size) + "\n\
# Beta Bin size = " + str(beta_bin_size) + "\n\
#\n\
#\n\
# Nbody = 50000\n\
# Evolve time = 3.945000\n\
# Timestep = 0.001200\n\
# Sun GC Dist = 8.000000\n\
# Criterion = NewCriterion\n\
# Theta = 1.000000\n\
# Quadrupole Moments = true\n\
# Eps = 0.000481\n\
#\n\
#\n\
# Potential: (Milkyway@Home N-body potential)\n\
#\n\
# Disk: MiaymotoNagai\n\
#   mass = 445865.888000\n\
#   a = 6.500000\n\
#   b = 0.260000\n\
#\n\
# Halo: Logarithmic\n\
#   vhalo = 73.000000\n\
#   d = 12.000000\n\
#\n\
#\n\
# UseBin  Lambda  Beta  Probability  Error\n\
#\n\
\n\
n = 50000\n\
massPerParticle = 0.0002400000\n\
totalSimulated = 50000\n\
lambdaBins = 50\n\
betaBins = 50\n")
    
    for i in range(0, int(n_lambda)):
        bodies = counts[i] * 5.0 / (222288.24  * total)#this is N
        coeff = bodies / ( c * math.sqrt(2.0 * pi))
        beta = beta_start
        total_n = 0.0
        for j in range(0, int(n_beta)):
            n = coeff * math.exp( - (beta - b)**2.0 / (2.0 * c)) * beta_bin_size
            total_n = total_n + n
            g.write("%r %f %f %f %f\n" % (1, lambda_start, beta, n, 0.0))
            beta = beta + beta_bin_size
        lambda_start = lambda_start - lambda_bin_size
        
        diff = diff + (bodies - total_n)**2 #sum of the differences

    stdev = math.sqrt( diff / n_lambda)#to make sure the dist integrates to original value
    #print(stdev)
    g.close()
    
    f = open('hist_data.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal wxt persist\n")
    f.write("set key on\n")
    f.write("set ylabel 'beta'\n")
    f.write("set xlabel 'lambda'\n")
    f.write("set xrange[40:-40]\n")
    f.write("set yrange[" + str(-beta_start) + ":" + str(beta_start) + "]\n")
    #f.write("set zrange[0:0.01]\n\n\n")

    f.write("set output \"~/Desktop/research/quick_plots/hist_data.png\" \n")
    f.write("set title '' \n")
    f.write("splot './quick_plots/hists_outputs/" + data_2d + "' u 2:3:4  w boxes title 'hist' \n\n", )
    os.system("gnuplot hist_data.gnuplot")
    #os.system("rm hist_data.gnuplot")
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_nbody_hist == True):
    print("making histogram")
    lines = []
    lines = open('quick_plots/hists_outputs/' + plot_hist1).readlines();
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
    lines = open('quick_plots/hists_outputs/' + plot_hist2).readlines();
    lines = lines[40:len(lines)]
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
    plt.xlim((140, -140))
    plt.ylim((0.0, 0.15))
    plt.ylabel('counts')
    
    plt.subplot(212)
    plt.bar(data_l, data_n, width=1, color='k')
    plt.legend("d")
    plt.xlim((140, -140))
    plt.ylim((0.0, 0.15))
    plt.xlabel('l')
    plt.ylabel('counts')
    #f.subplots_adjust(hspace=0)
    plt.savefig('quick_plots/hist', format='png')
    #plt.show()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
if(plot_distruption_map == True):
    print("plotting distruption map")
    f = open('quick_plots/histogram_distrupt.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'beta'\n")
    f.write("set xlabel 'lambda'\n")
    f.write("set xrange[180:-180]\n")
    f.write("set yrange[-20:20]\n\n\n")
    f.write("set pm3d map\n")
    f.write("set output \"~/Desktop/research/quick_plots/distruption.png\" \n")
    f.write("set title 'Histogram of Light Matter Distribution After 4 Gy' \n")
    f.write("plot 'quick_plots/hists_outputs/" + disruption_hist + "' using 2:3:4 with image \n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  \n")
    f.close()
    
    os.system("gnuplot ./quick_plots/histogram_distrupt.gnuplot")
    os.system("rm ./quick_plots/histogram_distrupt.gnuplot")
    
    distrupt_pyplot = n
    if(distrupt_pyplot == True):
        lines = []
        lines = open('quick_plots/hists_outputs/' + histogram).readlines();
        lines = lines[40:len(lines)]
        sim_lx = []
        sim_by = []
        sim_nz = []
        for line in lines:
            tokens = line.split();
            if tokens: #tests to make sure tokens is not empty
                lda = float(tokens[1])
                bta = float(tokens[2])
                cts = float(tokens[3])
                sim_lx.append(lda)
                sim_by.append(bta)
                sim_nz.append(cts)
        print("%f \t %f \t %f\n" % (len(sim_lx), len(sim_by), len(sim_nz)))
        
        sim_l = np.asarray(sim_lx)
        sim_b = np.asarray(sim_by)
        sim_n = np.asarray(sim_nz)
        
        nx = sim_l.max() - sim_l.min() + 1
        ny = sim_b.max() - sim_b.min() + 1
        Z = np.zeros((nx,ny)) 
        print("%f \n" % (Z.shape[0]))
        
        assert sim_l.shape == sim_b.shape == sim_n.shape
        for i in range(len(sim_l)):
            Z[sim_l[i] - sim_l.min()][sim_b[i] - sim_b.min()] = sim_n[i] 

        fig = plt.figure()
        plt.scatter(sim_l, sim_b, c=sim_n)
        #plt.show()
        
        plt.pcolor(np.arange(nx), np.arange(ny), Z, cmap = plt.cm.Reds)
        plt.colorbar()
        plt.xlim(0, sim_l.max() - sim_l.min())
        plt.ylim(0, sim_b.max() - sim_b.min())
        
        xlabels = np.arange(sim_l.min(), sim_l.max(), Nspacingx) # define Nspacing accordingly 
        ylabels = np.arange(sim_b.min(), sim_b.max(), Nspacingy) 
        plt.xticks(np.arange(0, sim_l.max() - sim_l.min(), Nspacingx), xlabels)
        plt.yticks(np.arange(0, sim_b.max() - sim_b.min(), Nspacingy), ylabels)

        plt.savefig('quick_plots/distruption2.png', format='png')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
os.chdir("./quick_plots")
os.system("python lb_plot.py hists_outputs/out.out")
os.chdir("../")
#os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio)

if(match_histograms == True):
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
    -h ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_correct + "\
    -s ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_compare)
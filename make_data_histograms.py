#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
#######################################################################
#This script creates the data histograms, both 1d and 2d
#    LIBRARY   #
y = True
n = False

#    SWITCHES  #
make_1d_data_hist = y
make_2d_data_hist = y
match_histograms  = y
#    Histogram names     #
data = "Orphan_Data_September_2014.hist"

data_1d = "data_1d.hist"
data_2d = "data_2d.hist"


#    histograms for runs #
match_hist_correct = data_1d
match_hist_compare = data_2d

seed = '379780525'
lua = "EMD_20k_1_54.lua"
#######################################################################

#data from orphan stream paper. approximate counts
counts = [150, 0, 0, 0, 275, 150, 100, 75, 110, 110, 100, 110, 100, 120, 110, 150, 130, 75, 150, 100, 50, 50, 0, 20, 20]

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
    g.write("#\n"
    + "# Generated Sun Nov 29 22:13:36 2015\n"
    + "#\n"
    + "# (phi,   theta,  psi) = (128.790000, 54.390000, 90.700000)\n"
    + "# (lambdaStart, lambdaCenter, lambdaEnd) = (" + str(-lambda_start) + ", 0.000000, " + str(lambda_start) + ")\n"
    + "# (betaStart, betaCenter, betaEnd) = (" + str(beta_start) + ", 0.000000, " + str(-beta_start) + ")\n"
    + "# Lambda Bin size = " + str(lambda_bin_size) + "\n"
    + "# Beta Bin size = " + str(beta_bin_size) + "\n"
    + "#\n"
    + "#\n"
    + "# Nbody = 50000\n"
    + "# Evolve time = 3.945000\n"
    + "# Timestep = 0.000514\n"
    + "# Sun GC Dist = 8.000000\n"
    + "# Criterion = NewCriterion\n"
    + "# Theta = 1.000000\n"
    + "# Quadrupole Moments = true\n"
    + "# Eps = 0.000481\n"
    + "#\n"
    + "#\n"
    + "# Potential: (Milkyway@Home N-body potential)\n"
    + "#\n"
    + "# Disk: MiaymotoNagai\n"
    + "#   mass = 445865.888000\n"
    + "#   a = 6.500000\n"
    + "#   b = 0.260000\n"
    + "#\n"
    + "# Halo: Logarithmic\n"
    + "#   vhalo = 73.000000\n"
    + "#   d = 12.000000\n"
    + "#\n"
    + "#\n"
    + "# UseBin  Lambda  Beta  Probability  Error\n"
    + "#\n"
    + "\n"
    + "n = 50000\n"
    + "massPerParticle = 0.0002400000\n"
    + "totalSimulated = 50000\n"
    + "lambdaBins = " + str(n) + "\n"
    + "betaBins = 1\n")
    
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
    g.write("#\n"
    + "# Generated Sun Nov 29 22:13:36 2015\n"
    + "#\n"
    + "# (phi,   theta,  psi) = (128.790000, 54.390000, 90.700000)\n"
    + "# (lambdaStart, lambdaCenter, lambdaEnd) = (" + str(-lambda_start) + ", 0.000000, " + str(lambda_start) + ")\n"
    + "# (betaStart, betaCenter, betaEnd) = (" + str(beta_start) + ", 0.000000, " + str(-beta_start) + ")\n"
    + "# Lambda Bin size = " + str(lambda_bin_size) + "\n"
    + "# Beta Bin size = " + str(beta_bin_size) + "\n"
    + "#\n"
    + "#\n"
    + "# Nbody = 50000\n"
    + "# Evolve time = 3.945000\n"
    + "# Timestep = 0.001200\n"
    + "# Sun GC Dist = 8.000000\n"
    + "# Criterion = NewCriterion\n"
    + "# Theta = 1.000000\n"
    + "# Quadrupole Moments = true\n"
    + "# Eps = 0.000481\n"
    + "#\n"
    + "#\n"
    + "# Potential: (Milkyway@Home N-body potential)\n"
    + "#\n"
    + "# Disk: MiaymotoNagai\n"
    + "#   mass = 445865.888000\n"
    + "#   a = 6.500000\n"
    + "#   b = 0.260000\n"
    + "#\n"
    + "# Halo: Logarithmic\n"
    + "#   vhalo = 73.000000\n"
    + "#   d = 12.000000\n"
    + "#\n"
    + "#\n"
    + "# UseBin  Lambda  Beta  Probability  Error\n"
    + "#\n"
    + "\n"
    + "n = 50000\n"
    + "massPerParticle = 0.0002400000\n"
    + "totalSimulated = 50000\n"
    + "lambdaBins = 50\n"
    + "betaBins = 50\n") 
    
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
os.chdir("./quick_plots")
os.system("python lb_plot.py hists_outputs/out.out")
os.chdir("../")
#os.system("./stability_test.py " + back_time + " " + r0 + " " + light_r_ratio + " " + mass + " " + mass_ratio)

if(match_histograms == True):
    os.system("~/Desktop/research/nbody_test/bin/milkyway_nbody \
    -h ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_correct + "\
    -s ~/Desktop/research/quick_plots/hists_outputs/" + match_hist_compare)
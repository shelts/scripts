#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
os.system("./clean.sh")
y = True
n = False
names   = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
number_of_files  = 17
M  = 0
plot = y
for i in range(M, number_of_files):
    g = open('./mw_2d_parameter_sweeps/r_vs_rr_' + str(i) + '.txt', 'r')
    num = 1
    for line in g:
        if (line.startswith("The best")):
            break
        else:
            num += 1

    g.close()

    f = open('./mw_likelihood_data/r_vs_rr_data.txt', 'a')
    lines = []
    lines = open('./mw_2d_parameter_sweeps/r_vs_rr_' + str(i) + '.txt').readlines() 
    lines = lines[num:len(lines)]
    for line in lines:
        ss = line.split(',')#splits the line between the two sides the delimiter
        tt = ss[2].split('[')#chooses the second of the split parts and resplits
        ww = ss[7].split(']')
        like = ss[1]
        r = ss[4]
        rr = ss[5]
        #print ss[1], ss[3], ss[4], ss[5], ss[6]
        f.write("%s \t %s \t %s \n" % (r, rr, like))#writes the first of the resplit lines

    f.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if(plot == True):
    f   = 'Forward Evolve Time'
    b   = 'Reverse Orbit Ratio'
    rad  = 'Radius'
    r_r = 'Radius Ratio'
    mass  = 'Mass'
    m_r = 'Mass Ratio'

    name = 'r_vs_rr'
    xlabel = rad
    ylabel = r_r

    #starts, ends
    ft  = [1.0, 3.0]
    bt  = [0.8, 1.2]
    r   = [0.1, 0.9]
    rr  = [0.1, 0.8]
    m   = [2.0, 45]
    mr  = [0.1, 0.55]
    xranges = [0.1, 0.8]  
    yranges = [0.1, 0.8]
    color_cutoff = -1000

    f = open('mw_2d_plot.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal wxt persist\n")
    f.write("set key off\n")
    #f.write("set pm3d interpolate 50,50\n")
    #f.write("set samples 25, 25\n")
    #f.write("set isosamples 26, 26\n")
    #f.write("set contour base\n")
    #f.write("set cntrlabel  format '%8.3g' font ',7' start 5 interval 20\n")
    #f.write("set cntrparam order 8\n")
    #f.write("set cntrparam bspline\n")
    #f.write("set style data lines\n")
    f.write("set xlabel '" + xlabel + "'\n")
    f.write("set ylabel '" + ylabel + "'\n")
    f.write("set zlabel 'likelihood'\n")
    
    #f.write("set palette  maxcolors 1000\n")
    #f.write("set palette rgbformulae \n")
    #f.write("set palette gray \n")
    #f.write("set cbrange[" + str(color_cutoff) + ":0]\n")
    f.write("set xrange[" + str(xranges[0]) + ":" + str(xranges[1]) + "]\n")
    f.write("set zrange[" + str(color_cutoff) + ":0]\n")
    f.write("set yrange[" + str(yranges[0]) + ":" + str(yranges[1]) + "]\n\n\n")

    p = "mw_likelihood_data/" + name + "_data.txt"
    f.write("set output 'plots/" + name + ".png' \n")
    f.write("set title 'Likelihood Surfsace of " + str(xlabel) + " vs " + str(ylabel) + "' \n")
    f.write("splot '" + p + "' using 1:2:3  with points pointtype 7 ps 0.25 \n\n") 
#points pointtype 7 ps 0.25
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

    f.close()

    os.system("gnuplot mw_2d_plot.gnuplot 2>>piped_output.txt")
    os.system("rm mw_2d_plot.gnuplot")
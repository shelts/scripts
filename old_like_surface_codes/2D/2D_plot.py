#! /usr/bin/python
import os

f   = 'Forward Evolve Time'
b   = 'Reverse Orbit Ratio'
rad  = 'Radius'
r_r = 'Radius Ratio'
mass  = 'Mass'
m_r = 'Mass Ratio'


names = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
xlabels = [f, f, f, f, f, b, b, b, b, rad, rad ,rad, r_r, r_r, mass]  
ylabels = [b, rad, r_r, mass, m_r, rad, r_r, mass, m_r, r_r, mass, m_r, mass, m_r, m_r]

#starts, ends
ft  = [1.0, 3.0]
bt  = [0.8, 1.2]
r   = [0.1, 0.9]
rr  = [0.1, 0.7]
m   = [2.0, 45]
mr  = [0.1, 0.55]
xranges_start = [ft[0], ft[0], ft[0], ft[0], ft[0], bt[0], bt[0], bt[0], bt[0], r[0], r[0], r[0], rr[0], rr[0], m[0]]
yranges_start = [bt[0], r[0], rr[0], m[0], mr[0], r[0], rr[0], m [0], mr[0], rr[0], m[0], mr[0], m[0], mr[0], mr[0]]

xranges = [ft[1], ft[1], ft[1], ft[1], ft[1], bt[1], bt[1], bt[1], bt[1], r[1], r[1], r[1], rr[1], rr[1], m[1]]
yranges = [bt[1], r[1], rr[1], m[1], mr[1], r[1], rr[1], m [1], mr[1], rr[1], m[1], mr[1], m[1], mr[1], mr[1]]

color_cutoff = -200

N  = 15
M  = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
data_vals = "parameter_data/"
like_data = "likelihood_data/"


f = open('2D_plot.gnuplot', 'w')
f.write("reset\n")
f.write("set terminal png\n")
f.write("set key off\n")
f.write("set pm3d interpolate 50,50\n")
for i in range(M, N):
    f.write("set xlabel '" + xlabels[i] + "'\n")
    f.write("set ylabel '" + ylabels[i] + "'\n")
    f.write("set zlabel 'likelihood'\n")
    #f.write("set palette  maxcolors 1000\n")
    #f.write("set palette rgbformulae \n")
    #f.write("set palette gray \n")
    f.write("set cbrange[" + str(color_cutoff) + ":0]\n")
    f.write("set xrange[" + str(xranges_start[i]) + ":" + str(xranges[i]) + "]\n")
    f.write("set yrange[" + str(yranges_start[i]) + ":" + str(yranges[i]) + "]\n\n\n")

    p = "<paste parameter_data/" + names[i] + ".txt likelihood_data/" + names[i] + "_data.txt"
    f.write("set output 'plots/" + names[i] + ".png' \n")
    f.write("set title 'Likelihood Surface of " + str(xlabels[i]) + " vs " + str(ylabels[i]) + "' \n")
    f.write("plot '" + p + "' using 1:2:3  with image \n\n") 

    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")
    f.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # \n")

f.close()

os.system("gnuplot 2D_plot.gnuplot 2>>piped_output.txt")
os.system("rm 2D_plot.gnuplot")
#! /usr/bin/python
import os

names   = ['ft', 'bt',  'rad', 'rr', 'mass', 'mr']


for i in range(0,6):
  g = open('./parameter_sweeps/' + str(names[i]) + '.txt', 'r')
  f = open('./likelihood_data/' + str(names[i]) + '_data.txt', 'w')

  for line in g:
    if (line.startswith("<")):
      ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
      tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
      f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
  f.close()
  g.close()


#---------------------------------------------
def oneD_cost_emd_parser():
    for i in range(0,5):
        g = open('./1D_like_surface/parameter_sweeps/' + str(oneD_names[i]) + '.txt', 'r')
        f = open('./1D_like_surface/cost_emd_data/' + str(oneD_names[i]) + '_cost_data.txt', 'w')
        d = open('./1D_like_surface/cost_emd_data/' + str(oneD_names[i]) + '_emd_data.txt', 'w')
        for line in g:
            if (line.startswith("log(EMDComponent)")):
                ss = line.split('log(EMDComponent) = ')#splits the line between the two sides the delimiter
                d.write("%f\n" % (float(ss[1])))#writes the first of the resplit lines
                
            if (line.startswith("log(CostComponent)")):
                tt = line.split('log(CostComponent) = ')#chooses the second of the split parts and resplits
                f.write("%s" % (tt[1]))#writes the first of the resplit lines
        
    f.close()
    g.close()
    d.close()

def oneD_cost_emd_plot():
    ft = [3.8, 4.3]#plot ranges
    bt = [3.8, 4.3]
    r  = [0.1, 4.0]
    rr = [0.7, 4.0]
    m  = [2.0, 120.0]
    mr = [2, 1200]
    l = -100
    #ranges_start = [ft[0], bt[0], r[0], rr[0], m[0], mr[0]]
    #ranges_end   = [ft[1], bt[1], r[1], rr[1], m[1], mr[1]]
    ranges_start = [ft[0], r[0], rr[0], m[0], mr[0]]
    ranges_end   = [ft[1], r[1], rr[1], m[1], mr[1]]
    #how many of the data sets are we plotting
    N  = 5
    M  = 0
    
    #titles  = ['Forward Evolve Time', 'Reverse Orbit Time', 'Baryonic Scale Radius', 'Dark Scale Radius', 'Baryonic Matter Mass',  'Dark Matter Mass']
    titles  = ['Forward Evolve Time', 'Baryonic Scale Radius', 'Dark Scale Radius', 'Baryonic Matter Mass',  'Dark Matter Mass']
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    data_vals = "parameter_data/"
    like_data = "likelihood_data/"


    f = open('1D_plot.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal jpeg\n")
    f.write("set key on\n")

    for i in range(M, N):
        f.write("set xlabel '" + titles[i] + "'\n")
        f.write("set ylabel 'likelihood'\n")
        f.write("set yrange [" + str(l) + ":0]\n")
        f.write("set xrange[" + str(ranges_start[i]) + ":" + str(ranges_end[i]) + "]\n")
        
        p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_cost_data.txt"
        q = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_emd_data.txt"
        w = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/likelihood_data/" + oneD_names[i] + "_data.txt"
        f.write("set output '1D_like_surface/cost_emd_plots/" + oneD_names[i] + "_cost.jpeg' \n")
        f.write("set title 'Cost and EMD Surface of " + titles[i] + "' \n")
        f.write("plot '" + p + "' using 1:2  with lines title 'Cost', '" + q + "' using 1:2  with lines title 'EMD', '" + w + "' using 1:2  with lines title 'Likelihood'\n  \n") 
        
        #p = "<paste 1D_like_surface/parameter_data/" + oneD_names[i] + "_vals.txt 1D_like_surface/cost_emd_data/" + oneD_names[i] + "_emd_data.txt"
        #f.write("set output '1D_like_surface/cost_emd_plots/" + oneD_names[i] + "_emd.jpeg' \n")
        #f.write("set title 'EMD Surface of " + titles[i] + "' \n")
        #f.write("plot '" + p + "' using 1:2  with lines\n\n") 

        f.write("# # # # # # # # # # # # # # # # # #\n")

    f.close()

    os.system("gnuplot 1D_plot.gnuplot 2>>piped_output.txt")
    os.system("rm 1D_plot.gnuplot")
    
    
    
    
    def twoD_parser():
    names   = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
    N  = 15
    M  = 0

    for i in range(M,N):
        g = open('./2D_like_surface/2d_parameter_sweeps/' + str(names[i]) + '.txt', 'r')
        f = open('./2D_like_surface/likelihood_data/' + str(names[i]) + '_data.txt', 'w')

        for line in g:
            if (line.startswith("<")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
        
    f.close()
    g.close()
    
    
    
    
    
    
    
    
        if(plot_cost_emd == True):
        oneD_cost_emd_parser()
        oneD_cost_emd_plot()
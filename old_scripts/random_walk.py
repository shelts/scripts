#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#perform the random walk of which test        #
inertia = True                                #
# # # # # # # # # # # # # # # # # # # # # # # #
#plot which parameter                         #
parameter_to_plot = 'ft'                      #
# # # # # # # # # # # # # # # # # # # # # # # #
#pop up interactive plots                     #
pop_up = False                                #
# # # # # # # # # # # # # # # # # # # # # # # #
#remove duplicate results:                    #
filter_res = True                             #         
# # # # # # # # # # # # # # # # # # # # # # # #




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # 
# struct declaration  #
# # # # # # # # # # # # 
class body:
    'these are bodies'
    body_count = 0

    def __init__(self, pos, l, ft, bt, rl, rr, ml, mr):
      self.pos = pos
      self.l = l
      self.ft = ft
      self.bt = bt
      self.rl = rl
      self.rr = rr
      self.ml = ml
      self.mr = mr
      body.body_count += 1
      
    def count(self):
          print body.body_count
      
# # # # # # # # #  
# parsing code  #
# # # # # # # # #  
def get_start_number(file_name):
    g = open(file_name, 'r')
    num = 1
    for line in g:
        if (line.startswith("The best ")):
            break
        else:
            num += 1
    g.close()
    
    return num

def parser(file_name):
    num = get_start_number(file_name)
    lines = []
    lines = open(file_name).readlines() 
    lines = lines[num:len(lines)] 
    bodies = []
    for line in lines:
        ss = line.split(',')#ss is 9 things long
        tt = ss[2].split('[')#seps out the ft
        ww = ss[7].split(']')#seps out the mr
        
        ps = float(ss[0])
        lk = float(ss[1])
        ft = float(tt[1])
        bt = float(ss[3])
        rl = float(ss[4])
        rr = float(ss[5])
        ml = float(ss[6])
        mr = float(ww[0])
        b = body(ps, lk, ft, bt, rl, rr, ml, mr)
        bodies.append(b)
        
    return bodies

# # # # # # # # #  
# plotting code #
# # # # # # # # #
def filter_results(bodies, i, j, size, parameter_to_plot, parameter):
    found_match = 0
    for ii in range(0, i + 1):
        for jj in range(0, size ):#for every member of the list before the current one
            if(size * ii + jj >= size * i + j):
                break
            if(parameter_to_plot == 'ft'):
                parameter_compare = bodies[ii][jj].ft
            elif(parameter_to_plot == 'bt'):
                parameter_compare = bodies[ii][jj].bt
            elif(parameter_to_plot == 'rl'):
                parameter_compare = bodies[ii][jj].rl
            elif(parameter_to_plot == 'rr'):
                parameter_compare = bodies[ii][jj].rr
            elif(parameter_to_plot == 'ml'):
                parameter_compare = bodies[ii][jj].ml
            elif(parameter_to_plot == 'mr'):
                parameter_compare = bodies[ii][jj].mr
        
            if(parameter == parameter_compare):
                found_match = 1
                break
        if(found_match == 1):
            break
    return found_match

def plot_position_parameter_time(bodies, Nsteps, parameter_to_plot, plot_name):
    f = open(plot_name + '.txt', 'w')
    k = 0
    counter1 = 0
    counter2 = 0
    size = len(bodies[0][:])
    for i in range(0, Nsteps):
        for j in range(0, size):
            if(parameter_to_plot == 'ft'):
                parameter = bodies[i][j].ft
            elif(parameter_to_plot == 'bt'):
                parameter = bodies[i][j].bt
            elif(parameter_to_plot == 'rl'):
                parameter = bodies[i][j].rl
            elif(parameter_to_plot == 'rr'):
                parameter = bodies[i][j].rr
            elif(parameter_to_plot == 'ml'):
                parameter = bodies[i][j].ml
            elif(parameter_to_plot == 'mr'):
                parameter = bodies[i][j].mr
            
            if(filter_res == True):
                found_match = filter_results(bodies, i, j, size, parameter_to_plot, parameter)
                
            if(found_match == 1):
                continue
            else:
                positions = k
                timesteps = float(i)
                f.write("%0.15f\t%0.15f\t%0.15f\n" %( positions, parameter, timesteps))
                k += 1
            

    f = open('random_walk.gnuplot', 'w')
    f.write("reset\n")
    f.write("set key off\n")
    f.write("set ylabel '" + plot_name + "'\n")
    f.write("set xlabel 'returned results'\n")
    f.write("set zlabel 'timesteps'\n")
    
    #f.write("set xrange[2000:4000]\n")
    f.write("set zrange[]\n")
    f.write("set yrange[]\n\n\n")
    f.write("set title 'Randowm Walk of " + (plot_name) + "' \n")

    p = "./" + plot_name + ".txt"
    if(pop_up == True):
        f.write("set terminal wxt persist\n")
        f.write("splot '" + p + "' using 1:2:3  with l pointtype 7 ps 0.25 \n\n") 
    
    f.write("# # # # # # \n")
    f.write("set terminal png\n")
    f.write("set output '" + plot_name + ".png' \n")
    f.write("plot '" + p + "' using 0:2  with p pointtype 7 ps 0.25 \n\n") 
    f.close()
    
    os.system("gnuplot random_walk.gnuplot 2>>piped_output.txt")
    os.system("rm random_walk.gnuplot")
    os.system('rm ' + plot_name + '.txt')
# # # # # # # # # # # # # 
# Types of random walks #
# # # # # # # # # # # # #
def interia_RW():
    file_structure = './inertia/data_inertia_'
    inertias = ['1p0', 'p35', 'p45', 'p55', 'p95']
    files_each = [4, 4, 4, 18, 18]
    
    bodies_1p0 = []
    bodies_p35 = []
    bodies_p45 = []
    bodies_p55 = []
    bodies_p95 = []
    btmp = []
    
    #structure:
    #bodies[the file from which the list came][ the list of results for that file].the parameter

    which = 0
    for i in range(0, files_each[which]):
        file_name = file_structure + inertias[which] + '/inertia_' + inertias[which] + '_' + str(i) + '.txt'
        btmp = parser(file_name)
        bodies_1p0.append(btmp)
    
    
    which = 1
    for i in range(0, files_each[which]):
        file_name = file_structure + inertias[which] + '/inertia_' + inertias[which] + '_' + str(i) + '.txt'
        btmp = parser(file_name)
        bodies_p35.append(btmp)
        
        
    which = 2
    for i in range(0, files_each[which]):
        file_name = file_structure + inertias[which] + '/inertia_' + inertias[which] + '_' + str(i) + '.txt'
        btmp = parser(file_name)
        bodies_p45.append(btmp)
        
    which = 3
    for i in range(0, files_each[which]):
        file_name = file_structure + inertias[which] + '/inertia_' + inertias[which] + '_' + str(i) + '.txt'
        btmp = parser(file_name)
        bodies_p55.append(btmp)
        
    which = 4
    for i in range(0, files_each[which]):
        file_name = file_structure + inertias[which] + '/inertia_' + inertias[which] + '_' + str(i) + '.txt'
        btmp = parser(file_name)
        bodies_p95.append(btmp)
    
    
    
    plot_position_parameter_time(bodies_1p0, files_each[0], parameter_to_plot, parameter_to_plot + '_intertia_1p0')
    plot_position_parameter_time(bodies_p35, files_each[1], parameter_to_plot, parameter_to_plot + '_intertia_p35')
    plot_position_parameter_time(bodies_p45, files_each[2], parameter_to_plot, parameter_to_plot + '_intertia_p45')
    plot_position_parameter_time(bodies_p55, files_each[3], parameter_to_plot, parameter_to_plot + '_intertia_p55')
    plot_position_parameter_time(bodies_p95, files_each[4], parameter_to_plot, parameter_to_plot + '_intertia_p95')
    
    
# # # # # # # 
#    Main   #
# # # # # # #  
def main():
    if(inertia == True):
        interia_RW()
    
main()
    
    
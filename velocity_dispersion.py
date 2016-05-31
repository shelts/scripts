#! /usr/bin/python
import os
from subprocess import call
import math
import sys

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
# Enter control switches                      #
# # # # # # # # # # # # # # # # # # # # # # # #
default_worst_case = -1
y = True
n = False

#how many bins in each direction
l_bins = 1
b_bins = 1
r_bins = 1


l_start = -100.0
l_end = 100.0
l_bin_width = (l_end - l_start) / l_bins

b_start = -20.0
b_end = 20.0
b_bin_width = (b_end - b_start) / b_bins

r_start = 0.0
r_end = 500
r_bin_width = (r_end - r_start) / r_bins
#print(l_bin_width, b_bin_width, r_bin_width)

plot_bins =  n

use_whole_sky = n
sym_l = y

if(use_whole_sky == True):
    l_start = 0.0
    l_end = 360.0
    if(sym_l == True):
        l_start = -180.0
        l_end = 180.0
    l_bin_width = (l_end - l_start) / l_bins

    b_start = -180.0
    b_end = 180.0
    b_bin_width = (b_end - b_start) / b_bins

    r_start = 0.0
    r_end = 500
    r_bin_width = (r_end - r_start) / r_bins


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

    def __init__(self, mtype, mass, x, y, z, l, b, r, vx, vy, vz, vl):
      self.mtype = mtype
      self.mass = mass
      self.x = x
      self.y = y
      self.z = z
      self.l = l
      self.b = b
      self.r = r
      self.vx = vx
      self.vy = vy
      self.vz = vz
      self.vl = vl
      body.body_count += 1
      
    def count(self):
          print body.body_count
      
    def disp_body(self):
          print "body type = ", self.mtype
          print "body mass = ", self.mass
          self.disp_pos()
          self.disp_vel()

    def disp_pos(self):
        print "position: ", self.x, self.y, self.z
    def disp_vel(self):
        print "velocity: ", self.vx, self.vy, self.vz

# # # # # # # # # # 
# data retrieval  #
# # # # # # # # # #

def get_start_number(file_name):
    g = open(file_name, 'r')
    num = 1
    for line in g:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    g.close()
    
    return num

def get_data(file_name):
    num = get_start_number(file_name)
    lines = []
    lines = open(file_name).readlines() 
    lines = lines[num:len(lines)]
    i = 0
    bodies = []
    for line in lines:
        ss = line.split(',')
        ty = (float(ss[0]))
        x  = (float(ss[1]))
        y  = (float(ss[2]))
        z  = (float(ss[3]))
        l  = (float(ss[4]))
        if(sym_l ==True):
            if(l > 180.0):
                l = l - 360.0
        b  = (float(ss[5]))
        r  = (float(ss[6]))
        vx = (float(ss[7]))
        vy = (float(ss[8]))
        vz = (float(ss[9]))
        m  = (float(ss[10]))
        
        vl = calc_line_of_sight(x, y, z, vx, vy, vz)
        b = body(ty, m , x, y, z, l, b, r, vx, vy, vz, vl) 
        bodies.append(b)
        i += 1
    return bodies

# # # # # # # # # # 
# data binning    #
# # # # # # # # # #
def binner_lbr(bodies):
    r_count = 0
    b_count = 0
    l_count = 0
    bins = [[[[] for z in range(l_bins)]  for y in range(b_bins)] for x in range(r_bins)] 
    #print(bins)
    
    #
        #This algorithm goes through each bin of the sky and each body. 
        #When it finds the bin the body belongs to, it stores the body index.
        #The array structure is: 
        #bins[current r bin][current b bin][current l bin][list of indexs of the bodies that are here]
    #
    
    for i in range(0, len(bodies)):#for each body
        for j in range(0, r_bins): #for each r bin
            if(bodies[i].r >= r_start + j * r_bin_width and bodies[i].r < r_start + (j + 1) * r_bin_width): #if it is in the r bin
                r_count += 1
                for k in range(0, b_bins): #if it is in the r bin, for each b bin
                    
                    if(bodies[i].b >= b_start + k * b_bin_width and bodies[i].b < b_start + (k + 1) * b_bin_width): #if it is in the b bin
                        b_count += 1
                        for m in range(0, l_bins): #if it is in the r,b bin for each l bin
                            
                            if(bodies[i].l >= l_start + m * l_bin_width and bodies[i].l < l_start + (m + 1) * l_bin_width):
                                l_count += 1
                                bins[j][k][m].append(i)
                                
    
    #print(r_count, b_count, l_count)
    return bins

# # # # # # # # # # 
# plotting code   #
# # # # # # # # # #
def plot_binned_counts(bins, disp_per_bin):
    p = 'data.txt'
    g = open(p, 'w')
    
    for j in range(0, r_bins): #for each r bin
            for k in range(0, b_bins): #for each b bin
                    for m in range(0, l_bins): #for each l bin
                        counts = (len(bins[j][k][m][:]))
                        disp_vx = disp_per_bin[j][k][m][0]
                        disp_vy = disp_per_bin[j][k][m][1]
                        disp_vz = disp_per_bin[j][k][m][2]
                        disp_vl = disp_per_bin[j][k][m][3]
                        g.write("%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n" % (j * r_bin_width + r_start, m * l_bin_width + l_start, k * b_bin_width + b_start, counts, disp_vl, disp_vx, disp_vy, disp_vz))
    
    g.close()
    
    b_lower = -80
    b_upper = 80
    dispersion_cutoff = 50
    count_cutoff = 100
    f = open('binned_counts_dispersions.gnuplot', 'w')
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'b'\n")
    f.write("set xlabel 'l'\n")
    
    f.write("set xrange[" + str(l_end) + ":" + str(l_start) + "]\n")
    f.write("set yrange[" + str(b_lower) + ":" + str(b_upper) + "]\n")
    f.write("set cbrange[0:" + str(count_cutoff) + "]\n")
    
    f.write("set title 'counts' \n")
    f.write("set output 'counts.png' \n")
    f.write("plot '" + p + "' using 2:3:4 with image\n")
    f.write("# # # # # # # # # # # # # # #\n")
    f.write("reset\n")
    f.write("set terminal png\n")
    f.write("set key off\n")
    f.write("set ylabel 'b'\n")
    f.write("set xlabel 'l'\n")
    
    f.write("set xrange[" + str(l_end) + ":" + str(l_start) + "]\n")
    f.write("set yrange[" + str(b_lower) + ":" + str(b_upper) + "]\n")
    f.write("set cbrange[" + str(default_worst_case) + ":" + str(dispersion_cutoff) + "]\n")
    
    f.write("set title 'dispersions' \n")
    f.write("set output 'dispersions_vl.png' \n")
    f.write("plot '" + p + "' using 2:3:5 with image\n")
    
    f.write("set output 'dispersions_vx.png' \n")
    f.write("plot '" + p + "' using 2:3:6 with image\n")
    
    f.write("set output 'dispersions_vy.png' \n")
    f.write("plot '" + p + "' using 2:3:7 with image\n")
    
    f.write("set output 'dispersions_vz.png' \n")
    f.write("plot '" + p + "' using 2:3:8 with image\n")
    f.close()
    os.system('gnuplot binned_counts_dispersions.gnuplot 2>>gnuplot_errors.txt')
    
# # # # # # # # # # 
# calc dispersion #
# # # # # # # # # #

def binned_dispersion(bins, bodies):
    dispersion_per_bin = [[[[default_worst_case for xyzl in range(4)] for z in range(l_bins)]  for y in range(b_bins)] for x in range(r_bins)] 
    #print(dispersion_per_bin)
    disp_vx1 = 0
    disp_vy1 = 0
    disp_vz1 = 0
    
    disp_vx2 = 0
    disp_vy2 = 0
    disp_vz2 = 0
    
    disp_vl1 = 0
    disp_vl2 = 0
    total_number = 0
    #
        #this will go through each of the bins and calculate the vel dispersion in each bin.
        #it will only do the calculation if there is a list of indexes in that bin, 
        #meaning there are bodies in the bin.
        #the dispersion in each direction is stored in an array which has 3 values per bin.
    #
    for j in range(0, r_bins): #for each r bin
            for k in range(0, b_bins): #for each b bin
                    for m in range(0, l_bins): #for each l bin
                            if(bins[j][k][m][:]):#if there is bodies in the bin calc the dispersion in it
                                N_bodies_in_bin = (len(bins[j][k][m][:]))
                                total_number += N_bodies_in_bin
                                disp_vx1 = 0
                                disp_vy1 = 0
                                disp_vz1 = 0
                                
                                disp_vx2 = 0
                                disp_vy2 = 0
                                disp_vz2 = 0
                                
                                disp_vl1 = 0
                                disp_vl2 = 0
                                    
                                for index in range(0, N_bodies_in_bin):
                                    #print N_bodies_in_bin
                                    i = bins[j][k][m][index]
                                    #print i
                                    disp_vx1 += bodies[i].vx * bodies[i].vx   
                                    disp_vx2 += bodies[i].vx
                                
                                    disp_vy1 += bodies[i].vy * bodies[i].vy
                                    disp_vy2 += bodies[i].vy
                                    
                                    disp_vz1 += bodies[i].vz * bodies[i].vz  
                                    disp_vz2 += bodies[i].vz
                                    
                                    disp_vl1 += bodies[i].vl * bodies[i].vl
                                    disp_vl2 += bodies[i].vl 
                                    #print disp_vl2, bodies[i].vl
                                    
                                N = N_bodies_in_bin
                                disp_vx = (disp_vx1 / N) - (disp_vx2 * disp_vx2 / (N * N) )
                                disp_vy = (disp_vy1 / N) - (disp_vy2 * disp_vy2 / (N * N) )
                                disp_vz = (disp_vz1 / N) - (disp_vz2 * disp_vz2 / (N * N) )
                                disp_vl = (disp_vl1 / N) - (disp_vl2 * disp_vl2 / (N * N) )
                                #print disp_vy1, disp_vy2
                                
                                dispersion_per_bin[j][k][m][0] = disp_vx
                                dispersion_per_bin[j][k][m][1] = disp_vy
                                dispersion_per_bin[j][k][m][2] = disp_vz
                                dispersion_per_bin[j][k][m][3] = disp_vl
                                #print disp_vl, N_bodies_in_bin
    
    return dispersion_per_bin

def vel_disp(file_name, bodies):
    N = len(bodies)
    disp_vx1 = 0
    disp_vy1 = 0
    disp_vz1 = 0
    
    disp_vx2 = 0
    disp_vy2 = 0
    disp_vz2 = 0
    
    disp_vl1 = 0
    disp_vl2 = 0
    #vx dispersion
    for i in range(0, N):
        disp_vx1 += bodies[i].vx * bodies[i].vx   
        disp_vx2 += bodies[i].vx
    
        disp_vy1 += bodies[i].vy * bodies[i].vy
        disp_vy2 += bodies[i].vy
        
        disp_vz1 += bodies[i].vz * bodies[i].vz  
        disp_vz2 += bodies[i].vz
        
        disp_vl1 += bodies[i].vl * bodies[i].vl
        disp_vl2 += bodies[i].vl 
        
    disp_vx = (disp_vx1 / N) - (disp_vx2 * disp_vx2 / (N * N) )
    disp_vy = (disp_vy1 / N) - (disp_vy2 * disp_vy2 / (N * N) )
    disp_vz = (disp_vz1 / N) - (disp_vz2 * disp_vz2 / (N * N) )
    
    disp_vl = (disp_vl1 / N) - (disp_vl2 * disp_vl2 / (N * N) )
    return disp_vx, disp_vy, disp_vz, disp_vl


# # # # # # # # # # #
# mass calculations #
# # # # # # # # # # #
def calc_half_light_radius(bodies):
    total_mass = 0
    total_dark_mass = 0
    total_light_mass = 0

    for i in range(0, body.body_count):
        total_mass += bodies[i].mass
        if(bodies[i].mtype == 1):
            total_dark_mass += bodies[i].mass
        if(bodies[i].mtype == 0):
            total_light_mass += bodies[i].mass
            
            
    
    print total_mass, total_light_mass, total_dark_mass
    
    return half_light_radius

def calc_actual_mass_in_bin(bins, bodies):#calculates the total mass
    total_mass = 0
    total_count = 0
    for j in range(0, r_bins): #for each r bin
            for k in range(0, b_bins): #for each b bin
                    for m in range(0, l_bins): #for each l bin
                        N_bodies_in_bin = (len(bins[j][k][m][:]))
                        total_count += N_bodies_in_bin
                        
                        for index in range(0, N_bodies_in_bin):
                            i = bins[j][k][m][index]
                            total_mass += bodies[i].mass
                            
    print 'correct mass:', total_mass, '\nbody count:', total_count
    return total_mass

def calc_mass_per_bin(disp_per_bin, half_light_radius):#for when looking at core (1 bin)
    mass_per_bin = [[[[0 for xyzl in range(1)] for z in range(l_bins)]  for y in range(b_bins)] for x in range(r_bins)] 
    half_light_radius = 5.0 #place holder until I figure out how to calculate this.
    
    for j in range(0, r_bins): #for each r bin
            for k in range(0, b_bins): #for each b bin
                    for m in range(0, l_bins): #for each l bin
                        if(disp_per_bin[j][k][m][3] != default_worst_case):#make sure the line of sight velocity was calculated (there were bodies in the bin)
                            sigma = disp_per_bin[j][k][m][3]
                            mass = 3.0 * sigma * sigma / half_light_radius
                            mass_per_bin[j][k][m][0] = mass
                            #print 'mass from dispersion:', mass, '\ndispersion:', sigma
    return mass_per_bin
# # # # # # # # # # # # # # # 
# line of sight conversion  #
# # # # # # # # # # # # # # #
def calc_line_of_sight(x, y, z, vx, vy, vz):
    x += 8 #for sun centered coordinates
    mag = (x * x + y * y + z * z) ** (0.5)
    vl = x * vx + y * vy + z * vz
    vl = vl / mag
    #print vl, vx, vy, vz, x, y, z
    return vl
    
def main():
    if(len(sys.argv) > 1):
        name1 = str(sys.argv[1])
    else: 
        name1 = 'velocity_dispersion_test_Null_lbr_xyz_0gy'
        #name1 = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = '/home/sidd/Desktop/research/quick_plots/outputs/' + name1 + '.out'
    print "for output: ", name1 
    
    bodies = []
    bodies = get_data(file_name)
    
    #this calculates the total vx vy vz dispersion
    disp_vx, disp_vy, disp_vz, disp_vl = vel_disp(file_name, bodies)
    dispersion = [disp_vx, disp_vy, disp_vz, disp_vl]
    #print(dispersion) #dispersion of the entire sky
    
    #this bins the bodies by their positions
    bins = []
    bins = binner_lbr(bodies)
    
    #this calculates the vx vy vz vline_of_sight dispersion in each bin
    dispersion_per_bin = []
    dispersion_per_bin = binned_dispersion(bins, bodies)
    
    mass_per_bin = []
    half_light_radius = calc_half_light_radius(bodies)
    mass_per_bin = calc_mass_per_bin(dispersion_per_bin, half_light_radius)
    
    calc_actual_mass_in_bin(bins, bodies)
    
    if(plot_bins == True):
        plot_binned_counts(bins, dispersion_per_bin)
main()
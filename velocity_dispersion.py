#! /usr/bin/python
import os
from subprocess import call
import math
import sys


class body:
    'these are bodies'
    body_count = 0

    def __init__(self, mtype, mass, x, y, z, l, b, r, vx, vy, vz):
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
      self.vz =  vz
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
        b  = (float(ss[5]))
        r  = (float(ss[6]))
        vx = (float(ss[7]))
        vy = (float(ss[8]))
        vz = (float(ss[9]))
        m  = (float(ss[10]))
        b = body(ty, m , x, y, z, l, b, r, vx, vy, vz) 
        bodies.append(b)
        i += 1
    #print bodies[0].y
    return bodies

def vel_disp(file_name, bodies):
    N = len(bodies)
    disp_vx1 = 0
    disp_vy1 = 0
    disp_vz1 = 0
    
    disp_vx2 = 0
    disp_vy2 = 0
    disp_vz2 = 0
    #vx dispersion
    for i in range(0, N):
        disp_vx1 += bodies[i].vx * bodies[i].vx   
        disp_vx2 += bodies[i].vx
    
        disp_vy1 += bodies[i].vy * bodies[i].vy
        disp_vy2 += bodies[i].vy
        
        disp_vz1 += bodies[i].vz * bodies[i].vz  
        disp_vz2 += bodies[i].vz

    disp_vx = (disp_vx1 / N) - (disp_vx2 * disp_vx2 / (N * N) )
    disp_vy = (disp_vy1 / N) - (disp_vy2 * disp_vy2 / (N * N) )
    disp_vz = (disp_vz1 / N) - (disp_vz2 * disp_vz2 / (N * N) )
    
    return disp_vx, disp_vy, disp_vz


def binned_dispersion(bins, bodies, l_bins, b_bins, r_bins)
            for j in range(0, r_bins): #for each r bin
                    for k in range(0, b_bins): #for each b bin
                            for m in range(0, l_bins): #for each l bin
                                    if(bins[j][k][m][:]):
                                        print(bins[j][k][m][:])


#def convert_line_of_sight():
    
def binner_lbr(bodies, l_bins, b_bins, r_bins):
    l_start = 0.0
    l_end = 360.0
    l_bin_width = (l_end - l_start) / l_bins
    #l_bins = 4
    #b_bins = 1
    #r_bins = 1
    
    
    b_start = -180.0
    b_end = 180.0
    b_bin_width = (b_end - b_start) / b_bins
    
    r_start = 0.0
    r_end = 500
    r_bin_width = (r_end - r_start) / r_bins
    print(l_bin_width, b_bin_width, r_bin_width)
    

    r_count = 0
    b_count = 0
    l_count = 0
    bins = [[[[] for z in range(l_bins)]  for y in range(b_bins)] for x in range(r_bins)] 
    #print(bins)
    t = 0
    #for x in range(0, r_bins):
        #for y in range(0, b_bins):
            #for z in range(0, l_bins):
                #bins[x][y][z] = 0
                #t += 1

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
                                print(m, l_start + m * l_bin_width, l_start + (m + 1) * l_bin_width)
                                bins[j][k][m].append(i)
                                
    
    #print(r_count, b_count, l_count)
    return bins


def main():
    name1 = str(sys.argv[1])
    file_name = '/home/sidd/Desktop/research/quick_plots/outputs/' + name1 + '.out'
        
    print "for output: ", name1 
    bodies = []
    bodies = get_data(file_name)
    disp_vx, disp_vy, disp_vz = vel_disp(file_name, bodies)
    dispersion = [disp_vx, disp_vy, disp_vz]
    print(dispersion)
    l_bins = 4
    b_bins = 1
    r_bins = 1
    
    bins = []
    bins = binner_lbr(bodies, l_bins, b_bins, r_bins)
    
    binned_dispersion(bins, bodies, l_bins, b_bins, r_bins)
    
    
main()
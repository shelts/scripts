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

def vel_disp(file_name):
    bodies = []
    bodies = get_data(file_name)
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

def main():
    name1 = str(sys.argv[1])
    file_name = '/home/sidd/Desktop/research/quick_plots/outputs/' + name1 + '.out'
        
    print "for output: ", name1 
    vel_disp(file_name)
    disp_vx, disp_vy, disp_vz = vel_disp(file_name)
    dispersion = [disp_vx, disp_vy, disp_vz]
    print(dispersion)
    
main()
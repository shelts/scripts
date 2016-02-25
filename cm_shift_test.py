#! /usr/bin/python
import os
from subprocess import call
import math
import sys


class body:
    'these are bodies'
    body_count = 0

    def __init__(self, mtype, mass, x, y, z, vx, vy, vz):
      self.mtype = mtype
      self.mass = mass
      self.x = x
      self.y = y
      self.z = z
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

def get_data(file_name, masspd, masspl):
    num = get_start_number(file_name)
    lines = []
    lines = open(file_name).readlines() 
    lines = lines[num:len(lines)]
    i = 0
    bodies = []
    mass = 0.0
    for line in lines:
        ss = line.split(',')
        mtype = (float(ss[0]))
        if(mtype == 0):
            mass = masspl
        else:
            mass = masspd
            
        x  = (float(ss[1]))
        y  = (float(ss[2]))
        z  = (float(ss[3]))
        vx = (float(ss[4]))
        vy = (float(ss[5]))
        vz = (float(ss[6]))
        b = body(mtype, mass , x, y, z, vx, vy, vz) 
        bodies.append(b)
        i += 1
    #print bodies[0].y
    return bodies

def get_N(file_name):
    g = open(file_name, 'r')
    N = 0
    count = False
    for line in g:
        if (line.startswith("# ignore")):
            count = True
            continue
        if(count == True):
            N += 1
    g.close()
    return N

def com(file_name, mass_l, mass_d, N):
    masspd = mass_d / (0.5 * N)
    masspl = mass_l / (0.5 * N)
    
    bodies = []
    bodies = get_data(file_name, masspd, masspl)
    cm_x = 0
    cm_y = 0
    cm_z = 0
    cm_vx = 0
    cm_vy = 0
    cm_vz = 0
    #print "light mass: ", mass_l
    #print "dark mass: ",  mass_d
    #print  "mass per dark particle: ", masspd
    #print "mass per light particle: ", masspl
    for i in range (0, N):
        cm_x += bodies[i].mass * bodies[i].x
        cm_y += bodies[i].mass * bodies[i].y
        cm_z += bodies[i].mass * bodies[i].z
        
        cm_vx += bodies[i].mass * bodies[i].vx
        cm_vy += bodies[i].mass * bodies[i].vy
        cm_vz += bodies[i].mass * bodies[i].vz

    cm = [0.0, 0.0, 0.0]
    cmv = [0.0, 0.0, 0.0]
    cm[0] = cm_x / (mass_l + mass_d)
    cm[1] = cm_y / (mass_l + mass_d)
    cm[2] = cm_z / (mass_l + mass_d)
    
    cmv[0] = cm_vx / (mass_l + mass_d)
    cmv[1] = cm_vy / (mass_l + mass_d)
    cmv[2] = cm_vz / (mass_l + mass_d)    
    CM = math.sqrt( cm[0] * cm[0] + cm[1] * cm[1] + cm[2] * cm[2] )
    CMV = math.sqrt( cmv[0] * cmv[0] + cmv[1] * cmv[1] + cmv[2] * cmv[2] )
    print "COM of (x, y, z): (", cm[0], cm[1], cm[2], ")"
    print "COV of (x, y, z): (",cmv[0], cmv[1], cmv[2], ")"
    return CM, CMV
    

def main():
    mass_l = float( sys.argv[1] )
    mass_ratio = float( sys.argv[2] )
    
   
    file1 = 'quick_plots/hists_outputs/0gy_null_pot.out'
    file2 = 'quick_plots/hists_outputs/4gy_null_pot.out'
    if(len(sys.argv) == 4):
        name1 = str(sys.argv[3])
        file1 = 'quick_plots/hists_outputs/' + name1
   
    if(len(sys.argv) == 5):
        name1 = str(sys.argv[3])
        name2 = str(sys.argv[4])
        file1 = 'quick_plots/hists_outputs/' + name1
        file2 = 'quick_plots/hists_outputs/' + name2
        
    #print mass_l, mass_ratio, N
    dwarfMass = mass_l / mass_ratio
    mass_d    = dwarfMass * (1.0 - mass_ratio)
    
    #file1 = 'quick_plots/hists_outputs/regular.out'
    #file2 = 'quick_plots/hists_outputs/regular.out'
    print "for output: ", name1 
    N1 = get_N(file1)
    cm1, cmv1 = com(file1, mass_l, mass_d, N1)
    print "initial COM: ", cm1, "\ninitial COV: ", cmv1, "\n" 
    
    if(len(sys.argv) == 5):
        print "for output: ", name2
        N2 = get_N(file2)
        cm2, cmv2 = com(file2, mass_l, mass_d, N2)
        print "initial COM: ", cm2, "\ninitial COV: ", cmv2, "\n" 
        
        
        v_ave = (cm2 - cm1) / (4.0)
        
        ace = ((cmv2 * cmv2) - (cmv1 * cmv1)) / (2.0)
        
        print "average velocity: ", v_ave, "\tacceleration ", ace

main()
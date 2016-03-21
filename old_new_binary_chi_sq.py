#! /usr/bin/python
import os
from subprocess import call
import math as m
import numpy as np
import sys
args = sys.argv;

folder = "quick_plots"

def get_data(file1, type_of_data):
    
    if(type_of_data == "output"):
        starting = 5
    if(type_of_data == "initial"):
        starting = 3
    lines = []
    lines = open(folder + '/' + file1).readlines();
    lines = lines[starting:len(lines) - 3]
    x1 = []
    y1 = []
    z1 = []
    vx1 = []
    vy1 = []
    vz1 = []
    for line in lines:
        if(type_of_data == "initial"):
            tokens = line.split();
            if tokens: #tests to make sure tokens is not empty
                x = float(tokens[0])
                y = float(tokens[1])
                z = float(tokens[2])
                vx = float(tokens[3])
                vy = float(tokens[4])
                vz = float(tokens[5])
        if(type_of_data == "output"):
            tokens = line.split(",");
            if tokens: #tests to make sure tokens is not empty
                x = float(tokens[1])
                y = float(tokens[2])
                z = float(tokens[3])
                vx = float(tokens[4])
                vy = float(tokens[5])
                vz = float(tokens[6])
                
        x1.append(x)
        y1.append(y)
        z1.append(z)
        vx1.append(vx)
        vy1.append(vy)
        vz1.append(vz)
    return x1, y1, z1, vx1, vy1, vz1


def get_vec(x, y, z):
    X = []
    for i in range(0, len(x)):
        #print(x[0], y[0], z[0])
        X.append(m.sqrt( x[i] * x[i] + y[i] * y[i] + z[i] * z[i] ))
        
        
    Y = np.add( np.power(x, 2), np.power(y, 2) )
    Y = np.add(Y, np.power(z, 2))
    Y = np.sqrt(Y)
    #print(Y[0], X[0])
    return X


def calc_chi_sq(x, y):
    total = 0.0
    total2 = 0.0
    for i in range(0, len(x)):
        total += (x[i] - y[i])**2.0
    
    return total
    
def main():
    
    file1 = "ipv_old_binary0gy.txt"
    file2 = "ipv_new_binary0gy.txt"
    
    if(len(sys.argv) == 4):
        file1 = str(args[1])
        file2 = str(args[2])
        data_type = str(args[3])
        
    print("comparing: \n%s \n%s\n%s" % (file1, file2, data_type))
    x1, y1, z1, vx1, vy1, vz1 = get_data(file1, data_type)
    x2, y2, z2, vx2, vy2, vz2 = get_data(file2, data_type)
    #print("%.12f %.12f \n" % (vz1[0], vz2[0]))
    
    x_csq = calc_chi_sq(x1, x2)
    y_csq = calc_chi_sq(y1, y2)
    z_csq = calc_chi_sq(z1, z2)
    
    vx_csq = calc_chi_sq(vx1, vx2)
    vy_csq = calc_chi_sq(vy1, vy2)
    vz_csq = calc_chi_sq(vz1, vz2)
    print("%0.20f %0.20f %0.20f %0.20f %0.20f %0.20f\n" % (x_csq, y_csq, z_csq, vx_csq, vy_csq, vz_csq))
    X1 = get_vec(x1, y1, z1)
    V1 = get_vec(vx1, vy1, vx1)
    
    X2 = get_vec(x2, y2, z2)
    V2 = get_vec(vx2, vy2, vx2)
    positions_csq = calc_chi_sq(X1, X2)
    velocities_csq = calc_chi_sq(V1, V2)
    print("%.20f %.20f \n" % (positions_csq, velocities_csq))
    
main()
#/* Copyright (c) 2016 Siddhartha Shelton */
import sys
import numpy as np
import matplotlib.pyplot as plt





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


def parse_data(file_name, ext):
    g = open('light_matter.dat', 'w')
    f = open('dark_matter.dat', 'w')
    lines = []
    lines = open(file_name).readlines() 
    start = get_start_number(file_name)
    lines = lines[start:len(lines)];

    for line in lines:
        tt = line.split(', ');
        #print(len(tt))
        isDark = int(tt[0]);
        if(len(tt) == 8):
            x = float(tt[1]);
            y = float(tt[2]);
            z = float(tt[3]);
            vx = float(tt[4]);
            vy = float(tt[5]);
            vz = float(tt[6]);
        if(len(tt) == 11):
            x = float(tt[1]);
            y = float(tt[2]);
            z = float(tt[3]);
            l = float(tt[4]);
            b = float(tt[5]);
            r = float(tt[6]);
            vx = float(tt[7]);
            vy = float(tt[8]);
            vz = float(tt[9]);

        if(len(tt) == 8):
            if (isDark == 1):
                f.write("%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t\n" % (x, y, z, vx, vy, vz))
            else:
                g.write("%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t\n" % (x, y, z, vx, vy, vz))
        if(len(tt) == 11):
            if (isDark == 1):
                f.write("%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t\n" % (x, y, z, l, b, r, vx, vy, vz))
            else:
                g.write("%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t%.15f\t\n" % (x, y, z, l, b, r, vx, vy, vz))

def main():
    args = sys.argv;
    file_name = args[1];
    ext       = args[2];
    parse_data(file_name, ext)

main()
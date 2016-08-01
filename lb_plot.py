#/* Copyright (c) 2016 Siddhartha Shelton */
import sys
import numpy as np
import matplotlib.pyplot as plt

args = sys.argv;

try:
    PATH = args[1];
except:
    print("Please pass a file to the program.\n")
    return 1;

try:
    f = open(PATH)
except:
    print("Error 404 file not found.\n")
    return 2;

lines = [];
lines = f.readlines();
lines = lines[4:len(lines)];

light_l = [];
light_b = [];
light_r = [];
light_vx = [];
light_vy = [];
light_vz = [];

for line in lines:
    tokens = line.split(', ');
    isDark = int(tokens[0]);
    l = float(tokens[1]);
    if(l > 180.0):
        l = l - 360.0
    b = float(tokens[2]);
    r = float(tokens[3]);
    vx = float(tokens[4]);
    vy = float(tokens[5]);
    vz = float(tokens[6]);

    light_l.append(l);
    light_b.append(b);
    light_r.append(r)
    light_vx.append(vx);
    light_vy.append(vy);
    light_vz.append(vz);


light_l = np.array(light_l);
light_b = np.array(light_b);
light_r = np.array(light_r);
light_vx = np.array(light_vx);
light_vy = np.array(light_vy);
light_vz = np.array(light_vz);

plt.plot(light_l, light_b, '.', markersize=2)
plt.xlim((180, -180))
plt.ylim((-80, 80))
plt.xlabel('l')
plt.ylabel('b')
plt.title('l vs b')
plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream', format='png')
#plt.show()

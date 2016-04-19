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

light_x = [];
light_y = [];
light_z = [];
light_vx = [];
light_vy = [];
light_vz = [];

dark_x = [];
dark_y = [];
dark_z = [];
dark_vx = [];
dark_vy = [];
dark_vz = [];

for line in lines:
    tokens = line.split(', ');
    isDark = int(tokens[0]);
    x = float(tokens[1]);
    y = float(tokens[2]);
    z = float(tokens[3]);
    vx = float(tokens[4]);
    vy = float(tokens[5]);
    vz = float(tokens[6]);

    #print isDark
    if (isDark == 1):
        dark_x.append(x);
        dark_y.append(y);
        dark_z.append(z)
        dark_vx.append(vx);
        dark_vy.append(vy);
        dark_vz.append(vz);
    
    else:
        light_x.append(x);
        light_y.append(y);
        light_z.append(z)
        light_vx.append(vx);
        light_vy.append(vy);
        light_vz.append(vz);

#print lightProperties;
#print darkProperties;

light_x = np.array(light_x);
light_y = np.array(light_y);
light_z = np.array(light_z);
light_vx = np.array(light_vx);
light_vy = np.array(light_vy);
light_vz = np.array(light_vz);

dark_x = np.array(dark_x);
dark_y = np.array(dark_y);
dark_z = np.array(dark_z);
dark_vx = np.array(dark_vx);
dark_vy = np.array(dark_vy);
dark_vz = np.array(dark_vz);

print "light: ", len(light_x), "dark: ", len(dark_x)
np.savetxt('./light_matter.dat', zip(light_x,light_y, light_z,light_vx, light_vy, light_vz), delimiter='\t')

np.savetxt('./dark_matter.dat', zip(dark_x,dark_y, dark_z,dark_vx, dark_vy, dark_vz), delimiter='\t')

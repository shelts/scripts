#!/usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import numpy as np
import matplotlib.pyplot as plt
import sys
import pylab as lab
import re
import math

#Command Line Args
histogram = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p25_m60_mr0p2_2D.hist" 
f = open('hists_outputs/' + histogram, 'r')

x = []; y = []; likelihood = [];

lmin = 0.0;
lmax = -10.0;
tmin = -150;
tmax = 150;
pmin = -40;
pmax = 40;
xparam = 0.0;
count = 0;

best = [0.0, 0.0]

lines = []
lines = open('hists_outputs/' + histogram).readlines();
lines = lines[40:len(lines)]

for line in lines:
    ln = line.split();
    if ln:
        if count == 0:
            temp = [];
        if count != 0:
            #print len(temp);
            x.append(temp);
            temp = [];
        if(count == 3):
            print x
        temp.append(float(ln[3]));
        count += 1;
        
lines = []
lines = open('hists_outputs/' + histogram).readlines();
lines = lines[40:len(lines)]
sim_lx = []
sim_by = []
sim_nz = []
cts = []
for line in lines:
    tokens = line.split();
    if tokens: #tests to make sure tokens is not empty
        lda = float(tokens[1])
        bta = float(tokens[2])
        cts.append(float(tokens[3]))
        sim_lx.append(lda)
        sim_by.append(bta)
        sim_nz.append(cts)

#print count;

extent = [ tmin, tmax, pmin, pmax ];
print "%3f %3f %3f %3f" % (tmin, tmax, pmin, pmax);
x = np.array(sim_nz).transpose();
#print sim_nz
#plt.imshow(x, extent=extent, origin='lower', interpolation='spline16', 
plt.imshow(sim_nz, interpolation='none', vmin=lmin, vmax=lmax, cmap='gray');
plt.colorbar();
#plt.contour(x, 10, extent=extent, vmin=lmin, vmax=lmax, cmap='autumn');
plt.xlabel("Theta");
plt.ylabel("Phi");
plt.title("Theta, Phi Parameter Sweep");
plt.xlim([extent[0], extent[1]]);
plt.ylim([extent[2], extent[3]]);
plt.grid();
plt.show();
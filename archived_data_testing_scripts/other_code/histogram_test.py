#! /usr/bin/python
import os
from subprocess import call

args = [4, 1, 0.2, .2, 60, 0.2]

counts = [150, 0, 0, 0, 275, 150, 100, 75, 110, 110, 100, 110, 100, 120, 110, 150, 130, 75, 150, 100, 50, 50, 0, 20, 20]

#print "parameters: ", back_time, r0, light_r_ratio, mass, mass_ratio
make_data_hist = False

data2 = "Orphan_Data_September_2014.hist"
data = "data.hist"
#######################################################################

if(make_data_hist == True):
    g = open("histograms/" + data, 'w')
    lamb = 32 + 5
    total = 0.0
    for i in range(0, len(counts)):
        total = total + counts[i]
    total = total * 5.0 / 222288.24  #each count is fturn off star which reps about a cluster of 5 solar masses
    for i in range(0, len(counts)):
        bodies = counts[i] * 5.0 / 222288.24
        g.write("%f \t %f\n" % (lamb, bodies / total ))
        lamb = lamb - 3
    g.close()


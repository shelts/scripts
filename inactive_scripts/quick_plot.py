#! /usr/bin/python
import os
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

os.system("mv ~/Desktop/research/nbody_test/bin/invertfunc.txt ./")
os.system("mv ~/Desktop/research/nbody_test/bin/invertfunc_den.txt ./")
print("plotting")
lines = []
lines = open('./invertfunc.txt').readlines();
lines = lines[0:len(lines)]
vel = []
func = []
for line in lines:
    tokens = line.split();
    if tokens: #tests to make sure tokens is not empty
        v = float(tokens[0])
        f = float(tokens[1])
        vel.append(v)
        func.append(f)
        
#lines = []
#lines = open('./invertfunc_den.txt').readlines();
#lines = lines[0:len(lines)]
#rad = []
#den_l = []
#den_d = []
#for line in lines:
    #tokens = line.split();
    #if tokens: #tests to make sure tokens is not empty
        #r  = float(tokens[0])
        #dl = float(tokens[1])
        #dd = float(tokens[2])
        #rad.append(r)
        #den_l.append(dl)
        #den_d.append(dd)


#plt.subplot(311)
plt.plot(vel, func, color='b')
plt.title('vel')
#plt.xlim((140, -140))
#plt.ylim((0.0, 0.15))
plt.xlabel('v')
plt.ylabel('func')
#plt.savefig('./inversionfunc.png', format='png')

#plt.subplot(312)
#plt.plot(rad, den_l, color='k')
#plt.title('den light')
#plt.xlim((0, 1))
##plt.ylim((0.0, 0.15))
#plt.xlabel('r')
#plt.ylabel('den')
##f.subplots_adjust(hspace=0)
##plt.savefig('./inversionfunc_denl.png', format='png')
##plt.show()


#plt.subplot(313)
#plt.plot(rad, den_d, color='k')
#plt.title('den dark')
#plt.xlim((0, 1))
##plt.ylim((0.0, 0.15))
#plt.xlabel('l')
#plt.ylabel('den')
##f.subplots_adjust(hspace=0)
#plt.tight_layout()
#plt.savefig('./inversionfunc.png', format='png')
plt.show()
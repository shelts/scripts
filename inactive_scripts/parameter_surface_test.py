#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

#Original
radius_l = 0.2
radius_ratio = []
radius_d_old = []
radius_d_new = []
rr = 0.01
while (1):
    r = radius_l / rr
    radius_d_old.append(r)
    
    rscale_t = radius_l / rr
    r = rscale_t *  (1.0 - rr)
    radius_d_new.append(r)
    radius_ratio.append(rr)
    rr += 0.01
    if(rr > 1.0):
        break
    
plt.subplots()
plt.plot(radius_ratio, radius_d_old, label= 'old')
plt.plot(radius_ratio, radius_d_new, label ='new')
legend = plt.legend(loc='upper center', shadow=True)
plt.title('parameter surface')
plt.xlabel('rr')
plt.ylabel('r_d')
plt.savefig('./parameter_surface.png', format='png')



radius_ratio = 0.2
radius_l = []
radius_d_old = []
radius_d_new = []
r_l = 0.01
while (1):
    r = r_l / radius_ratio
    radius_d_old.append(r)
    
    rscale_t = r_l / radius_ratio
    r = rscale_t *  (1.0 - radius_ratio)
    radius_d_new.append(r)
    radius_l.append(r_l)
    r_l += 0.01
    if(r_l > 5.0):
        break
    

plt.subplots()
plt.plot(radius_l, radius_d_old, label="old")
plt.plot(radius_l, radius_d_new, label='new')
legend = plt.legend(loc='upper center', shadow=True)
plt.title('parameter surface')
plt.xlabel('radius_l')
plt.ylabel('r_d')
plt.savefig('./parameter_surface2.png', format='png')
plt.show()




    
    


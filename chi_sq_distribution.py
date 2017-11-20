import os
import subprocess
from subprocess import call
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as mt
import matplotlib.patches as mpatches
import random
from nbody_functional import *
random.seed(a = 12345678)



def chi_sq_dist_plot():
    k = 50.0
    cf = (k / 2.0) - 1.0
    x = 0.1
    xs = []
    func1s = []
    func2s = []
    func3s = []
    while(1):
        func1 = cf * mt.log(x) - x / 2.0
        func2 = func1 - cf * (mt.log(2.0 * cf) - 1.0) 
        if(x < 2.0 * cf):
            func3 = 0.0
        else:
            func3 = func2
            
        xs.append(x)
        func1s.append(func1)
        func2s.append(func2)
        func3s.append(func3)
        if(x > 1000):
            break
        else:
            x += 0.1
    plt.ylim((-200, 100))
    plt.xlim((0, 400))
    plt.xlabel(r'N$_{\sigma}$$^{2}$')
    plt.ylabel('Probability')
    #plt.plot(xs, func1s)
    #plt.plot(xs, func2s)
    plt.plot(xs, func3s)
    plt.savefig('/home/sidd/Desktop/research/quick_plots/chi_sq_func3', format='png')
    #plt.show()
# #
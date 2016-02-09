#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Command Line Args
#input = sys.argv[1];

lines = []
lines = open('quick_plots/heat_map_test_data.txt').readlines();
lines = lines[0: len(lines)]
mass  = [] 
m_r   = []
like  = []

for line in lines:
    tokens = line.split()
    if tokens:
        m = float(tokens[0])
        mr = float(tokens[1])
        l = float(tokens[2])
        
        mass.append(m)
        m_r.append(mr)
        like.append(l)


#x = np.array(mass)
#y = np.array(mr)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(mass, m_r, like, linewidth = 3.2, linestyle = '--')
#ax.contour(x, y, like)
#plt.xlim((0.0, 100))
#plt.ylim((0.0, 0.25))
#plt.zlim((0.0, -25))
#ax.view_init(elev=20, azim=60)
#ax.dist = 11


Z=np.array(((1,2,3,4,5),(4,5,6,7,8),(7,8,9,10,11)))
im = plt.imshow(Z, cmap='hot')
plt.colorbar(im, orientation='horizontal')
plt.show()

#x = []; y = []; likelihood = [];

#like_min = 0.0;
#like_max = -10.0;
#mass_min = 5.0;
#mass_max = 0.0;
#m_r_min = 5.0;
#m_r_max = 0.0;
#xparam = 0.0;
#count = 0;

#extent = [ mass_min, mass_max, m_r_min, m_r_max ];
#print "%3f %3f %3f %3f" % (mass_min, mass_max, m_r_min, m_r_max);
#x = np.array(x).transpose();

##plt.imshow(x, extent=extent, origin='lower', interpolation='spline16', 
#plt.imshow(x, extent=extent, origin='lower', interpolation='none',vmin=like_min, vmax=like_max, cmap='gray');
#plt.colorbar();
#plt.contour(x, 10, extent=extent, vmin=like_min, vmax=like_max, cmap='autumn');
#plt.xlabel("Theta");
#plt.ylabel("Phi");
#plt.title("Theta, Phi Parameter Sweep");
#plt.xlim([extent[0], extent[1]]);
#plt.ylim([extent[2], extent[3]]);
#plt.grid();
#plt.show();
#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#this plots the distribution heat map with matplotlib

#Command Line Args
#input = sys.argv[1];

lines = []
lines = open('quick_plots/hists_outputs/heat_map_test_data.txt').readlines();
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


## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #distrupt_pyplot = n
    #if(distrupt_pyplot == True):
        #lines = []
        #lines = open('quick_plots/hists_outputs/' + histogram).readlines();
        #lines = lines[40:len(lines)]
        #sim_lx = []
        #sim_by = []
        #sim_nz = []
        #for line in lines:
            #tokens = line.split();
            #if tokens: #tests to make sure tokens is not empty
                #lda = float(tokens[1])
                #bta = float(tokens[2])
                #cts = float(tokens[3])
                #sim_lx.append(lda)
                #sim_by.append(bta)
                #sim_nz.append(cts)
        #print("%f \t %f \t %f\n" % (len(sim_lx), len(sim_by), len(sim_nz)))
        
        #sim_l = np.asarray(sim_lx)
        #sim_b = np.asarray(sim_by)
        #sim_n = np.asarray(sim_nz)
        
        #nx = sim_l.max() - sim_l.min() + 1
        #ny = sim_b.max() - sim_b.min() + 1
        #Z = np.zeros((nx,ny)) 
        #print("%f \n" % (Z.shape[0]))
        
        #assert sim_l.shape == sim_b.shape == sim_n.shape
        #for i in range(len(sim_l)):
            #Z[sim_l[i] - sim_l.min()][sim_b[i] - sim_b.min()] = sim_n[i] 

        #fig = plt.figure()
        #plt.scatter(sim_l, sim_b, c=sim_n)
        ##plt.show()
        
        #plt.pcolor(np.arange(nx), np.arange(ny), Z, cmap = plt.cm.Reds)
        #plt.colorbar()
        #plt.xlim(0, sim_l.max() - sim_l.min())
        #plt.ylim(0, sim_b.max() - sim_b.min())
        
        #xlabels = np.arange(sim_l.min(), sim_l.max(), Nspacingx) # define Nspacing accordingly 
        #ylabels = np.arange(sim_b.min(), sim_b.max(), Nspacingy) 
        #plt.xticks(np.arange(0, sim_l.max() - sim_l.min(), Nspacingx), xlabels)
        #plt.yticks(np.arange(0, sim_b.max() - sim_b.min(), Nspacingy), ylabels)

        #plt.savefig('quick_plots/distruption2.png', format='png')
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
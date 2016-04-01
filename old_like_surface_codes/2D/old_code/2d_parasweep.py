#! /usr/bin/python
import os
#from subprocess import call
h= open('./data/progress.dat', 'w')
mass_counter=1.0
mass=str(mass_counter)
massratio_counter=0.1
massratio=str(massratio_counter)
counter=1

while mass_counter < 191:
	massratio_counter=0.1
	massratio=str(massratio_counter)
	while massratio_counter < 0.75:
	  os.system(" ~/research/nbody_test_10k/bin/milkyway_nbody \
        	-f ~/research/lua/EMD_10k_isotropic2_1_48.lua \
		-h ~/research/like_surface/histogram_in_seed125896_10kEMD_4_1_p5_p2_30_p2.hist \
	        -o ~/research/nbody_test_10k/bin/output.out \
	        -z ~/research/like_surface/histogram_out_seed491349_1kEMD_4_1_p5_p2_30_sweep.hist \
	        -n 10 -x -e  491349 -i 4 1 0.5 0.2 "+ mass +" "+ massratio + " \
	        2>>~/research/like_surface/2d_mass_massratio_sweep/data/out.txt")
	  h.write( str(counter)+ "\n")
	  counter=counter+1
	  massratio_counter=massratio_counter+0.02
	  massratio=str(massratio_counter)
	mass_counter=mass_counter + 10
	mass=str(mass_counter)
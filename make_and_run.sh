#!/bin/bash          
# 	rm -r nbody_test
# 	mkdir nbody_test
	rm ~/Desktop/research/nbody_test/bin/milkyway_nbody
	cd ~/Desktop/research/nbody_test
	cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
	make -j 

	cd ~/Desktop/research/nbody_test/bin
# 	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-o output_test.out \
	-z ~/Desktop/research/histogram_20kEMD_v150.hist \
	-n 4 -x  -e  125896  -i 0.001 1 0.5 0.2 30 .2 \
#  	2>>~/Desktop/research/piped_output.txt  
# 	rm ./milkyway_nbody

        mv rho.txt  ~/Desktop/research/quick_plots
#         mv rho2.txt  ~/Desktop/research/quick_plots
#         mv dist.txt  ~/Desktop/research/quick_plots
#         mv dist_1.txt  ~/Desktop/research/quick_plots
#         mv dist_single_masses1.txt ~/Desktop/research/quick_plots
#         mv dist_single_masses2.txt ~/Desktop/research/quick_plots
        mv pot.txt ~/Desktop/research/quick_plots
        cd ~/Desktop/research/gnuplot_scripts
        gnuplot rho_plot.gnuplot
#         gnuplot dist_plot.gnuplot 
#         gnuplot theory_dist_plot.gnuplot
        gnuplot pot_plot.gnuplot
        
	cd ~/Desktop/research	 
	python outputparser.py ~/Desktop/research/nbody_test/bin/output_test.out
# 	rm ~/Desktop/research/nbody_test/bin/output.out
	
# 	valgrind --tool=callgrind
# 	insert above before ./
# 	cd ~/Desktop/research/nbody_test/bin
# 	callgrind_annotate --inclusive=yes --auto=yes callgrind.out

# 	/Desktop/research/lua/EMD_20k_isotropic_1_50.lua 125896   -e 125896
# 	/Desktop/research/lua/Null_even.lua
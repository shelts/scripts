#!/bin/bash          
# 	rm -r nbody_test
# 	mkdir nbody_test
	cd ~/Desktop/research/nbody_test
	cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
	make -j 

	cd ~/Desktop/research/nbody_test/bin

	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150.hist \
	-n 4 -x  -P -e 125896 -i 0.01 1 0.4 0.2 11 .2 \
	2>>~/Desktop/research/piped_output.txt
	
	cp output_0gy.out ~/Desktop/research/data_testing
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e 125896 -i 0.01 1 0.4 0.2 11 .2\
	2>>~/Desktop/research/piped_output.txt
	
	
	
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150.hist \
	-n 4 -x -P -e 125896 -i 4 1 0.4 0.2 11 .2 \
	2>>~/Desktop/research/piped_output.txt
	
	cp output_0gy.out ~/Desktop/research/data_testing
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P -e 125896  -i 4 1 0.4 0.2 11 .2\
	2>>~/Desktop/research/piped_output.txt
	
	#######################################################
		time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150.hist \
	-n 4 -x -P  -i 0.01 1 0.4 0.2 11 .2 \
	2>>~/Desktop/research/piped_output.txt
	
# 	cp output_0gy.out ~/Desktop/research/data_testing
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P -i 0.01 1 0.4 0.2 11 .2\
	2>>~/Desktop/research/piped_output.txt
	
	
	
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150.hist \
	-n 4 -x -P  -i 4 1 0.4 0.2 11 .2 \
	2>>~/Desktop/research/piped_output.txt
	
# 	cp output_0gy.out ~/Desktop/research/data_testing
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/EMD_20k_isotropic_1_50.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P -i 4 1 0.4 0.2 11 .2\
	2>>~/Desktop/research/piped_output.txt
	
	
	
	
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	
	

# 	/Desktop/research/lua/EMD_50k_isotropic_1_48.lua
# 	/Desktop/research/lua/Null_even.lua
	

	

 

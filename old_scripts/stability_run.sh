#!/bin/bash          
# 	rm -r nbody_test
# 	mkdir nbody_test
	cd ~/Desktop/research/nbody_test
	cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
	make -j 
        
#         cd ~/Desktop/research/data_testing
#         bash cleanse.sh
        
	cd ~/Desktop/research/nbody_test/bin
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-o output_0gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 0.00001 1 0.5 0.2 30 0.2
# 	2>>~/Desktop/research/piped_output.txt 
	cp output_0gy.out ~/Desktop/research/data_testing/sim_outputs
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_p25gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 0.25 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_p25gy.out ~/Desktop/research/data_testing/sim_outputs
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_p5gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 0.5 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_p5gy.out ~/Desktop/research/data_testing/sim_outputs
	
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_p75gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 0.75 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_p75gy.out ~/Desktop/research/data_testing/sim_outputs
	
	
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_1gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 1 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_1gy.out ~/Desktop/research/data_testing/sim_outputs

# 
	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_2gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 2 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_2gy.out ~/Desktop/research/data_testing/sim_outputs

	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_3gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P  -e  125896 -i 3 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_3gy.out ~/Desktop/research/data_testing/sim_outputs


	time  ./milkyway_nbody \
	-f ~/Desktop/research/lua/Null_even.lua \
	-h ~/Desktop/research/histogram_20kEMD_v150.hist \
	-o output_4gy.out \
	-z ~/Desktop/research/histogram_20kEMD_v150_compare.hist \
	-n 4 -x -P -e  125896   -i 4 1 0.5 0.2 30 0.2 \
# 	2>>~/Desktop/research/piped_output.txt
	cp output_4gy.out ~/Desktop/research/data_testing/sim_outputs
	
	cd ~/Desktop/research/data_testing
	bash stability_test.sh

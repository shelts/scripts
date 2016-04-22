#!/bin/bash          
# 	cp ~/Desktop/MW-research/nbody_test/bin/output.out ./
        python outputparser.py ./output_0gy.out  0gy
        g++ -std=c++11 output_test.cpp -o output_test
        time ./output_test  0.5 0.2 30.0 0.2 #all parameters excluding time, forward and backward
        gnuplot plot.gnuplot
# 	xdg-open plots/radii_distribution_dark.jpeg        
        
          
        
#         mkdir run1
#         mv binned_data run1
#         mv plots run1
#         mv raw_data run1
#         mkdir binned_data
#         mkdir plots
#         mkdir raw_data
        
# 	xdg-open run1/plots/radii_distribution.jpeg
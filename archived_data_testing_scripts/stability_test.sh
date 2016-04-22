#!/bin/bash          
# 	cp ~/Desktop/MW-research/nbody_test/bin/output.out ./
        python outputparser.py ./sim_outputs/output_0gy.out  0gy
        g++ -std=c++11 output_test.cpp -o output_test
        ./output_test 0 1 0.5 0.2 30 .2
#         2>>~/Desktop/research/data_testing/piped_output.txt  
        
        python outputparser.py ./sim_outputs/output_p25gy.out  p25gy
        ./output_test p25 1 0.5 0.2 30 0.2  
        
        python outputparser.py ./sim_outputs/output_p5gy.out  p5gy
        ./output_test p5 1 0.5 0.2 30.0 0.2  
        
        python outputparser.py ./sim_outputs/output_p75gy.out  p75gy
        ./output_test p75 1 0.5 0.2 30.0 0.2  
        
        python outputparser.py ./sim_outputs/output_1gy.out  1gy
        ./output_test 1 1 0.5 0.2 30.0 0.2  
        
        python outputparser.py ./sim_outputs/output_2gy.out  2gy
        ./output_test 2 1 0.5 0.2 30.0 0.2  
        
        python outputparser.py ./sim_outputs/output_3gy.out  3gy
        ./output_test 3 1 0.5 0.2 30.0 0.2  
        
        python outputparser.py ./sim_outputs/output_4gy.out  4gy
        ./output_test 4 1 0.5 0.2 30.0 0.2  
        
        
        gnuplot gnuplot_scripts/stability_plots.gnuplot 
        gnuplot gnuplot_scripts/theta.gnuplot
        gnuplot gnuplot_scripts/phi.gnuplot
        gnuplot gnuplot_scripts/vel.gnuplot
        gnuplot gnuplot_scripts/v_vs_r.gnuplot
        gnuplot gnuplot_scripts/vel_theory_binned.gnuplot
        gnuplot gnuplot_scripts/vel_phi.gnuplot
        gnuplot gnuplot_scripts/vel_theta.gnuplot
# 	xdg-open run1/plots/radii_distribution.jpeg
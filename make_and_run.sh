#!/bin/bash          
    rm -r nbody_test
    mkdir nbody_test
    cd ~/Desktop/research/nbody_test
    cmake  -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
    make -j 

    cd ~/Desktop/research/nbody_test/bin
    
    time  ./milkyway_nbody -i\
    -f ~/Desktop/research/lua/EMD_20k_isotropic_1_54.lua \
    -o output_test.out \
    -n 8 -e 9876543 -u \
    --visualizer-args '-r -q '\
    -i 4 .6 0.2 0.2 30 .2 \
#     >~/Desktop/research/piped_output.txt  \
#     rm ./milkyway_nbody


#     mv rho.txt  ~/Desktop/research/quick_plots
#     mv dist.txt  ~/Desktop/research/quick_plots
#     mv dist2.txt  ~/Desktop/research/quick_plots
#     mv dist3.txt  ~/Desktop/research/quick_plots
#     mv pot.txt ~/Desktop/research/quick_plots
#     mv fun.txt ~/Desktop/research/quick_plots
#     mv fun2.txt ~/Desktop/research/quick_plots
#     mv denom.txt ~/Desktop/research/quick_plots
#     mv num.txt ~/Desktop/research/quick_plots
#     cd ~/Desktop/research/quick_plots
#     gnuplot rho_plot.gnuplot
#     gnuplot dist_plot.gnuplot 
#     gnuplot pot_plot.gnuplot
#     gnuplot fun.gnuplot

#     cd ~/Desktop/research	 
# python outputparser.py ~/Desktop/research/nbody_test/bin/output_test.out
# rm dark_matter.dat
# rm light_matter.dat
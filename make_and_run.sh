#!/bin/bash          
#     rm -r nbody_test
#     mkdir nbody_test
#     cd ~/Desktop/research/nbody_test
#     cmake  -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 

    cd ~/Desktop/research/nbody_test/bin
    
    time  ./milkyway_nbody -i\
    -f ~/Desktop/research/lua/EMD_20k_isotropic_1_54.lua \
    -o output_test.out \
    -n 8 -e 9876543 \
    --visualizer-args '-r -q '\
    -i 0.01 .6 0.2 0.2 30 .2 \
#     2>>~/Desktop/research/piped_output.txt  \
#     rm ./milkyway_nbody
    cd $r
    python outputparser.py ./nbody_test/bin/output_test.out
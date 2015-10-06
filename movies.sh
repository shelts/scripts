#!/bin/bash          
#     rm -r nbody_test
#     mkdir nbody_test
#     rm ~/Desktop/research/nbody_test/bin/milkyway_nbody
#     cd ~/Desktop/research/nbody_test
#     cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 

    cd ~/Desktop/research/nbody_test/bin

    time  ./milkyway_nbody \
    -f ~/Desktop/research/lua/Null_even.lua \
    -o output_test.out \
    -n 6 -x -u \
    --visualizer-args --print-frames=test \
    -e 123456 -i 4 1 0.5 0.2 30 .2 \
#     2>>~/Desktop/research/piped_output.txt  
#     rm ./milkyway_nbody


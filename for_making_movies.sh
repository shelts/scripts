#!/bin/bash          
#     rm -r nbody_test
#     mkdir nbody_test
#     rm ~/Desktop/research/nbody_test/bin/milkyway_nbody
#     cd ~/Desktop/research/nbody_test
#     cmake  -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 

    cd ~/Desktop/research/nbody_test/bin
    
    time  ./milkyway_nbody \
    -f ~/Desktop/research/lua/EMD_20k_isotropic_1_52.lua \
    -o output_test.out \
    -n 8 -x -u \
    --visualizer-args '-r -q' \
    -e 123456 -i 4 1 0.5 0.2 30 .2 \
#     2>>~/Desktop/research/piped_output.txt  
#     rm ./milkyway_nbody

    cd ~/Desktop/research
    mkdir frames
    mv nbody_test/bin/Frame* ./frames
    cd frames
    mogrify -resample 72x72 -resize 256x256 *.tga
    convert -delay 10 -loop 0 Frame*.tga animation.gif

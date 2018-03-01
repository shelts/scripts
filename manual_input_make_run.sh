#!/bin/bash          
#/* Copyright (c) 2016 Siddhartha Shelton */
#     rm -r nbody_test
#     mkdir nbody_test
#     cd nbody_test
#     cmake  -DCMAKE_BUILD_TYPE=Release -DNBODY_DEV_OPTIONS=ON -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 


    cd ~/Desktop/research/nbody_test/bin
    



    ./milkyway_nbody \
    -f ~/Desktop/research/lua/halo_object_dev.lua \
    -o some_output.out \
    -z path_to_output_hist \
    -n 8 -b  -u\
    -i 4.0 1 0.2 0.5 12 0.5 ~/Desktop/research/disk.out\


#if you run:
#     ./milkyway_nbody --help\
# it wil show you what all the flags mean
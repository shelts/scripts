#!/bin/bash          
#/* Copyright (c) 2016 Siddhartha Shelton */

rebuild=false
run=true
run_compare=false
compare_only=false
manual_input=false
get_flag_list=false

if $rebuild
then
#     rm -r nbody_test
#     mkdir nbody_test
    cd nbody_test
    cmake  -DCMAKE_BUILD_TYPE=Release -DNBODY_DEV_OPTIONS=ON -DNBODY_GL=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
    make -j 
fi

cd nbody_test/bin
if $run 
then
    ./milkyway_nbody \
    -f full_control.lua \
    -h path_to_input_hist \
    -o some_output.out \
    -n 8 -b  -P -u\
    -i 3.95 1.0 0.2 0.2 12 0.2 \
    
fi

if $run_compare
then
    ./milkyway_nbody \
    -f full_control.lua \
    -o some_output.out \
    -h path_to_input_hist \
    -z path_to_output_hist \
    -n 8 -b  -P -u\
    -i 3.95 1.0 0.2 0.2 12 0.2 \

fi

#OPTIONS:
#-s -> compare using only emd and cost component
#-S -> use emd, cost, beta dispersion
#-V -> use emd, cost, velocity dispersion
#-D -> use emd, cost, beta dispersion and velocity dispersion
if $compare_only 
then
    ./milkyway_nbody \
    -h path_to_input_hist \
    -S path_to_output_hist \

fi


# if you run:
if $get_flag_list
then
    ./milkyway_nbody --help
# it wil show you what all the flags mean
fi

if $manual_input
then
    ./milkyway_nbody \
    -f ~/Desktop/research/lua/halo_object_dev.lua \
    -o some_output.out \
    -z path_to_output_hist \
    -n 8 -b  -u\
    -i 4.0 1 0.2 0.5 12 0.5 ~/Desktop/research/disk.out\

fi
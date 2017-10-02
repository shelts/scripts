#!/bin/bash          
#/* Copyright (c) 2016 Siddhartha Shelton */

    
# windows:

    ./milkyway_nbody_openmpOFF.exe\
    -f EMD_v166.lua \
    -h hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17.hist \
    -z hist_test.hist \
    -n 8 -b  \
    -i 3.95 1.0 0.2 0.2 12 0.2\

    ./milkyway_nbody_openmpOFF.exe\
    -f EMD_v166.lua \
    -h hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17.hist \
    -z hist_test.hist \
    -n 8 -b  \
    -i 3.97 1.0 0.3 0.3 13 0.3\

    
     ./milkyway_nbody_openmpON.exe\
    -f EMD_v166.lua \
    -h hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17.hist \
    -z hist_test.hist \
    -n 8 -b  \
    -i 3.95 1.0 0.2 0.2 12 0.2\

    ./milkyway_nbody_openmpON.exe\
    -f EMD_v166.lua \
    -h hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17.hist \
    -z hist_test.hist \
    -n 8 -b  \
    -i 3.97 1.0 0.3 0.3 13 0.3\
    
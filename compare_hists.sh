#!/bin/bash          
#     rm -r nbody_test
#     mkdir nbody_test
#     rm ~/Desktop/research/nbody_test/bin/milkyway_nbody
#     cd ~/Desktop/research/nbody_test
#     cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 

    cd ~/Desktop/research/nbody_test/bin

    time  ./milkyway_nbody --help \
    -h ~/Desktop/research/light_matter_bins_0gy.hist\
    -s ~/Desktop/research/light_matter_bins_0gy.hist


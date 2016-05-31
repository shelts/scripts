#!/bin/bash    



cd nbody_test/bin
./milkyway_nbody_1.62_x86_64-pc-linux-gnu__mt \
    -f ~/research/lua/EMD_v162.lua \
    -z ~/research/quick_plots/hists/mt_check_of_input.hist \
    -i 3.87427734322731 0.948765315488652 0.356895748596523 .145236987452136 10.1548765394315 0.185215358746843 \

    
./milkyway_nbody_1.62_x86_64-pc-linux-gnu \
    -f ~/research/lua/EMD_v162.lua \
    -z ~/research/quick_plots/hists/st_check_of_input.hist \
    -i 3.87427734322731 0.948765315488652 0.356895748596523 .145236987452136 10.1548765394315 0.185215358746843 \
    
    
    
    
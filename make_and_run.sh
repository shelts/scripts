#!/bin/bash          
#/* Copyright (c) 2016 Siddhartha Shelton */
#     rm -r nbody_test
#     mkdir nbody_test
#     cd ~/Desktop/research/nbody_test
#     cmake  -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 
#     ./one_script.py
    cd ~/Desktop/research/nbody_test/bin
    
#     time  ./milkyway_nbody \
#     -f ~/Desktop/research/lua/EMD_v162.lua \
#     -o output_0gy.out \
#     -z ~/Desktop/research/quick_plots/hists/hist_test.hist \
#     -n 8 -b   \
#     -i 0.0001 1.0 0.2 0.5 6 0.5\

#     rm ~/Desktop/research/data_testing/sim_outputs/output_0gy.out
#     cp output_0gy.out ~/Desktop/research/data_testing/sim_outputs/output_0gy.out
#     cd ~/Desktop/research/data_testing
#     ./stability_test.py 1.0 0.2 0.5 6 0.5


    time  ./milkyway_nbody \
    -f ~/Desktop/research/lua/EMD_v162.lua \
    -o output_0gy.out \
    -z ~/Desktop/research/quick_plots/hists/hist_test.hist \
    -n 8 -b  -u \
    -i 4.0 1.0 0.2 0.5 6 0.5\


#     valgrind --tool=callgrind callgrind_annotate --threshold=100 --tree=both callgrind.out.* ./milkyway_nbody_162j \
#     -h  ~/Desktop/research/quick_plots/hists/hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16.hist \
#     -s ~/Desktop/research/quick_plots/hists/windows_multithreaded5.hist \
#     2>> ~/Desktop/research/piped.txt
    
# cp ~/Desktop/research/quick_plots/hists/hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16.hist ./correct.hist
# cp ~/Desktop/research/quick_plots/hists/OS_test/windows_multithreaded5.hist ./compare.hist
# valgrind -v --track-origins=yes ./milkyway_nbody_VM \
# -h  correct.hist \
# -s compare.hist \
# 2>> ~/Desktop/research/piped1.txt
    
   
#     gdb --core=COREFILE --exec=EXECFILE ./milkyway_nbody_162j \
#     -h  ~/Desktop/research/quick_plots/hists/hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16.hist \
#     -s ~/Desktop/research/quick_plots/hists/windows_multithreaded5.hist \
#     2>> ~/Desktop/research/piped.txt

# ulimit -c unlimited
# ./nbody_test/bin/milkyway_nbody_vm -h  ~/Desktop/research/quick_plots/hists/hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16.hist -s ~/Desktop/research/quick_plots/hists/OS_test/windows_multithreaded5.hist 
# # gdb bin/milkyway_nbody_VM_debug core
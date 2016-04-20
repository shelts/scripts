#!/bin/bash          
#     rm -r nbody_test
#     mkdir nbody_test
#     cd ~/Desktop/research/nbody_test
#     cmake  -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/
#     make -j 

    cd ~/Desktop/research/nbody_test/bin
    
    time  ./milkyway_nbody --help\
    -f ~/Desktop/research/lua/EMD_20k_v158_fixed_seed.lua \
    -o output_test.out \
    -z ~/Desktop/research/quick_plots/hists/hist_test.hist \
    -n 8 -u  \
    -i 4.0 1.0 0.2 0.2 12 .2 \
#     2>>~/Desktop/research/piped_output2.txt  \
# #     rm ./milkyway_nbody
#     cd $r
#     python outputparser.py ./nbody_test/bin/output_test.out
# #     --visualizer-args '-r -q '\
# 
# rm dark_matter.dat light_matter.dat
# # ./hist_check.py
# # 9876543
# 
# cd quick_plots
# ./quick_plot.py

#     FILE * file;
#     file = fopen("new_binary.txt", "w");
#     for(int i = 0; i < nbody; i++)
#         fprintf(file, "%22.15f\t%22.15f\t%22.15f\t%22.15f\t%22.15f\t%22.15f\n", bodies[i].bodynode.pos.x, bodies[i].bodynode.pos.y, bodies[i].bodynode.pos.z, bodies[i].vel.x, bodies[i].vel.y, bodies[i].vel.z);
#     fclose(file);
#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
import math
#This creates a histrogram and matches to another histogram.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False

#args = [3.945, 0.9862, 0.2, 0.2, 12, 0.2] #for hist with dark matter
args = [0.000000000000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [4.0, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter

sim_time      = str(args[0])
back_time     = str(args[1])
r0            = str(args[2])
light_r_ratio = str(args[3])
mass_l        = str(args[4])
mass_ratio    = str(args[5])


#    SWITCHES  #
run_nbody = n
remake    = n

plot_hists  = n
match_histograms = y
calc_chi_sq = y


#    Histogram names     #
histogram_mw_1d_new = "tidal_histogram_EMD_20k_v154_ft3p945_rt0p9862_r0p2_rr0p2_ml12_mr0p2_2_9_16"
histogram_mw_1d_newer = "tidal_histogram_EMD_20k_v156_ft3p9_rt0p9862_r0p2_rr0p2_ml12_mr0p2_3_8_16"

with_lua_correction_on_old_binary = 'with_lua_correction_on_old_binary'
with_correction_on_new_binary = 'with_correction_on_new_binary'

#    histograms1 for runs #
histogram_for_nbody_run = with_correction_on_new_binary + '.hist'

match_hist_correct = with_lua_correction_on_old_binary + '.hist'
match_hist_compare = with_correction_on_new_binary + '.hist'

lua = "EMD_20k_v154_fixed_seed.lua"
version = ['_154', '']
time  = "3945"
names = ['ipv_old_binary0gy.txt', 'ipv_new_binary0gy.txt']
outputs = [with_lua_correction_on_old_binary + time + "gy.out", with_correction_on_new_binary + time + "gy.out"]
hists   = [with_lua_correction_on_old_binary + time + "gy.hist", with_correction_on_new_binary + time + "gy.hist"]
folder = "outputs/"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def run(version, name, output, hist, versioning):
    print('running nbody')
    if(remake == True):
        os.chdir("./")
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    ~/Desktop/research/milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    os.system(" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + version + " \
        -f ~/Desktop/research/lua/" + lua + " \
        -z ~/Desktop/research/quick_plots/hists/" + hist + " \
        -o ~/Desktop/research/quick_plots/outputs/" + output + " \
        -n 8 -x  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " " + str(versioning) + " \
        > " + name)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def plot(hist1, hist2):
    os.system("./plot_matching_hist.py " + hist1 + " " + hist2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def match(hist1, hist2, version):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" ~/Desktop/research/nbody_test/bin/milkyway_nbody" + version  
          + " -h ~/Desktop/research/quick_plots/hists/" + hist1
          + " -s ~/Desktop/research/quick_plots/hists/" + hist2], shell=True)
    print hist1, "\n", hist2
print "\n"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
def main():
    if(run_nbody == True):
        run(version[0], names[0], outputs[0], hists[0], 0)
        run(version[1], names[1], outputs[1], hists[1], 1)
        
    if(match_histograms == True):
        match(hists[0], hists[0], version[0])
        match(hists[1], hists[1], version[0])
        
        match(hists[0], hists[0], version[1])
        match(hists[1], hists[1], version[1])
    
    if(plot_hists == True):
        plot(hists[0], hists[1])
    
    os.system("mv " + names[0] + " " + names[1] + " quick_plots")
    if(calc_chi_sq == True):
        os.system("./old_new_binary_chi_sq.py " + folder + outputs[0] + " " + folder + outputs[1] + " " + "output")
main()
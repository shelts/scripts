#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # # # #\#
                #    One script to rule them all.   #
                #    One script to call them        #
                #    One script to run them.        #
                #    And in the folder, bind them   #
                #\# # # # # # # # # # # # # # # # #/#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import subprocess
from subprocess import call
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as mt
import matplotlib.patches as mpatches
import random
random.seed(a = 12345678)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
#args_run_comp = [3.764300006400000, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run_comp = [4.037308903030000, 0.98, 0.2, 0.2, 12, 0.2]
args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 
args_run_comp = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run_comp = [2.08, 0.98, 0.2, 0.3, 12, 0.45] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#              Standard Run switches          #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = n                 #
match_histograms          = n                 #
run_and_compare           = n                 #
run_from_checkpoint       = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
#              Hist Plot Switches             #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_hists                = n                 #
plot_veldisp_switch       = n                 #
vlos_plot_switch          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
#              Non-Hist Plot Switches         #
# # # # # # # # # # # # # # # # # # # # # # # #
lb_plot_switch            = n                 #
lambda_beta_plot_switch   = n                 #

plot_adjacent             = y                 #
plot_overlapping          = y                 #
# # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # #
#              possible tests                 #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_disp_switch      = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_some_hists_switch    = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
stabity_test_switch       = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
test_vel_theta_binning_switch = n
ridge_probe_switch        = n
plot_all_hists_switch     = n                 #
check_timestep_switch     = n                 #
quick_calculator_switch   = n                 #
half_mass_radius_switch   = y                 #
proper_motion_check_switch = n
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Circuitry           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Histogram names      #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'

#    histograms for runs  #
correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct'
run_test = 'arg_3.95_0.98_0.2_0.2_12_0.2'

#correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_postchange'
#run_test = 'run_test_postchange'

#    hist to match against for compare after run  #
correct_hist = correct

#    hist name for the nbody run   #
histogram_for_nbody_run = correct
histogram_for_nbody_run_and_compare = run_test

#    if you are just matching, these are the two hists #
match_hist_correct = histogram_for_nbody_run
match_hist_compare = histogram_for_nbody_run_and_compare
plot_name = histogram_for_nbody_run


output = histogram_for_nbody_run
output_run_compare = histogram_for_nbody_run_and_compare
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#    run specfics   #
#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
lua = "full_control.lua"
#lua = "EMD_v164.lua"

#    pathways  #
#I am tired of constantly adapting it for the servers
lmc_dir = '~/research/'
sid_dir = '/home/sidd/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = sid_dir
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class nbody_outputs:#a class that takes in data from nbody output files and makes them available
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_data()
        
    def get_data(self):
        self.xs = []; self.ys = []; self.zs = []
        self.ls = []; self.bs = []; self.rs = []
        self.vxs = []; self.vys = []; self.vzs = []
        self.vls = []; self.ms = []; self.tps = []
        
        f = open(self.file_name, 'r')
        read_data = False
        
        for line in f:
            if (line.startswith("# ignore")):
                read_data = True
                continue
            if(line.startswith("</bodies>")):
                break
            if(read_data):
                ss = line.split(', ')
                ty = int(ss[0])
                x = float(ss[1])
                y = float(ss[2])
                z = float(ss[3])
                
                l = float(ss[4])
                b = float(ss[5])
                r = float(ss[6])
                
                vx = float(ss[7])
                vy = float(ss[8])
                vz = float(ss[9])
                
                m  = float(ss[10])
                vl = float(ss[11])
                self.xs.append(x); self.ys.append(y); self.zs.append(z)
                self.ls.append(l); self.bs.append(b); self.rs.append(r)
                self.vxs.append(vx); self.vys.append(vy); self.vzs.append(vz)
                self.tps.append(ty); self.ms.append(m); self.vls.append(vl)
            
        f.close()
        
    def dark_light_split(self):#splits the data between light and dark
        self.light_x , self.light_y , self.light_z    = ([] for i in range(3))
        self.light_l , self.light_b , self.light_r    = ([] for i in range(3))
        self.light_vx , self.light_vy , self.light_vz = ([] for i in range(3))
        self.light_vl, self.light_m                   = ([] for i in range(2))
        
        self.dark_x , self.dark_y , self.dark_z       = ([] for i in range(3))
        self.dark_l , self.dark_b , self.dark_r       = ([] for i in range(3))
        self.dark_vx , self.dark_vy , self.dark_vz    = ([] for i in range(3))
        self.dark_vl, self.dark_m                     = ([] for i in range(2))
        
        for i in range(0, len(self.xs)):
            if(self.tps[i] == 0):
                self.light_x.append(self.xs[i])
                self.light_y.append(self.ys[i])
                self.light_z.append(self.zs[i])
                
                self.light_l.append(self.ls[i])
                self.light_b.append(self.bs[i])
                self.light_r.append(self.rs[i])
                
                self.light_vx.append(self.vxs[i])
                self.light_vy.append(self.vys[i])
                self.light_vz.append(self.vzs[i])
                
                self.light_vl.append(self.vls[i])
                self.light_m.append(self.ms[i])
                
            if(self.tps[i] == 1):
                self.dark_x.append(self.xs[i])
                self.dark_y.append(self.ys[i])
                self.dark_z.append(self.zs[i])
                
                self.dark_l.append(self.ls[i])
                self.dark_b.append(self.bs[i])
                self.dark_r.append(self.rs[i])
                
                self.dark_vx.append(self.vxs[i])
                self.dark_vy.append(self.vys[i])
                self.dark_vz.append(self.vzs[i])
                
                self.dark_vl.append(self.vls[i])
                self.dark_m.append(self.ms[i])    
                
    def rescale_l(self):#to change l range from [0:360] to [-180:180]
        for i in range(0, len(self.ls)):
            if(self.ls[i] > 180.0):
                self.ls[i] = self.ls[i] - 360.0
    
    def convert_lambda_beta(self, split):#to convert l,b to lambda, beta
        if(split):#if the data was split between light and dark
            self.light_lambda = []; self.light_beta = []
            self.dark_lambda  = []; self.dark_beta = []
        else:
            self.betas   = []
            self.lambdas = []
        
        for i in range(0, len(self.ls)):
            lmbda_tmp, beta_tmp = self.convert_to_Lambda_Beta(self.ls[i], self.bs[i], self.rs[i], False)
            if(split):
                if(self.tps[i] == 0):
                    self.light_lambda.append(lmbda_tmp)
                    self.light_beta.append(beta_tmp)
                    
                if(self.tps[i] == 1):
                    self.dark_lambda.append(lmbda_tmp)
                    self.dark_beta.append(beta_tmp)
            else:
                self.lambdas.append(lmbda_tmp)
                self.betas.append(beta_tmp)
            
        
        
    def convert_to_Lambda_Beta(self, x1, x2, x3, cartesian):#can convert l,b or x,y,z to lambda beta
        phi   = mt.radians(128.79)
        theta = mt.radians(54.39)
        psi   = mt.radians(90.70)
        
        if(cartesian):
            x_coor = x1
            y_coor = x2
            z_coor = x3
            x_coor += 8.0 #convert to solar centric
        else:
            l = mt.radians(x1)
            b = mt.radians(x2)
            r = x3
            
            x_coor = r * mt.cos(l) * mt.cos(b) #this is solar centered x
            y_coor = r * mt.sin(l) * mt.cos(b)
            z_coor = r * mt.sin(b)
        
        #A = MB
        B = [x_coor, y_coor, z_coor]
        M_row1 = [mt.cos(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.sin(psi),
                mt.cos(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.sin(psi),
                mt.sin(psi) * mt.sin(theta)]
        
        M_row2 = [-mt.sin(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.cos(psi),
                -mt.sin(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.cos(psi),
                mt.cos(psi) * mt.sin(theta)]
        
        M_row3 = [mt.sin(theta) * mt.sin(phi), 
                -mt.sin(theta) * mt.cos(phi),
                mt.cos(theta)]
        
        A1 = M_row1[0] * B[0] + M_row1[1] * B[1] + M_row1[2] * B[2]
        A2 = M_row2[0] * B[0] + M_row2[1] * B[1] + M_row2[2] * B[2]
        A3 = M_row3[0] * B[0] + M_row3[1] * B[1] + M_row3[2] * B[2]
        
        beta = mt.asin(-A3 / mt.sqrt(A1 * A1 + A2 * A2 + A3 * A3))
        lamb = mt.atan2(A2, A1)
        
        beta = mt.degrees(beta)
        lamb = mt.degrees(lamb)
        
        return lamb, beta
    
    
    def binner_vlos(self, angle_cuttoffs):
        self.binned_vlos = []
        self.which_bin   = []
        
        bin_size = abs(angle_cuttoffs[0] - angle_cuttoffs[1]) / angle_cuttoffs[2]
        mid_bins = []
        which_lambda = []
        which_beta = []
        #setting up the mid bin coordinates
        for i in range(0, angle_cuttoffs[2]):
            mid_bin = angle_cuttoffs[0] + i * bin_size + bin_size / 2.0
            mid_bins.append(mid_bin)
            
        #transform to lambda beta coordinates from lbr
        self.convert_lambda_beta(False)
        
        for i in range(0, len(self.lambdas)):#go through the different lambda coordinates
            if(self.betas[i] >= angle_cuttoffs[3] and self.betas[i] <= angle_cuttoffs[4]):#if it is between the beta cuttoffs
                for j in range(0, len(mid_bins)):#go through the bin coordinates
                    left_edge  = mid_bins[j] - bin_size / 2.0 #edges of the bin
                    right_edge = mid_bins[j] + bin_size / 2.0 #edges of the bin
                    
                    if(self.lambdas[i] >= left_edge and self.lambdas[i] <= right_edge):#check if the lambda coor falls in the bin
                        self.which_bin.append(mid_bins[j])#which mid bin it should be 
                        self.binned_vlos.append(self.vls[i])#the line of sight vel
                        
                        which_lambda.append(self.lambdas[i])#the coordinate that was put there
                        which_beta.append(self.betas[i])
                        break 

class nbody_histograms:#a class that takes in data from nbody histogram files and makes them available
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_data()
        
    def get_data(self):
        self.lbins = []; self.counts = []; self.count_err = []; self.vd = []; self.vd_error = []
        read_data = False

        lines = open(self.file_name, 'r')
        for line in lines:
            if (line.startswith("betaBins")):
                read_data = True
                continue
            if(line.startswith("</histogram>")):
                break
            
            if(read_data):
                if(line.startswith("\n")):
                    continue
                else:
                    ss = line.split(' ')
                    self.lbins.append(    float(ss[1]))
                    self.counts.append(   float(ss[3]))
                    self.count_err.append(float(ss[4]))
                    self.vd.append(       float(ss[5]))
                    self.vd_error.append( float(ss[6]))
                    
        lines.close()
        
        
# # # # # # # # # # # # # # # # # # # # # #
#    standard nbody running functions     #
# # # # # # # # # # # # # # # # # # # # # #
def standard_run():
    if(remake):
        make_nbody()
        
    if(run_nbody):
        nbody(args_run, lua, histogram_for_nbody_run, histogram_for_nbody_run, version, False)
    
    if(run_and_compare):
        compare_after_run(args_run_comp, lua, correct_hist, histogram_for_nbody_run_and_compare, output_run_compare, version)
    
    if(match_histograms):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(plot_hists):
        plot(match_hist_correct , match_hist_compare, plot_name, '1', '2')
        
    if(plot_veldisp_switch):
        plot_veldisp(match_hist_correct , match_hist_compare, plot_name + "_velDisp", '1', '2')
    
    
    if(vlos_plot_switch):
        vlos_plot(match_hist_correct, match_hist_compare)
        
    return 0
# #        
def make_nbody():
        os.chdir("./")
        #-DCMAKE_C_COMPILER=/usr/bin/cc 
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")

# #    
def nbody(paras, lua_file, hist, out, ver, should_pipe):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    
    if(not run_from_checkpoint and should_pipe == False):
        print('running nbody1 ')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f "+ path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b -P  -i --no-clean-checkpoint " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
    if(run_from_checkpoint and should_pipe == False):
        print('running nbody from checkpoint')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b  -P --no-clean-checkpoint --checkpoint=nbody_checkpoint_correct_parameter_sweep " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
     
    
    if(should_pipe == True):
        print('running nbody')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 12 -b -P  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " \
         2>> " + out + "_piped.out")
     
     
     
    #os.chdir("../")
    os.chdir(path)
# #     
def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
          + " -S " + path + "quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0
# # 
def match_hists_pipe(hist1, hist2, ver, pipe_name):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "" + hist1 + '.hist'
          + " -S " + path + "" + hist2 + '.hist' + " 2>>" + pipe_name], shell=True)
    print hist1, "\n", hist2
    print "\n"
    return 0
# # 
def compare_after_run(paras, lua_file, correct, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    if(not run_from_checkpoint):
        print('running nbody 2')
        os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -h " + path + "quick_plots/hists/" + correct + ".hist \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b -P -i --no-clean-checkpoint " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
    
    if(run_from_checkpoint):#this is the version that will run from a checkpoint
        print 'running from checkpoint'
        os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
            -f " + path + "lua/" + lua_file + " \
            -h " + path + "quick_plots/hists/" + correct + ".hist \
            -z " + path + "quick_plots/hists/" + hist + ".hist \
            -o " + path + "quick_plots/outputs/" + out + ".out \
            -n 10 -b -P --no-clean-checkpoint --checkpoint=nbody_checkpoint_parameter_sweep_ft_4p03730890303 " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
# # 
# # # # # # # # # # # # # # # # # # # # # #
#        histogram plot                   #
# # # # # # # # # # # # # # # # # # # # # #
# # 
def plot(hist1, hist2, name, label1, label2):
    ylimit = 1.0
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    #folder = 'like_surface/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    #os.system("" + path + "scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    plot_hist1 = hist1 + ".hist"
    plot_hist2 = hist2 + ".hist"

    
    print("plotting histograms\n")
    hist1 = nbody_histograms(folder + plot_hist1)
    hist2 = nbody_histograms(folder + plot_hist2)
            
    if(plot_overlapping):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(hist1.lbins, hist1.counts, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(hist2.lbins, hist2.counts, width = w_overlap, color='r', alpha=0.75, label= label2)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.xlabel('Lambda')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        plt.clf()
        #plt.show()
        
    if(plot_adjacent):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(hist1.lbins, hist1.counts, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.xlabel('Lambda')

        plt.subplot(212)
        plt.bar(hist2.lbins, hist2.counts, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        plt.clf()
        #plt.show()
        return 1
# # 
def plot_veldisp(hist1, hist2, name, label1, label2):
    ylimit = 100
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    #folder = 'like_surface/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    #os.system("" + path + "scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    plot_hist1 = hist1 + ".hist"
    plot_hist2 = hist2 + ".hist"

    print("plotting histograms\n")
    hist1 = nbody_histograms(folder + plot_hist1)
    hist2 = nbody_histograms(folder + plot_hist2)
            
    if(plot_overlapping):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(hist1.lbins, hist1.vd, width = w_overlap, color='k', alpha=1,    label= label1)
        plt.bar(hist2.lbins, hist2.vd, width = w_overlap, color='r', alpha=0.75, label= label2)
        #plt.bar(hist1.lbins, hist1.count_err, width = w_overlap, color='black', alpha=0.75, label= label2)
        #plt.bar(hist2.lbins, hist2.count_err, width = w_overlap, color='b', alpha=0.75, label= label2)
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        plt.clf()
        #plt.show()
        
    if(plot_adjacent):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(hist1.lbins, hist1.vd, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.xlabel('Lambda')

        plt.subplot(212)
        plt.bar(hist2.lbins, hist2.vd, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('vel disp')
        plt.xlabel('Lambda')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        plt.clf()
        #plt.show()
        return 1
# # 
# # # # # # # # # # # # # # # # # # # # # #
#        NON-histogram plot               #
# # # # # # # # # # # # # # # # # # # # # #
# #

def vlos_plot(file1, file2):
    ylimit = 100
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    folder_hist = 'quick_plots/hists/'
    folder_outs = 'quick_plots/outputs/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    
    print "plot histogram 1: ", file1
    print "plot histogram 2: ", file2
    
    plot_hist1 = file1 + ".hist"
    plot_hist2 = file2 + ".hist"
    
    output1 = file1 + ".out"
    output2 = file2 + ".out"
    
    label1 = '1'
    label2 = '2'
    
    name = 'vlos_plots'
    print("plotting histograms\n")
    
    hist1 = nbody_histograms(folder_hist + plot_hist1)
    hist2 = nbody_histograms(folder_hist + plot_hist2)
     
    angle_cuttoffs = [-150.0, 150.0, 50, -15.0, 15.0, 1]
    
    out1 = nbody_outputs(folder_outs + output1)
    out2 = nbody_outputs(folder_outs + output2)
    
    out1.binner_vlos(angle_cuttoffs)#bin the line of sight vels
    out2.binner_vlos(angle_cuttoffs)
    
    
    if(plot_adjacent):
        count_y_limit = 0.4
        rawcount_y_limit = 2000
        vel_disp_ylimit = 100
        
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        #plt.subplots(4, sharex = True, sharey = True)
        ax1 = plt.subplot(421)
        plt.bar(hist1.lbins, hist1.counts, width = w_adjacent, color='b')
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.ylabel('counts')

        ax2 = plt.subplot(422)
        plt.bar(hist2.lbins, hist2.counts, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.yticks([])

        ax5 = plt.subplot(423)
        plt.bar(hist1.lbins, hist1.count_err, width = w_adjacent, color='b')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.ylabel('raw count')
        #plt.xlabel('Lambda')

        ax6 = plt.subplot(424)
        plt.bar(hist2.lbins, hist2.count_err, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.yticks([])
        #plt.xlabel('Lambda')
        
        ax3 = plt.subplot(425)
        #plt.subplots(2, sharex = True, sharey = False)
        plt.bar(hist1.lbins, hist1.vd, width = w_adjacent, color='b')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')

        ax4 = plt.subplot(426)
        plt.bar(hist2.lbins, hist2.vd, width = w_adjacent, color='k')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.yticks([])
        
        ax3 = plt.subplot(427)
        #plt.subplots(2, sharex = True, sharey = False)
        plt.scatter(out1.which_bin, out1.binned_vlos, color='b', s=.5, marker= 'o')
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')

        ax4 = plt.subplot(428)
        plt.scatter(out2.which_bin, out2.binned_vlos, color='k', s=.5, marker= 'o', )
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.yticks([])
        plt.savefig(save_folder_adj + name + '.png', format='png', dpi=1000)
        
        
    if(plot_overlapping):
        count_y_limit = 0.4
        rawcount_y_limit = 2000
        vel_disp_ylimit = 100
        
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)

        ax1 = plt.subplot(411)
        plt.bar(hist1.lbins, hist1.counts, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(hist2.lbins, hist2.counts, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.title('Line of Sight Vel Disp Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.ylabel('counts')
        plt.legend()
        
        ax3 = plt.subplot(412)
        plt.bar(hist1.lbins, hist1.count_err, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(hist2.lbins, hist2.count_err, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, rawcount_y_limit))
        plt.ylabel('raw count')
        plt.xlabel('Lambda')
        plt.legend()
        
        ax2 = plt.subplot(413)
        plt.bar(hist1.lbins, hist1.vd, width = w_adjacent, color='k', alpha=1,    label= label1)
        plt.bar(hist2.lbins, hist2.vd, width = w_adjacent, color='r', alpha=0.75, label= label2)
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        
        ax2 = plt.subplot(414)
        plt.scatter(out1.which_bin, out1.binned_vlos, s=1, marker= '.',  color='red', alpha=1,label= label1, edgecolors='none')
        plt.scatter(out2.which_bin, out2.binned_vlos, s=1, marker= '.', color='blue', alpha=1, label= label2, edgecolors='none')
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel('vel disp')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png', dpi=1000)
        #plt.clf()
        #plt.show()
        
        return 1
 
def lambda_beta_plot(file_name):
    path_charles = 'quick_plots/outputs/'
    path = 'quick_plots/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = n
    plot_dm_alone = n
    
    out = nbody_outputs(path_charles + file_name + '.out')
    out.dark_light_split()
    out.convert_lambda_beta(True)
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr):
        plt.figure(figsize=(20, 20))
        xlower = -360.0
        xupper = 360.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel('lambda')
        plt.ylabel('beta')
        plt.title('lambda vs beta')
        #default to just plot lm
        plt.plot(out.light_lambda, out.light_beta, '.', markersize = 1.75, color = 'b', alpha=1.0, marker = '.')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta', format='png')
        print "plotting:", len(out.light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('lambda')
            plt.ylabel('beta')
            plt.title('lambda vs beta')
            plt.plot(out.dark_lambda, out.dark_beta, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta', format='png')
            print "plotting:", len(light_l) + len(dark_l), " points"
        # # # # # # # # # #
        if(plot_dm_alone):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('lambda')
            plt.ylabel('beta')
            plt.title('lambda vs beta')
            plt.plot(out.dark_lambda, out.dark_beta, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lambdabeta_dark', format='png')
            
    return 0 
 
def lb_plot(file_name):
    path_charles = 'quick_plots/outputs/'
    path = 'quick_plots/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = y
    plot_dm = n
    plot_xyz = n
    plot_orbit = n
    
    out = nbody_outputs(path_charles + file_name + '.out')
    out.dark_light_split()
    out.rescale_l()
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr):
        plt.figure(figsize=(20, 20))
        xlower = -180.0
        xupper = 180.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel('l')
        plt.ylabel('b')
        plt.title('l vs b')
        #default to just plot lm
        plt.plot(out.light_l, out.light_b, '.', markersize = 1.75, color = 'b', alpha=1.0, marker = '.')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
        print "plotting:", len(out.light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(out.dark_l, out.dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
            print "plotting:", len(out.light_l) + len(out.dark_l), " points"
        # # # # # # # # # #
        if(plot_orbit):
            orb = nbody_outputs(path + 'reverse_orbit.out')
            orb.rescale_l()
            orb.dark_light_split()
            
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb.ls, orb.bs, '.', markersize = .15, color = 'g', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            
            orb = nbody_outputs(path + 'forward_orbit.out')
            orb.rescale_l()
            orb.dark_light_split()
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb.ls, orb.bs, '.', markersize = .15, color = 'r', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            plt.show()

        # # # # # # # # # #
        if(plot_dm):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(out.dark_l, out.dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_dark', format='png')
            
    if(plot_xyz):
        xlower = 50
        xupper = -50
        fig.tight_layout()
        plt.axes().set_aspect('equal')
        plt.subplot(131, aspect='equal')
        plt.plot(out.light_x, out.light_y, '.', markersize = 1, color = 'r', marker = 'o')
        
        if(plot_light_and_dark == True):
            plt.plot(out.dark_x, out.dark_y, '.', markersize = 1, color = 'b', marker = '+')
        
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('x vs y')
        
        plt.subplot(132,aspect='equal')
        
        plt.plot(out.light_x, out.light_z, '.', markersize = 1, color = 'r', marker = 'o')
        
        if(plot_light_and_dark == True):
            plt.plot(out.dark_x, out.dark_z, '.', markersize = 1, color = 'b', marker = '+')
        
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title('x vs z')
        
        plt.subplot(133, aspect='equal')
        
        plt.plot(out.light_z, out.light_y, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(out.dark_z, out.dark_y, '.', markersize = 1, color = 'b', marker = '+')
        
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('z')
        plt.ylabel('y')
        plt.title('z vs y')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_xyz', format='png')
    
    return 0
# #
# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
# #
def velocity_dispersion():
    args = [3.95, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = 'nbody1'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    nbody(args, l, file_name, file_name, version, False)
    #lb_plot(file_name)
    os.system("./scripts/velocity_dispersion.py " + file_name)
# # 
# # # # # # # # # # # # # # # # # # # # # #
#               MISC                      #
# # # # # # # # # # # # # # # # # # # # # #
# #
def proper_motion_check():
    args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
    folder = './quick_plots/outputs/'
    name1 = 'proper_motion1'
    name2 = 'proper_motion2'
    name3 = 'proper_motion_bestfit_1'
    name4 = 'proper_motion_bestfit_2'
    #nbody(args_run, lua, name1, name1, version, False)
    #nbody(args_run, lua, name2, name2, version, False)
    #name1 = folder + 'arg_3.95_0.98_0.2_0.2_12_0.2_correct.out'
    
    #args_run = [3.93673991552041, 1, 0.208862028335965, 0.247442889353978, 12.0777105127247, 0.350410837056286]
    #nbody(args_run, lua, name3, name3, version, False)
    #nbody(args_run, lua, name4, name4, version, False)
    #print os.path.isfile(folder + name1 + '.out')
    
    out1 = nbody_outputs(folder + name1 + '.out')
    out1.convert_lambda_beta(False)
    
    out2 = nbody_outputs(folder + name2 + '.out')
    out2.convert_lambda_beta(False)
    output3 = nbody_outputs(folder + name3 + '.out')
    output4 = nbody_outputs(folder + name4 + '.out')
    
    #print len(output1.xs)
    output3.convert_lambda_beta(False)
    output4.convert_lambda_beta(False)
    diff_sum1 = 0
    diff_sum2 = 0
    
    max_diff1 = 0.0
    max_diff2 = 0.0
    for i in range(0, len(out1.lambdas)):
        diff1 = out1.lambdas[i] - out2.lambdas[i]
        diff_sum1 += diff1
        
        diff2 = output3.lambdas[i] - output4.lambdas[i]
        diff_sum2 += diff2
        
        if(diff1 > max_diff1):
            max_diff1 = diff1
        if(diff2 > max_diff2):
            max_diff2 = diff2
        
    N = float(len(out1.lambdas))
    print N
    ave1 = diff_sum1 / N
    
    N = float(len(output3.lambdas))
    ave2 = diff_sum2 / N
    
    print ave1, ave2
    print max_diff1, max_diff2
    #name1 =  'arg_3.95_0.98_0.2_0.2_12_0.2_correct'


# #
def half_mass_radius():
    #found
    #-5.274575416,
    paras = [3.92936973371562, 1, 0.207910965711911, 0.295960733507015, 12.0120839736256, 0.632718403210685]
    
    #-1.628862634, 
    paras = [3.93673991552041, 1, 0.208862028335965, 0.247442889353978, 12.0777105127247, 0.350410837056286]
    
    #-2.017973168, 
    paras = [3.94791258079938, 1, 0.209888722689345, 0.237645947560661, 12.218431949382, 0.318558828332454]
    
    #-2.105469375, 
    paras = [3.94119850266711, 1, 0.20808218702441, 0.240524291805915, 12.0369010486177, 0.303651066818279]
    
    #-2.128633377, 
    paras = [3.93725511804223, 1, 0.209352829691495, 0.248126046080144, 12.1556158897001, 0.350097152269437]
    
    #-3.463901109
    #paras = [3.94256860087439, 1, 0.206455972523872, 0.252297658380121, 12.0365623332094, 0.372225859672762]
    #-3.622963436 
    #paras = [3.93355105434544, 1, 0.209191889511683, 0.23118108259514, 12.0577139347663, 0.307140060416423]
    #-3.237566942 
    #paras = [3.93711682423856, 1, 0.209691066770417, 0.253259351849556, 12.072108229451, 0.330662214732729]
    #-2.783683116
    #paras = [3.94241225402383, 1, 0.20874204818164, 0.234103694371879, 12.0684867434258, 0.305167746809311] 
    




    rl_f = paras[2]
    rr_f = paras[3]
    ml_f = paras[4]
    mr_f = paras[5]
    
    rd_f = (rl_f / rr_f) * (1.0 - rr_f)
    md_f = (ml_f / mr_f) * (1.0 - mr_f)
    
    print "found rd, md:\t", rd_f, md_f
    
    #correct
    ml_c = 12.0
    rl_c = 0.2
    rr_c = 0.2
    mr_c = 0.2
    rd_c = (rl_c / rr_c) * (1.0 - rr_c)
    md_c = (ml_c / mr_c) * (1.0 - mr_c)
    print "correct rd, md:\t", rd_c, md_c
    
    cut = .5 * ml_c
    
    r = 0.001
    while(1):
        m_enc_l = ml_c * r**3.0 / (r * r + rl_c * rl_c )**(3.0 / 2.0)
        
        m_enc_d_c = md_c * r**3.0 / (r * r + rd_c * rd_c )**(3.0 / 2.0)
        m_enc_d_f = md_f * r**3.0 / (r * r + rd_f * rd_f )**(3.0 / 2.0)
        
        
        plummer_den_d_c = (3.0 / (4.0 * mt.pi * rd_c**3.0)) * md_c / (1.0 + (r * r)/ (rd_c * rd_c))**(5.0 / 2.0)
        plummer_den_d_f = (3.0 / (4.0 * mt.pi * rd_f**3.0)) * md_f / (1.0 + (r * r)/ (rd_f * rd_f))**(5.0 / 2.0)
        if(m_enc_l >= cut):
            break
        else:
            r += 0.001

    print 'plum den correct, found:\t', plummer_den_d_c, plummer_den_d_f   #density of DM within correct baryon extent     
    print 'DM enc correct, DM enc found :\t', m_enc_d_c, m_enc_d_f
    
    print 'BM enc, r:\t', m_enc_l, r
    
# #
def test_vel_theta_binning():
    pathway = './data_testing/sim_outputs/'
    file_name = pathway + 'output_plummer_plummer_0gy.out'
    vxs = []
    vys = []
    vzs = []
    ms = []
    g = open(file_name, 'r')
    num = 1
    for line in g:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    g.close()
    
    line_n = 0
    lines = open(file_name, 'r')
    print num
    for line in lines:
        if(line_n < num):
            line_n += 1
            continue
        
        tt = line.split(', ')
        ty = float(tt[0])
        vx = float(tt[7])
        vy = float(tt[8])
        vz = float(tt[9])
        m  = float(tt[10])
        vxs.append(vx)
        vys.append(vy)
        vzs.append(vz)
        ms.append(m)
        
    lines.close()
    N = len(vxs)
    
    
    
    #cm correction
    cmx = 0.
    cmy = 0.
    cmz = 0.
    mtot = 0
    for i in range(0,N):
        cmx += ms[i] * vxs[i]
        cmy += ms[i] * vys[i]
        cmz += ms[i] * vzs[i]
        mtot += ms[i]
    cmx = cmx / mtot
    cmy = cmy / mtot
    cmz = cmz / mtot
    
    for i in range(0, N):
        vxs[i] -= cmx
        vys[i] -= cmy
        vzs[i] -= cmz
    
    thetas = []
    vs = []
    for i in range(0,len(vxs)):
        v = mt.sqrt( vxs[i] * vxs[i] + vys[i] * vys[i] + vzs[i] * vzs[i])
        theta = mt.acos( vzs[i] / v)
        thetas.append(theta)
        vs.append(v)
        
    print vs
    
    
    #binning
    binN = 1000
    binwidth = 0.1
    upper = binN * binwidth
    
    bins = []
    bin_ranges = []
    for k in range(0, binN):
        bins.append(0)
        bin_ranges.append(0)
        
        
    tmp = thetas
    #print tmp
    for i in range(0, N):
        bin_range = 0
        
        for j in range(0, binN):
            if( (bin_range + binwidth) < upper):
                if(tmp[i] >= bin_range and tmp[i] < (bin_range + binwidth)):
                    bins[j] += 1
                    break
                bin_range += binwidth
            elif( ( bin_range + binwidth) == upper):
                if( tmp[i] >= bin_range and tmp[i] <= (bin_range + binwidth)):
                    bins[j] += 1
                    break
                bin_range += binwidth

        
    bin_range = 0
    for k in range(0, binN):
        bin_ranges[k] = bin_range
        bin_range += binwidth
    #print bins

    plt.bar(bin_ranges, bins, width = .05 , color = 'r', edgecolor = 'k')
    plt.xlim(-3, 5)
    plt.show()
# #
def ridge_probe():
    rl = 0.2
    ml = 12
    rr_range = [0.1, 0.5]
    mr_range = [0.01, 0.95]
    
    rr = 0.2
    mr = 0.2
    
    rscale_t = rl / (rr)
    rd = rscale_t * (1.0 - rr)
    
    dwarfmass = ml / mr
    md = dwarfmass * (1.0 - mr)
    
    f = open("ridge_data.txt", 'w')
    print rd, md
    
    rr = rr_range[0]
    mr = mr_range[0]
    ratios = []
    density1s = []
    density2s = []
    
    rrs = []
    mrs = []
    while(1):
        mr = mr_range[0]
        while(1):
            rscale_t = rl / (rr)
            rd = rscale_t * (1.0 - rr)
        
            dwarfmass = ml / mr
            md = dwarfmass * (1.0 - mr)
            
            ratio = md / rd
            density1 = md / (4.0 * mt.pi * rd**3)
            density2 = rd**2 * density1
            
            rrs.append(rr)
            mrs.append(mr)
            ratios.append(ratio)
            density1s.append(density1)
            density2s.append(density2)
            
            f.write("%0.15f\t %0.15f\t%0.15f\t%0.15f\t%0.15f\n" % (rr, mr, ratio, density1, density2))
            
            
            if(mr > mr_range[1]):
                break
            else:
                mr += 0.01
                
        if(rr > rr_range[1]):
            break
        else:
            rr += 0.001
    f.close()
    
    gnu_args = ['reset',
                'set terminal wxt persist',
                'set key off',
                "set xlabel 'rrs' ",
                "set ylabel 'mrs' ",
                "set zlabel 'ratio' ",
                "set xrange[0.1: 0.5]",
                "set yrange[0.01:0.95]",
                "set zrange[0:100]"]
                
                
    g = open("ridge_probe.gnu", 'w')
    for i in range(0, len(gnu_args)):
        g.writelines(gnu_args[i] + "\n")
    g.write("splot 'ridge_data.txt' using 1:2:4 with points palette pointtype 5 ps 0.5\n")
    g.close()
    os.system("gnuplot ridge_probe.gnu 2>>piped_output.txt")
    
    return 0
# #
def plot_all_hists():
    ver = ''
    paras = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
    lua_file = 'EMD_v162.lua'
    sweep = 'parameter_sweeps_10_21_2016_post_best_like_fix_narrow_random_0.9sim'
    bins = '100'
    typ = 'ft'
    correct = sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/arg_3.95_0.98_0.2_0.2_12_0.2_correct'
    f = open('like_surface/' + sweep + '/' + bins + 'bins/likelihood_data_rand_iter_' + bins + 'bins/' + typ + '_data_vals.txt', 'r')
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    for i in range(0, len(values)):
        hist_name = sweep + '/' + bins + 'bins/hists_' + bins + 'bins_tight/' + typ + '_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_0.2'
        label1 = '3.95gy'
        label2 = "ft = " + str(values[i]) + " likel =    " + str(likes[i]) + "% sim" + str(values[i]/3.95)
        plot(correct, hist_name, str(i), label1, label2)
    return 0
# #
def check_timestep():
    rl = [0.05, 0.5]
    rr = [0.1, 0.5]
    ml = [1, 50]
    mr = [0.01, 0.95]
    f = open("times.txt", 'w')
    rl_inc = 0.1
    rr_inc = 0.05
    ml_inc = 1
    mr_inc = 0.05
    
    irl = rl[0]
    while(1):
        irr = rr[0]
        while(1):
            iml = ml[0]
            while(1):
                imr = mr[0]
                while(1):
                    dwarfMass = iml / imr
                    rscale_t  = irl / irr
                    rd  = rscale_t *  (1.0 - irr)
                    md    = dwarfMass * (1.0 - imr)
                    
                    
                    mass_enc_d = md * (irl)**3 * ( (irl)**2 + (rd)**2  )**(-3.0/2.0)

                    mass_enc_l = iml * (rd)**3 * ( (irl)**2 + (rd)**2  )**(-3.0/2.0)

                    s1 = (irl)**3 / (mass_enc_d + iml)
                    s2 = (rd)**3 / (mass_enc_l + md)
                    
                    if(s1 < s2):
                        s = s1
                    else:
                        s = s2
                    
                    t = (1 / 100.0) * ( mt.pi * (4.0 / 3.0) * s)**(1.0/2.0)
                    f.write("%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\t%0.15f\n" % (t, irl, irr, iml, imr, rd, md))
                    
                    if(imr > mr[1]):
                        break
                    else:
                        imr += mr_inc
                
                if(iml > ml[1]):
                    break
                else:
                    iml += ml_inc
            
            if(irr > rr[1]):
                break
            else:
                irr += rr_inc
                
        if(irl > rl[1]):
            break
        else:
            irl += rl_inc
                    
                   
    f.close()
# # 
def stabity_test():
    args = [0.0001, 0.9862, 0.2, 0.5, 24, .5]
    #args = [0.0001, 0.9862, 0.2, 0.2, 24, .2]
    sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
    ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
    N               = 1
    M               = 0
    
    make_nbody()
    
    b_t = str(args[1])
    r_l = str(args[2])
    r_r = str(args[3])
    m_l = str(args[4])
    m_r = str(args[5])
    
    
    ver = ''
    lua_file = "mixeddwarf.lua"
    
    nfw  = 'output_nfw_nfw_0gy'
    plum = 'output_plummer_plummer_0gy'
    hern = 'output_hern_hern_0gy'
    plum_nfw = 'output_plummer_nfw_0gy'

    fn = nfw
    #args = [sim_time[0], 0.9862, 0.8, 0.5, 24, .5]
    #nbody(args, lua_file, fn, fn, ver, False)
    
    for i in range(M, N):
        args[0] = sim_time[i]
        nfw  = 'output_nfw_nfw_' + ext[i] + 'gy'
        plum = 'output_plummer_plummer_' + ext[i] + 'gy'
        hern = 'output_hern_hern_' + ext[i] + 'gy'
        plum_nfw = 'output_plummer_nfw_' + ext[i] + 'gy'
        fn = nfw
        nbody(args, lua_file, fn, fn, ver, False)
    
    
    os.chdir("data_testing")    
    os.system("./stability_test.py " + b_t + " " + r_l + " " + r_r + " " + m_l + " " + m_r)
# # 
def clean():
    os.system("rm boinc_*")
# #      
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Generator           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
def main():
    standard_run()
    
    if(test_vel_theta_binning_switch):
        test_vel_theta_binning()
        
    if(make_some_hists_switch):
        make_some_hists()
    
    if(stabity_test_switch):
        stabity_test()
    
    if(velocity_disp_switch):
        velocity_dispersion()
    
    if(lb_plot_switch):
        lb_plot(output)
    
    if(lambda_beta_plot_switch):
        lambda_beta_plot(output)
        
        
    if(plot_all_hists_switch):
        plot_all_hists()
    
    if(ridge_probe_switch):
        ridge_probe()
    
    
    if(check_timestep_switch):
        check_timestep()
        
    if(quick_calculator_switch):
        quick_calculator()
        
    if(half_mass_radius_switch):
        half_mass_radius()
        
    if(proper_motion_check_switch):
        proper_motion_check()
# spark plug #
main()

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
#args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run = [3.95, 0.98, 0.2, 0.2, 12, 1.43] 
args_run = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
args_run_comp = [3.95, 0.98, 0.2, 0.170053817392000, 12, 0.203131549162000] 
#args_run_comp = [3.28828657813, 0.98, 0.2, 0.2, 12, 0.2]

#args_run_comp = [2.08, 0.98, 0.2, 0.3, 12, 0.45] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#              Standard Run switches          #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = y                 #
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
plot_all_hists_switch     = n                 #
half_mass_radius_switch   = n                 #
chi_sq_dist_plot_switch   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Circuitry           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#    Histogram names      #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'

#    histograms for runs  #
#correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_mw'
correct1 = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_diff_seed'
sweep_test1 = 'sweep_test1'
sweep_test2 = 'sweep_test2'
sweep_test3 = 'sweep_test3'#same as 1
sweep_test4 = 'sweep_test4'#same as 2

#    hist to match against for compare after run  #
correct_hist = correct1
compare_hist = '2D_hist_checking_mw'



#    hist name for the nbody run   #
histogram_for_nbody_run = correct_hist
histogram_for_nbody_run_and_compare = compare_hist

#    if you are just matching, these are the two hists #
match_hist_correct = histogram_for_nbody_run
match_hist_compare = histogram_for_nbody_run_and_compare
plot_name = compare_hist


output = histogram_for_nbody_run
output_run_compare = histogram_for_nbody_run_and_compare
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#    run specfics   #
#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
#lua = "full_control.lua"
lua = "EMD_v164.lua"

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
        compare_after_run(args_run_comp, lua, histogram_for_nbody_run, histogram_for_nbody_run_and_compare, output_run_compare, version)
    
    if(match_histograms):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(plot_hists):
        plot(match_hist_correct , match_hist_compare, plot_name, '1', '2')
        
    if(plot_veldisp_switch):
        plot_veldisp(match_hist_correct , match_hist_compare, plot_name + "_velDisp", '1', '2')
    
    
    if(vlos_plot_switch):
        vlos_plot(match_hist_correct, match_hist_compare)
        vlos_plot_single(match_hist_correct)
        
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
    #folder = ''
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
def vlos_plot_single(file1):
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
    
    plot_hist1 = file1 + ".hist"
    
    output1 = file1 + ".out"
    
    label1 = '1'
    
    name = 'vlos_plots'
    print("plotting histograms\n")
    
    hist1 = nbody_histograms(folder_hist + plot_hist1)
     
    angle_cuttoffs = [-150.0, 150.0, 50, -15.0, 15.0, 1]
    
    out1 = nbody_outputs(folder_outs + output1)
    
    out1.binner_vlos(angle_cuttoffs)#bin the line of sight vels
    
    if(plot_overlapping):
        count_y_limit = 0.4
        rawcount_y_limit = 2000
        vel_disp_ylimit = 50
        
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)

        ax1 = plt.subplot(311)
        plt.bar(hist1.lbins, hist1.counts, width = w_adjacent, color='k', alpha=1)
        #plt.title(r'Line of Sight $\sigma_{line of sight}$ Distribution')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, count_y_limit))
        plt.ylabel('counts')
        plt.legend()
        
        #ax3 = plt.subplot(412)
        #plt.bar(hist1.lbins, hist1.count_err, width = w_adjacent, color='k', alpha=1)
        #plt.xlim((xlower, xupper))
        #plt.ylim((0.0, count_y_limit**0.5))
        #plt.ylabel('Count error')
        #plt.xlabel('Lambda')
        #plt.legend()
        
        ax2 = plt.subplot(312)
        plt.bar(hist1.lbins, hist1.vd, width = w_adjacent, color='k', alpha=1)
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel(r'$\sigma$ (km/s)')
        #plt.legend()
        
        ax2 = plt.subplot(313)
        plt.scatter(out1.which_bin, out1.binned_vlos, s=2, marker= '.',  color='k', alpha=1, edgecolors='none')
        plt.xlim((xlower, xupper))
        #plt.ylim((0.0, vel_disp_ylimit))
        plt.ylabel(r'${v_{los}}$ (km/s)')
        #plt.legend()
        plt.xlabel(r'$\Lambda$')
        plt.savefig(save_folder_ove + name + '_overlapping_single.png', format='png', dpi=500)
        #plt.clf()
        #plt.show()
        
        return 1

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
    plot_light_and_dark = y
    plot_dm_alone = n
    
    out = nbody_outputs(path_charles + file_name + '.out')
    out.dark_light_split()
    out.convert_lambda_beta(True)
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr):
        plt.figure(figsize=(10, 10))
        xlower = -180.0
        xupper = 180.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel(r'$\Lambda$')
        plt.ylabel(r'$\beta$')
        plt.title(r'$\Lambda$ vs $\beta$')
        #default to just plot lm
        plt.plot(out.light_lambda, out.light_beta, '.', markersize = .75, color = 'b', alpha=1.0, marker = '.',label = 'baryons')
        plt.legend()
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta_nodark', format='png')
        print "plotting:", len(out.light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel(r'$\Lambda$')
            plt.ylabel(r'$\beta$')
            plt.title(r'$\Lambda$ vs $\beta$')
            plt.plot(out.dark_lambda, out.dark_beta, '.', markersize = .5, color = 'black', alpha=.75, marker = '.', label = 'dark matter')
            plt.legend()
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + '_lambdabeta', format='png')
            print "plotting:", len(out.light_l) + len(out.dark_l), " points"
        # # # # # # # # # #
        if(plot_dm_alone):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel(r'$\Lambda$')
            plt.ylabel(r'$\beta$')
            plt.title(r'$\Lambda$ vs $\beta$')
            plt.plot(out.dark_lambda, out.dark_beta, '.', markersize = 1, color = 'b', marker = '+')
            plt.legend()
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
    out.rescale_l()
    out.dark_light_split()
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr):
        plt.figure(figsize=(10, 10))
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
        plt.plot(out.light_l, out.light_b, '.', markersize = 1., color = 'b', alpha=1.0, marker = '.', label = 'baryons')
        plt.legend()
        plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
        print "plotting:", len(out.light_l), " points"
        # # # # # # # # # #
        if(plot_light_and_dark):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(out.dark_l, out.dark_b, '.', markersize = 1, color = 'red', alpha=.25, marker = '.', label = 'dark matter')
            plt.legend()
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

# # # # # # # # # # # # # # # # # # # # # #
#               MISC                      #
# # # # # # # # # # # # # # # # # # # # # #
# #

def chi_sq_dist_plot():
    k = 50.0
    cf = (k / 2.0) - 1.0
    x = 0.1
    xs = []
    func1s = []
    func2s = []
    func3s = []
    while(1):
        func1 = cf * mt.log(x) - x / 2.0
        func2 = func1 - cf * (mt.log(2.0 * cf) - 1.0) 
        if(x < 2.0 * cf):
            func3 = 0.0
        else:
            func3 = func2
            
        xs.append(x)
        func1s.append(func1)
        func2s.append(func2)
        func3s.append(func3)
        if(x > 1000):
            break
        else:
            x += 0.1
    plt.ylim((-200, 100))
    plt.xlim((0, 400))
    plt.xlabel(r'N$_{\sigma}$$^{2}$')
    plt.ylabel('Probability')
    #plt.plot(xs, func1s)
    #plt.plot(xs, func2s)
    plt.plot(xs, func3s)
    plt.savefig('/home/sidd/Desktop/research/quick_plots/chi_sq_func3', format='png')
    #plt.show()
# #
def half_mass_radius():
    #found
    
    #-4.223705409, inertia 0.95  3  july 15
    paras = [3.94212310440862, 1, 0.209754488329843, 0.149297963920578, 12.0025209937495, 0.118499907769452]
    #-3.340390704, , inertia 0.95  3  july 17
    paras = [3.93319756659488, 1, 0.20650733573981, 0.231213550145698, 12.0500276364552, 0.253555598702015]
    #-3.259024291 3 july 19
    paras = [3.9336334482373, 1, 0.207990122635552, 0.106294048112, 12.2616054285078, 0.0476065538218]
    #-2.485412179, 3, july 25
    paras = [3.92986741357062, 1, 0.198291118789933, 0.106294048112, 12.0940980827287,  0.0476065538218]
    #-2.485412179, july 28
    paras = [3.92986741357062, 1, 0.198291118789933, 0.106294048112, 12.0940980827287, 0.0476065538218]
    #-2.485412179, july 31
    paras = [3.92986741357062, 1, 0.198291118789933, 0.106294048112, 12.0940980827287, 0.0476065538218]
    #-2.48437641, aug 24
    paras = [3.93358712305859, 1, 0.193580571037933, 0.106294048112117, 12.1442123356541, 0.0476065538221611]
    
    #-2.962097993, inertia 0.85  2 july 15
    #paras = [3.95378378434514, 1, 0.206041086218832, 0.147924308923534, 12.0409239373066, 0.114081112087091]
    #-2.962097993,  inertia 0.85  2 july 17
    #paras = [3.95378378434514, 1, 0.206041086218832, 0.147924308923534, 12.0409239373066, 0.114081112087091]
    #-2.893468048 2  july 19
    #paras =  [3.95309677360586, 1, 0.203955994957639, 0.150740069568347, 12.0295576783773, 0.113673581853117]
    #-2.835807667, 2, july 25
    #paras = [3.96084001571367, 1, 0.19883172037272,   0.140806663089422,  12.0399970584733,  0.0988578701643179]
    #-2.835807667, july 28
    #paras = [3.96084001571367, 1, 0.19883172037272, 0.140806663089422, 12.0399970584733, 0.0988578701643179]
    #-2.661055117, july 31
    #paras = [3.95717575453962, 1, 0.210073040269674, 0.199759136098848, 11.9732300009029, 0.244745393286548]
    #-2.293246408, aug 24
    #paras = [3.95994520654452, 1, 0.19801199565748, 0.141151236595692, 12.0768629690798, 0.0974371019908495]

    
    #-2.576449645 inertia 0.75  1 july 15
    #paras = [3.95022573221887, 1, 0.211005207741159, 0.234158545905685, 12.1524913389464, 0.322044096100095]
    #-2.451020931, inertia 0.75  1 july 17
    #paras = [3.94304172966898, 1, 0.207005794187862, 0.239074661015308, 12.1004122721036, 0.305314401157284]
    #-1.982544008, 1   july 19
    #paras = [3.94374191868974, 1, 0.209527551031424, 0.238111030876674, 12.0851791020405, 0.313628795395889]
    #-1.798167375, 1 july 25
    #paras = [3.94294089367003, 1, 0.208056824928637, 0.23901808287037,    12.0978099829844,  0.300798394769984]
    #-1.749000907, july 28
    #paras = [3.9424274169478, 1, 0.207665139519991, 0.239300095615801, 12.1021511215072, 0.298475763045956]
    #-1.749000907, july 31
    #paras = [3.9424274169478, 1, 0.207665139519991, 0.239300095615801, 12.1021511215072, 0.298475763045956]
    #-1.400173185, aug 24
    #paras = [3.94401142150537, 1, 0.207723248253692, 0.234680526248199, 12.086396585287, 0.294652083874054]
    paras = [3.94295443594432, 1, 0.208874690835381, 0.234263961296537, 12.0917409199754, 0.300065912129365]
    paras = [3.94119850266711, 1, 0.207553234347138, 0.241321487352245, 12.1486052311932, 0.306685105049991]
    paras = [3.93649841565613, 1, 0.208372119674464, 0.235151860862976, 12.0055674149201, 0.306476628533526]

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
    #calculates the density of the dm within the half mass radius of the correct baryon component
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
    
    
    r = 0.001
    #calculates the density of the dm within the half mass radius of the correct baryon component
    cut = 0.5 * ml_f
    while(1):
        m_enc_l = ml_f * r**3.0 / (r * r + rl_f * rl_f )**(3.0 / 2.0)
        
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
    
    
    
    #rr_c = 0.2
    #rd_c = (rl_c / rr_c) * (1.0 - rr_c)
    #m_enc_d_c = md_c * r**3.0 / (r * r + rd_c * rd_c )**(3.0 / 2.0)
    if(False):
        f = open('cons_den.txt', 'w')
        
        threshold = 0.2
        mr = 0.05
        while(1):
            rr = 0.05
            while(1):
                rd_f = (rl_c / rr) * (1.0 - rr)
                md_f = (ml_c / mr) * (1.0 - mr)
                #mdenc = (3.0 / (4.0 * mt.pi * rd_f**3.0)) * md_f / (1.0 + (r * r)/ (rd_f * rd_f))**(5.0 / 2.0)
                mdenc = md_f * r**3.0 / (r * r + rd_f * rd_f )**(3.0 / 2.0)
                #print mdenc, m_enc_d_c
                if(mdenc > (m_enc_d_c - threshold) and mdenc < (m_enc_d_c + threshold) ):
                    f.write("%0.15f\t%0.15f\t%0.15f\n" % (rr, mr, mdenc))
                
                if(rr > 0.5):
                    break
                else:
                    rr += 0.001
            if(mr > 0.95):
                break
            else:
                mr += 0.001
        f.close()
    #print m_enc_d_c

# #
def plot_all_hists():
    paras = [3.95, 0.98, 0.2, 0.2, 12, 0.2]
    sweep = 'parameter_sweeps_7_20_2017_new_fitting_functions'
    typ = 'ft'
    correct = 'parameter_sweeps/' + sweep + '/tel/hists/arg_3.95_0.98_0.2_0.2_12_1.43_correct'
    f = open('like_surface/' + sweep + '/likelihood_data_7_20_2017_new_fitting_functions_tel/' + typ + '_data_vals.txt', 'r')
    values = []
    likes  = []
    for line in f:
        ss = line.split("\t")
        value = float(ss[0])
        like  = float(ss[1])
        values.append(value)
        likes.append(like)
    
    for i in range(0, len(values)):
        hist_name = 'parameter_sweeps/' + sweep + '/tel/hists/' + typ + '_hists/arg_' + str(values[i]) + '_0.98_0.2_0.2_12_1.43'
        label1 = '3.95gy'
        label2 = "ft = " + str(values[i]) + " likel =    " + str(likes[i]) + "  % sim" + str(values[i]/3.95)
        plot(correct, hist_name, str(i), label1, label2)
    return 0
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
    
    
    if(lb_plot_switch):
        lb_plot(output)
    
    if(lambda_beta_plot_switch):
        lambda_beta_plot(output)
        
        
    if(plot_all_hists_switch):
        plot_all_hists()
    
        
    if(half_mass_radius_switch):
        half_mass_radius()
        
        
    if(chi_sq_dist_plot_switch):
        chi_sq_dist_plot()
# spark plug #
main()

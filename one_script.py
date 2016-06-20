#! /usr/bin/python
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
from matplotlib import cm
import math
import matplotlib.patches as mpatches
import numpy as np
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
args = [3.945, 0.98, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [0.000001, 1.0, 0.2, 0.2, 12, 0.2] #for hist with dark matter
#args = [3.87427734322731, 0.948765315488652, 0.356895748596523, .145236987452136, 10.1548765394315, 0.185215358746843]
#args = [2.0, 0.98, 0.2, 0.2, 13, 0.2] #for hist with dark matter

# # # # # # # # # # # # # # # # # # # # # # # #
#    SWITCHES for standard_run()  #           #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = n                 #
remake                    = y                 #
match_histograms          = n                 #
run_and_compare           = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
charles                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
calc_cm                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_hists                = n                 #
plot_overlapping          = n                 #
plot_adjacent             = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_lb                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
get_fornax_binary_now     = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # #
# possible tests #                            #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_dispersion_calc  = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_a_few_hists          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
run_stability_test        = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

#    Histogram names     #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_9_16'

#    histograms for runs #
multi = 'test_mt'
singl = 'test_st'

correct_hist = multi
histogram_for_nbody_run = multi


match_hist_correct = multi
match_hist_compare = histogram_for_nbody_run
plot_name = histogram_for_nbody_run

output = plot_name
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
#lua = "Null.lua"

outs = 2 #for the cm calculation function

#I am tired of constantly adapting it for the servers
lmc_dir = '~/research/'
sid_dir = '~/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = sid_dir
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # #
#    standard nbody running functions     #
# # # # # # # # # # # # # # # # # # # # # #
def standard_run():
    if(remake == True):
        make_nbody()
    
    if(run_nbody == True):
        nbody(args, lua, histogram_for_nbody_run, output, version)
    
    if(run_and_compare == True):
        compare_after_run(args, lua, correct_hist, histogram_for_nbody_run, output, version)
    
    if(match_histograms == True):
        match_hists(match_hist_correct, match_hist_compare, version)
        
        
    if(calc_cm == True):
        calculate_cm(args, output1, output2, outs)
    
    if(plot_hists == True):
        plot(match_hist_correct + ".hist" , match_hist_compare + ".hist", plot_name)
    
    #if(plot_lb == True):
        #os.system("./scripts/lb_plot.py quick_plots/outputs/" + output)
    return 0
# # # # # # # # # #         
def make_nbody():
        os.chdir("./")
        #-DCMAKE_C_COMPILER=/usr/bin/cc 
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=ON -DNBODY_STATIC=OFF -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
# # # # # # # # # #           
def nbody(paras, lua_file, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    
    print('running nbody')
    os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
        -f " + path + "lua/" + lua_file + " \
        -z " + path + "quick_plots/hists/" + hist + ".hist \
        -o " + path + "quick_plots/outputs/" + out + ".out \
         -n 12 -b   -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # #     
def match_hists(hist1, hist2, ver):
    print "matching histograms: "
    #using call here instead so the format of using it is on record
    call([" " + path + "nbody_test/bin/milkyway_nbody" + ver  
          + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
          + " -s " + path + "quick_plots/hists/" + hist2 + '.hist'], shell=True)
    print hist1, "\n", hist2
    print "\n"
# # # # # # # # # # 
def compare_after_run(paras, lua_file, correct, hist, out, ver):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
        #-h " + path + "quick_plots/hists/" + match_hist_correct + ".hist \
    print('running nbody')
    os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver + " \
        -f " + path + "lua/" + lua_file + " \
        -h " + path + "quick_plots/hists/" + correct + ".hist \
        -z " + path + "quick_plots/hists/" + hist + ".hist \
        -o " + path + "quick_plots/outputs/" + out + ".out \
        -n 10 -b -P -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
# # # # # # # # # #       
def plot(hist1, hist2, name):
    ylimit = 0.4
    xlower = 50
    xupper = -75
    w_overlap = 2.5
    w_adjacent = 1.5
    folder = 'quick_plots/hists/'
    save_folder_ove = 'quick_plots/comp_hist_plots/overlap/'
    save_folder_adj = 'quick_plots/comp_hist_plots/adj/'
    #os.system("" + path + "scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    print "plot histogram 1: ", hist1
    print "plot histogram 2: ", hist2
    plot_hist1 = hist1
    plot_hist2 = hist2
    
    print("plotting histograms\n")
    lines = []
    #print(os.getcwd())
    lines = open(folder + plot_hist1).readlines();
    
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("betaBins")):
            break 
    lines = lines[starting_line:len(lines)]
    
    sim_l = []
    sim_n = []
    for line in lines:
        if (line.startswith("</histogram>")):
            continue
        tokens = line.split();
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            cts = float(tokens[3])
            sim_l.append(lda)
            sim_n.append(cts)

    lines = []
    lines = open(folder + plot_hist2).readlines();
    
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("betaBins")):
            break 
    lines = lines[starting_line:len(lines)]
    
    data_l = []
    data_n = []
    for line in lines:
        if (line.startswith("</histogram>")):
            continue
        tokens = line.split()
        if tokens:
            dat_l = float(tokens[1])
            dat_n = float(tokens[3])
            data_l.append(dat_l)
            data_n.append(dat_n)
            
    if(plot_overlapping == True):
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        #plt.subplot(211)
        plt.bar(sim_l, sim_n, width = w_overlap, color='k', alpha=1, label= plot_hist1)
        plt.bar(data_l, data_n, width = w_overlap, color='r', alpha=0.5, label= plot_hist2)
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')
        plt.legend()
        plt.savefig(save_folder_ove + name + '_overlapping.png', format='png')
        #plt.show()
        
    if(plot_adjacent == True):
        plt.subplot(211)
        #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
        plt.bar(sim_l, sim_n, width = w_adjacent, color='b')
        plt.legend(handles=[mpatches.Patch(color='b', label= plot_hist1)])
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.ylabel('counts')

        plt.subplot(212)
        plt.bar(data_l, data_n, width = w_adjacent, color='k')
        plt.legend(handles=[mpatches.Patch(color='k', label= plot_hist2)])
        plt.xlim((xlower, xupper))
        plt.ylim((0.0, ylimit))
        plt.xlabel('l')
        plt.ylabel('counts')
        #f.subplots_adjust(hspace=0)
        plt.savefig(save_folder_adj + name + '.png', format='png')
        #plt.show()
        return 1
# # # # # # # # # #       
def calculate_cm(paras, output1, output2, outs):
    sim_time      = str(paras[0])
    back_time     = str(paras[1])
    r0            = str(paras[2])
    light_r_ratio = str(paras[3])
    mass_l        = str(paras[4])
    mass_ratio    = str(paras[5])
    
    if(outs == 2):
        os.system("./scripts/output_cm_calc.py " + mass_l + " " + mass_ratio + " " + output1 + " " + output2)
    if(outs == 1):
        os.system("./scripts/output_cm_calc.py " + mass_l + " " + mass_ratio + " " + output)
# # # # # # # # # #
def lb_plot(file_name):
    path_charles = 'quick_plots/outputs/charles/'
    path = 'quick_plots/outputs/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = y
    plot_dm = y
    plot_xyz = n
    plot_orbit = y
    plot_orbit_points = y
    plot_poly_points = y
    plot_old_orbit   = n
    
    f = open(path_charles + file_name + '.out')
    lines = []
    lines = f.readlines()
    
    num = 1
    for line in lines:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    
    lines = lines[num:len(lines)]
    print num
    light_x , light_y , light_z = ([] for i in range(3))
    light_l , light_b , light_r = ([] for i in range(3))
    light_vx , light_vy , light_vz = ([] for i in range(3))
    
    dark_x , dark_y , dark_z = ([] for i in range(3))
    dark_l , dark_b , dark_r = ([] for i in range(3))
    dark_vx , dark_vy , dark_vz = ([] for i in range(3))

    for line in lines:
        if(line.startswith("</bodies>")):
            break
        tokens = line.split(', ')
        isDark = int(tokens[0])
        X = float(tokens[1])
        Y = float(tokens[2])
        Z = float(tokens[3])
        l = float(tokens[4])
        if(l > 180.0):
            l = l - 360.0
        b = float(tokens[5])
        r = float(tokens[6])
        vx = float(tokens[7])
        vy = float(tokens[8])
        vz = float(tokens[9])
        if(isDark == 0):
            light_x.append(X)
            light_y.append(Y)
            light_z.append(Z)
            light_l.append(l)
            light_b.append(b)
            light_r.append(r)
            light_vx.append(vx)
            light_vy.append(vy)
            light_vz.append(vz)
        if(isDark == 1):
            dark_x.append(X)
            dark_y.append(Y)
            dark_z.append(Z)
            dark_l.append(l)
            dark_b.append(b)
            dark_r.append(r)
            dark_vx.append(vx)
            dark_vy.append(vy)
            dark_vz.append(vz)    
    print(len(light_l))
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    # # # # # # # # # #
    if(plot_lbr == True):
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
        plt.plot(light_l, light_b, '.', markersize = 1.5, color = 'c', alpha=1.0, marker = '.')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_light', format='png')
        
        # # # # # # # # # #
        if(plot_light_and_dark == True):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter', format='png')
        
        # # # # # # # # # #
        if(plot_orbit == True):
            f = open(path_charles + 'reverse_orbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'lime', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            f = open(path_charles + 'forward_orbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'g', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')

        if(plot_old_orbit == True):
            f = open(path_charles + 'reverse_orbit_oldorbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'darkred', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            f = open(path_charles + 'forward_orbit_oldorbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'indianred', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')


            f = open(path_charles + 'reverse_orbit_oldoldorbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'darkred', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            f = open(path_charles + 'forward_orbit_oldoldorbit.out')
            lines = []
            lines = f.readlines()
            orb_l , orb_b , orb_r = ([] for i in range(3))
            orb_vx , orb_vy , orb_vz = ([] for i in range(3))
            for line in lines:
                tokens = line.split('\t')
                orbX = float(tokens[0])
                if(orbX > 180.0):
                    orbX = orbX - 360.0
                orbY = float(tokens[1])
                orbZ = float(tokens[2])
                orbVx = float(tokens[3])
                orbVy = float(tokens[4])
                orbVz = float(tokens[5])
                orb_l.append(orbX)
                orb_b.append(orbY)
                orb_r.append(orbZ)
                orb_vx.append(orbVx)
                orb_vy.append(orbVy)
                orb_vz.append(orbVz)
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb_l, orb_b, '.', markersize = .15, color = 'indianred', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
        
        # # # # # # # # # #    
        if(plot_orbit_points == True):
            f = open(path_charles + 'Hermus_pm2_13stars.csv')
            lines = []
            lines = f.readlines()
            lines = lines[1:len(lines)]
            orbp_l , orbp_b , orbp_r = ([] for i in range(3))
            for line in lines:
                tokens = line.split(',')
                orbpl = float(tokens[2])
                orbpb = float(tokens[3])
                #print(orbpl, orbpb)
                orbp_l.append(orbpl)
                orbp_b.append(orbpb) 
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orbp_l, orbp_b, '.', markersize = 3, color = 'm', alpha= 1.0, marker = 'o')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
            
        # # # # # # # # # #    
        if(plot_poly_points == True):
            f = open(path_charles + 'polynomial_fit.csv')
            lines = []
            lines = f.readlines()
            lines = lines[1:len(lines)]
            orbpoly_l , orbpoly_b = ([] for i in range(2))
            for line in lines:
                tokens = line.split(',')
                tokens[3] = tokens[3].strip()
                #print tokens
                orbpl = float(tokens[2])
                orbpb = float(tokens[3])
                #print(orbpl, orbpb)
                orbpoly_l.append(orbpl)
                orbpoly_b.append(orbpb) 
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orbpoly_l, orbpoly_b, '.', markersize = 3, color = 'g', alpha= 1.0, marker = 'o')
            #os.system("mpg123  rasengan.mp3 ")
            plt.show()
            plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + 'with_poly', format='png')
            
        # # # # # # # # # #
        if(plot_dm == True):#to plot just dm
            plt.clf()
            plt.figure(figsize=(20, 20))
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_dark', format='png')
            
    if(plot_xyz == True):
        xlower = 50
        xupper = -50
        fig.tight_layout()
        plt.axes().set_aspect('equal')
        plt.subplot(131, aspect='equal')
        plt.plot(light_x, light_y, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('x vs y')
        
        plt.subplot(132,aspect='equal')
        plt.plot(light_x, light_z, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('x')
        plt.ylabel('z')
        plt.title('x vs z')
        
        plt.subplot(133, aspect='equal')
        plt.plot(light_z, light_y, '.', markersize = 1, color = 'r', marker = 'o')
        if(plot_light_and_dark == True):
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
        plt.xlim((xlower, xupper))
        plt.ylim((-80, 80))
        plt.xlabel('z')
        plt.ylabel('y')
        plt.title('z vs y')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_xyz', format='png')
    
    return 0
# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
def mass_enc(file_name, rscale):
    path_charles = 'quick_plots/outputs/charles/'
    f = open(path_charles + file_name + '.out')
    lines = []
    lines = f.readlines()
    
    num = 1
    for line in lines:
        if (line.startswith("# ignore")):
            break
        else:
            num += 1
    print num
    lines = lines[num:len(lines)]
    total_mass_l = 0.0
    total_mass_d = 0.0
    mass_enc_l = 0.0
    mass_enc_d = 0.0
    counterl = 0
    counterd = 0
    for line in lines:
        if(line.startswith("</bodies>")):
            break
        tokens = line.split(',')
        isDark = int(tokens[0])
        x = float(tokens[1])
        y = float(tokens[2])
        z = float(tokens[3])
        mass = float(tokens[10])
        r = (x * x + y * y + z * z)**0.5
        #dark is 1
        if(isDark == 0):
            counterl += 1
            total_mass_l += mass
            if(r < rscale):
                mass_enc_l += mass
        if(isDark == 1):
            counterd += 1
            total_mass_d += mass
            if(r < rscale):
                mass_enc_d += mass
                
    print counterd, counterl
    print 'total glob mass: ', total_mass_l * 222288.47
    print 'total dwarf mass: ', total_mass_d * 222288.47
    return mass_enc_d, mass_enc_l

def for_charles():
    plot_output  = y
    run          = n
    move_ro_fo   = n
    get_from_lmc = n
    get_from_tel = n
    list_of_runs = n
    
    #settings#
    lua_file = "charles_EMD_v162.lua"
    ver = ''
    ft = 0.00001 #gyr
    bt = 0.00001   #gyr
    rl = 0.175  #kpc
    rd = 0.175 #kpc
    ml = 5e4   #solar
    md = 1e6   #solar
    
    args = [ft, bt, rl, rd, ml, md]
    
    #output = 'ft2gy_bt2gy_massl1e5_massd5e6_rl0.01_rd0.125'
    #output = 'ft2.04gy_bt2gy_massl1e5_massd5e6_rl0.01_rd0.125_neworbit'
    #output = 'ft2.02gy_bt2gy_massl1e5_massd1e6_rl0.01_rd0.175_neworbit'
    #output = 'ft1.04gy_bt1gy_massl1e5_massd5e6_rl0.01_rd0.125'
    #output = 'output_0gy_null_massl1e5_massd1e6_rl0.01_rd0.175'
    #output = 'ft2.02gy_bt2gy_massl1e5_massd5e6_rl0.01_rd0.250'
    #output = 'ft2.02gy_bt2gy_massl2.5e6_massd2.5e6_rl0.250_rd0.250'
    #output = 'ft2.02gy_bt2gy_mass5e6_r0.250_single_plum'
    #output = 'ft2.02gy_bt2gy_massl1e5_massd1e6_rl0.01_rd0.175_forpaper_unsqreps'
    #output = 'ft2.02gy_bt2gy_massl1e5_massd1e6_rl0.01_rd0.175_forpaper'
    #output = 'ft2.02gy_bt2gy_massl1e5_massd1e6_rl0.01_rd0.175_forpaper_2_with_updated_orbit_paras'
    #output = 'ft4.02gy_bt2gy_massl1e5_massd1e6_rl0.01_rd0.175'
    output = 'ft2.02gy_bt2gy_massl5e4_massd1e6_rl0.01_rd0.175'
    #output = 'ft2.02gy_bt2gy_massl5e4_massd1e6_rl0.01_rd0.175_for_paper'
    
    if(run == True):
        nbody(args, lua_file, output, output, ver)
        os.system("mv quick_plots/outputs/" + output + ".out quick_plots/outputs/charles/")
        
    if(move_ro_fo == True):
        os.system("mv reverse_orbit.out quick_plots/outputs/charles/")
        os.system("mv forward_orbit.out quick_plots/outputs/charles/")
        
    if(get_from_lmc == True):
        os.system("scp $lmc:~/research/quick_plots/outputs/" + output + ".out quick_plots/outputs/charles/")
        
    if(get_from_tel == True):
        os.system("scp $teletraan:~/research/quick_plots/outputs/charles/" + output + ".out quick_plots/outputs/charles/")
        
    if(list_of_runs == True):
        args = [2.0, 2.0, 0.01, 0.125, 1e5 , 5e6]
    
    #mass_enc_d, mass_enc_l = mass_enc(output, rl)
    #print 'mass of dwarf enclosed with globular scale r = ', mass_enc_d * 222288.47
    #print 'mass of globular enclosed with globular scale r = ', mass_enc_l * 222288.47
    if(plot_output == True):
        lb_plot(output)
    return 0
# # # # # # # # # # # # # # # # # # # # # #
def velocity_dispersion():
    args = [3.95, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = 'nbody1'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    nbody(args, l, file_name, file_name, version)
    #lb_plot(file_name)
    os.system("./scripts/velocity_dispersion.py " + file_name)
# # # # # # # # # # # # # # # # # # # # # #
def make_some_hists():
    ver = ''
    para = [3.95, 0.98, 0.2, 0.2, 12, 0.2] #hist2 correct
    hist = "total_sim_test2"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 15, 0.2] #hist3 different mass
    hist = "total_sim_test3"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.93, 0.98, 0.2, 0.2, 12, 0.2] #hist4 slightly different sim time
    hist = "total_sim_test4"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 13, 0.2] #hist5 slightly different mass
    hist = "total_sim_test5"
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 0.98, 0.2, 0.2, 13, 0.213] #hist6 slightly different mass same DM mass
    hist = "total_sim_test6"
    #3.95  4.030612244898
    #0.2  0.8
    #48.032863849765     13
    #nbody(para, lua, hist, hist, ver)
    
    para = [3.95, 4.03061, 0.2, 0.8, 13, 48] #hist7 slightly different mass same DM mass (samish as 6)
    hist = "total_sim_test7"
    #3.95  4.03061
    #0.2  0.8
    #48   13
    nbody(para, lua, hist, hist, ver)
# # # # # # # # # # # # # # # # # # # # # #
def stabity_test():
    args = [0.9862, 0.2, 0.2, 12, .2]

    sim_time        = [0.0001, 0.25, 0.50, 0.75, 1.0, 2.0, 3.0, 4.0]
    ext             = [ "0", "p25", "p50", "p75", "1", "2", "3", "4"]
    N               = 1
    M               = 0
    back_time       = str(args[0])
    r_l             = str(args[1])
    light_r_ratio   = str(args[2])
    mass_l          = str(args[3])
    mass_ratio      = str(args[4])
    
    stability_rebuild = y
    stability_run     = y
    
    if(stability_rebuild == True):
        #os.system("rm -r nbody_test")
        #os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release  -DNBODY_GL=ON -DBOINC_APPLICATION=OFF -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
        os.system("make -j ")
        os.chdir("../")
    
    if(stability_run == True):
        for i in range(M, N):
            os.system("" + path + "nbody_test/bin/milkyway_nbody \
                -f " + path + "lua/Null.lua \
                -o " + path + "data_testing/sim_outputs/output_" + (ext[i]) + "gy.out \
                -n 8 -x -i "+ str(sim_time[i]) + " " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )

    os.chdir("data_testing")    
    os.system("./stability_test.py " + back_time + " " + r_l + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)
# # # # # # # # # # # # # # # # # # # # # #
def get_fornax_binary():
    os.system('scp $fornax:~/research/nbody_test/bin/milkyway_nbody ./nbody_test/bin/milkyway_nbody_fornax')
# # # # # # # # # # # # # # # # # # # # # #
def clean():
    os.system("rm boinc_*")
    
# # # # # # # # # # # # # # # # # # # # # #    
def main():
    if(get_fornax_binary_now == True):
        get_fornax_binary()
        
    standard_run()
    if(charles == True):
        for_charles()
    
    if(make_a_few_hists == True):
        make_some_hists()
    
    #if(run_binary_compare == True):
        #old_new_binary_compare()
        
    #if(run_diff_OS_test == True):
        #diff_OS_test_v160()
        #diff_OS_test_v158()
    
    if(run_stability_test == True):
        stabity_test()
    
    #if(recalc_para_sweep_likes == True):
        #recalc_parameter_sweep_likelihoods()
    
    #if(run_seed_fluctuation_test == True):
        #different_seed_fluctuation()
    
    if(velocity_dispersion_calc == True):
        velocity_dispersion()
    
    if(plot_lb == True):
        lb_plot(output)
        
        
    clean()
        
main()


# # # # # # # # # # # # # # # # # # # # # # # #
# deprecated tests #                          #
# # # # # # # # # # # # # # # # # # # # # # # #
#recalc_para_sweep_likes   = n                #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_diff_OS_test          = n                #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_seed_fluctuation_test = n                #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_binary_compare        = n                #
# # # # # # # # # # # # # # # # # # # # # # # #
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
# # # # # # # # # # # # # # # # # # # # # # # #
#    SWITCHES for standard_run()  #           #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = y                 #
remake                    = y                 #
match_histograms          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
calc_cm                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_hists                = n                 #
plot_overlapping          = n                 #
plot_adjacent             = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
plot_lb                   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
get_fornax_binary_now = n

# # # # # # # # # # # # # # # # # # # # # # # #
# possible tests #                            #
# # # # # # # # # # # # # # # # # # # # # # # #
velocity_dispersion_calc  = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
make_a_few_hists          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
run_stability_test        = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
#recalc_para_sweep_likes   = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_diff_OS_test          = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_seed_fluctuation_test = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #
#run_binary_compare        = n                 #
# # # # # # # # # # # # # # # # # # # # # # # #

#    Histogram names     #
histogram_mw_1d_v162 = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__5_31_16'

#    histograms for runs #
histogram_for_nbody_run = histogram_mw_1d_v162

match_hist_correct = histogram_mw_1d_v162
match_hist_compare = histogram_for_nbody_run
plot_name = 'mw_hist'

output = histogram_for_nbody_run
output1 = match_hist_correct + ".out"
output2 = match_hist_correct + ".out"

#version = '_162_VM' #determines which binary is run
version = ''
#lua = "EMD_v160.lua"
lua = "EMD_v162.lua"
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
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DNBODY_GL=OFF -DNBODY_STATIC=OFF -DBOINC_APPLICATION=ON -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
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
        -n 8 -b  -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio )
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
    plot_lbr = y
    plot_light_and_dark = y
    plot_dm = y
    
    plot_xyz = n
    f = open('quick_plots/outputs/' + file_name + '.out')
    lines = []
    lines = f.readlines()
    lines = lines[5:len(lines)]

    light_x , light_y , light_z = ([] for i in range(3))
    light_l , light_b , light_r = ([] for i in range(3))
    light_vx , light_vy , light_vz = ([] for i in range(3))
    
    dark_x , dark_y , dark_z = ([] for i in range(3))
    dark_l , dark_b , dark_r = ([] for i in range(3))
    dark_vx , dark_vy , dark_vz = ([] for i in range(3))

    for line in lines:

        tokens = line.split(', ')
        isDark = int(tokens[0])
        X = float(tokens[1])
        Y = float(tokens[2])
        Z = float(tokens[3])
        l = float(tokens[4])
        #if(l > 180.0):
            #l = l - 360.0
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
    light_x = np.array(light_x)
    light_y = np.array(light_y)
    light_z = np.array(light_z)
    light_l = np.array(light_l)
    light_b = np.array(light_b)
    light_r = np.array(light_r)
    light_vx = np.array(light_vx)
    light_vy = np.array(light_vy)
    light_vz = np.array(light_vz)
    
    dark_x = np.array(dark_x)
    dark_y = np.array(dark_y)
    dark_z = np.array(dark_z)
    dark_l = np.array(dark_l)
    dark_b = np.array(dark_b)
    dark_r = np.array(dark_r)
    dark_vx = np.array(dark_vx)
    dark_vy = np.array(dark_vy)
    dark_vz = np.array(dark_vz)
    
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.8, wspace = 0.8)
    
    if(plot_lbr == True):
        xlower = 360
        xupper = 0.0
        ylower = -80
        yupper = 80
        plt.xlim((xlower, xupper))
        plt.ylim((ylower, yupper))
        plt.xlabel('l')
        plt.ylabel('b')
        plt.title('l vs b')
        
        #default to just plot lm
        plt.plot(light_l, light_b, '.', markersize = 1, color = 'r', marker = 'o')
        plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_light', format='png')
        
        if(plot_light_and_dark == True):#plot lm and dm overlapping
            plt.plot(dark_l, dark_b, '.', markersize = 1, color = 'b', marker = '+')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter', format='png')
            
        if(plot_dm == True):#to plot just dm
            plt.clf()
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
        
# # # # # # # # # # # # # # # # # # # # # #
#        different test functions         #
# # # # # # # # # # # # # # # # # # # # # #
def velocity_dispersion():
    args = [3.95, 1.0, 0.2, 0.8, 12, 48]
    file_name = 'velocity_dispersion_test_pot_lbr_xyz_3.95gy'
    file_name = 'test2'
    #l = 'Null.lua'
    l = 'EMD_v160_direct_fit.lua'
    #nbody(args, l, file_name, file_name, version)
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


def clean():
    os.system("rm boinc_finish_called")
    os.system("rm boinc_milkyway_nbody_1.54_x86_64-pc-linux-gnu__mt_0")
    os.system("rm boinc_milkyway_nbody_1.58_x86_64-pc-linux-gnu__mt_0")
# # # # # # # # # # # # # # # # # # # # # #    
def main():

    if(get_fornax_binary_now == True):
        get_fornax_binary()
        
    standard_run()
    
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
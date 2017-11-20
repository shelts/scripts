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
from nbody_functional import *
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
args_run_comp = [3.95, 0.98, 0.2, 0.2, 12, 0.2] 
#args_run_comp = [3.28828657813, 0.98, 0.2, 0.2, 12, 0.2]

#args_run_comp = [2.08, 0.98, 0.2, 0.3, 12, 0.45] 
#args_run = [0.001, 0.98, 0.2, 0.2, 12, 0.2] 


# # # # # # # # # # # # # # # # # # # # # # # #
#              Standard Run switches          #
# # # # # # # # # # # # # # # # # # # # # # # #
run_nbody                 = y                 #
remake                    = n                 #
match_histograms          = n                 #
run_and_compare           = y                 #
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
histogram_v166 = 'hist_v166_3p95_0p98_0p2_0p2_12_0p2__9_27_17'

#    histograms for runs  #
#correct = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_mw'
correct1 = 'arg_3.95_0.98_0.2_0.2_12_0.2_correct_diff_seed'

#    hist to match against for compare after run  #
correct_hist = 'test'
compare_hist = 'test2'







#    hist name for the nbody run   #
correctans_hist = correct_hist
comparison_hist = compare_hist

plot_name = compare_hist



#    run specfics   #
#version = '_1.62_x86_64-pc-linux-gnu__mt'
version  = ''
lua = "full_control.lua"
#lua = "manual_body_input.lua"
#lua = "halo_object_dev.lua"
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

# # # # # # # # # # # # # # # # # # # # # #
#    standard nbody running functions     #
# # # # # # # # # # # # # # # # # # # # # #
def standard_run():
    nbody = nbody_running_env(lua, version, path)
    
    if(remake):
        nbody.build()
        
    if(run_nbody):
        nbody.run(args_run, correctans_hist)
    
    if(run_and_compare):
        nbody.run(args_run_comp, correctans_hist, comparison_hist)
    
    if(match_histograms):
        nbody.match_hists(correctans_hist, comparison_hist)
        
    if(plot_hists):
        plot(correctans_hist , comparison_hist, plot_name, '1', '2')
        
    if(plot_veldisp_switch):
        plot_veldisp(correctans_hist , comparison_hist, plot_name + "_velDisp", '1', '2')
    
    
    if(vlos_plot_switch):
        vlos_plot(correctans_hist, comparison_hist)
        vlos_plot_single(correctans_hist)
        
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

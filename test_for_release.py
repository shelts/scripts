#! /usr/bin/python
import os
import time
from subprocess import call
import sys
from pexpect import pxssh

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Control Panel       #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
y = True
n = False
# # # # # # # # # # # # # # # # # # # # # # # #
#    SWITCHES for standard_run()  #           #
# # # # # # # # # # # # # # # # # # # # # # # #
build                     = y                 #
create_hist               = n                 #
write_shell               = n                 #
send_to_others            = n                 #
run_everywhere            = n
# # # # # # # # # # # # # # # # # # # # # # # #

args_correct = [3.945, 0.98, 0.2, 0.2, 12, 0.2]
test_parameters = [3.87427734322731, 0.948765315488652, 0.356895748596523, .145236987452136, 10.1548765394315, 0.185215358746843]
hist_correct = 'hist_v162_ft3p945_rt0p98_rl0p2_rr0p2_ml12_mrp2__6_20_16'
hist_test1_mt = 'test_parameters_correct_mt'
hist_test2_mt = 'test_parameters_different_mt'
hist_test1_st = 'test_parameters_correct_st'
hist_test2_st = 'test_parameters_different_st'

out = hist_correct
lua = 'EMD_v162.lua'
version_mt = '_1.62_x86_64-pc-linux-gnu__mt'
version_st = '_1.62_x86_64-pc-linux-gnu'

lmc_dir = '~/research/'
sid_dir = '~/Desktop/research/'
sgr_dir = '/Users/master/sidd_research/'
path = lmc_dir
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Engine Room         #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def build_binary():
    os.chdir("./")
    os.system("rm -r nbody_test")
    os.system("mkdir nbody_test")
    os.chdir("nbody_test")
    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=ON -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=ON -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + path + "milkywayathome_client/")
    os.system("make -j ")

    os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=ON -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=ON -DSEPARATION=OFF -DNBODY_OPENMP=OFF    " + path + "milkywayathome_client/")
    os.system("make -j ")
    os.chdir("../")

def create_histogram():
    sim_time      = str(args_correct[0])
    back_time     = str(args_correct[1])
    r0            = str(args_correct[2])
    light_r_ratio = str(args_correct[3])
    mass_l        = str(args_correct[4])
    mass_ratio    = str(args_correct[5])
    
    print('running nbody')
    os.system(" " + path + "nbody_test/bin/milkyway_nbody" + version_mt + " \
        -f " + path + "lua/" + lua + " \
        -z " + path + "quick_plots/hists/" + hist_correct + ".hist \
        -o " + path + "quick_plots/outputs/" + hist_correct + ".out \
        -n 12 -b -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio)

def write_shell_run_script(script_name):
    sim_time      = str(args_correct[0])
    back_time     = str(args_correct[1])
    r0            = str(args_correct[2])
    light_r_ratio = str(args_correct[3])
    mass_l        = str(args_correct[4])
    mass_ratio    = str(args_correct[5])    
    
    f = open(script_name, 'w')
    f.write("#!/bin/bash\n\n")
    f.write("cd " + path + "nbody_test/bin/\n\n")
    
    f.write("#MULTI THREADED\n")
    f.write("./milkyway_nbody" + version_mt + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-z " + path + "quick_plots/hists/" + hist_test1_mt + ".hist ")
    f.write("-n 12 -b -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + "\n\n")
    
    f.write("./milkyway_nbody" + version_mt + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-s " + path + "quick_plots/hists/" + hist_test1_mt + ".hist \n\n")
    
    sim_time      = str(test_parameters[0])
    back_time     = str(test_parameters[1])
    r0            = str(test_parameters[2])
    light_r_ratio = str(test_parameters[3])
    mass_l        = str(test_parameters[4])
    mass_ratio    = str(test_parameters[5]) 
    
    f.write("./milkyway_nbody" + version_mt + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-z " + path + "quick_plots/hists/" + hist_test2_mt + ".hist ")
    f.write("-n 12 -b -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + "\n\n")
    
    f.write("./milkyway_nbody" + version_mt + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-s " + path + "quick_plots/hists/" + hist_test2_mt + ".hist \n\n")
    
    
    f.write("#SINGLE THREADED\n")
    f.write("./milkyway_nbody" + version_st + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-z " + path + "quick_plots/hists/" + hist_test1_st + ".hist ")
    f.write("-n 12 -b -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + "\n\n")
    
    f.write("./milkyway_nbody" + version_st + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-s " + path + "quick_plots/hists/" + hist_test1_st + ".hist \n\n")
    
    sim_time      = str(test_parameters[0])
    back_time     = str(test_parameters[1])
    r0            = str(test_parameters[2])
    light_r_ratio = str(test_parameters[3])
    mass_l        = str(test_parameters[4])
    mass_ratio    = str(test_parameters[5]) 
    
    f.write("./milkyway_nbody" + version_st + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-z " + path + "quick_plots/hists/" + hist_test2_st + ".hist ")
    f.write("-n 12 -b -i " + sim_time + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + "\n\n")
    
    f.write("./milkyway_nbody"  + version_st + " ")
    f.write("-f " + path + "lua/" + lua + " ")
    f.write("-h " + path + "quick_plots/hists/" + hist_correct + ".hist ")
    f.write("-s " + path + "quick_plots/hists/" + hist_test2_st + ".hist \n\n")
        
    f.close()

def send():
    lmc = 'shelts@lmc.phys.rpi.edu'
    tel = 'shelts@teletraan-i.phys.rpi.edu'
    cos = 'shelts@cosmos.phys.rpi.edu'
    
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_mt + "  " + lmc + ":~/research/nbody_test/bin/")
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_st + "  " + lmc + ":~/research/nbody_test/bin/")
    
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_mt + "  " + tel + ":~/research/nbody_test/bin/")
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_st + "  " + tel + ":~/research/nbody_test/bin/")
    
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_mt + "  " + cos + ":~/research/nbody_test/bin/")
    os.system("scp " + path + "nbody_test/bin/milkyway_nbody" + version_st + "  " + cos + ":~/research/nbody_test/bin/")
    
    os.system("scp " + path + "quick_plots/hists/" + hist_correct + ".hist  " + lmc + ":~/research/quick_plots/hists/")
    os.system("scp " + path + "quick_plots/hists/" + hist_correct + ".hist  " + tel + ":~/research/quick_plots/hists/")
    os.system("scp " + path + "quick_plots/hists/" + hist_correct + ".hist  " + cos + ":~/research/quick_plots/hists/")
    
    os.system("scp " + path + "testing_for_release.sh" + "  " + lmc + ":~/research/")
    os.system("scp " + path + "testing_for_release.sh" + "  " + tel + ":~/research/")
    os.system("scp " + path + "testing_for_release.sh" + "  " + cos + ":~/research/")
    
def run_on_others():
    s = pxssh.pxssh()
    hostname = ('lmc.phys.rpi.edu')
    username = ('shelts')

    if not s.login(hostname, username):
        print "SSH session failed on login."
    else:
        print "SSH session login successful"
        s.sendline ('nohup ./testing_for_release.sh ' + name)
        s.prompt()         # match the prompt
        print s.before  
        s.logout()
        s = pxssh.pxssh()
        
        
    hostname = ('cosmos.phys.rpi.edu')
    username = ('shelts')

    if not s.login(hostname, username):
        print "SSH session failed on login."
    else:
        print "SSH session login successful"
        s.sendline ('nohup ./testing_for_release.sh ' + name)
        s.prompt()         # match the prompt
        print s.before  
        s.logout()
        s = pxssh.pxssh()
    
    
    hostname = ('teletraan-i.phys.rpi.edu')
    if not s.login(hostname, username):
        print "SSH session failed on login."
    else:
        print "SSH session login successful"
        s.sendline ('nohup ./testing_for_release.sh ' + name)
        s.prompt()         # match the prompt
        print s.before  
        s.logout()
        s = pxssh.pxssh()
    
    os.system("nohup ./testing_for_release.sh")
    
def main():
    if(build == True):
        build_binary()
    
    if(create_hist == True):
        create_histogram()
        
    if(write_shell == True):
        name = 'testing_for_release.sh'
        write_shell_run_script(name)
        os.system("chmod +x " + name)
    
    if(send_to_others == True):
        send()
        
    if(run_everywhere == True):
        run_on_others()
        
        
main()
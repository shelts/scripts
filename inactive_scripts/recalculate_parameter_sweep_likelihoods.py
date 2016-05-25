def match_hists_piped(hist1, hist2, ver, pipe_name):
    os.system(" " + path + "nbody_test/bin/milkyway_nbody" + ver  
                + " -h " + path + "quick_plots/hists/" + hist1 + '.hist'
                + " -s " + path + "quick_plots/hists/" + hist2 + '.hist'
                + "  2>>'" + pipe_name + ".txt' ")
# # # # # # # # # # 



def recalc_parameter_sweep_likelihoods():
    args = [3.95, 3.95, 0.2, 0.8, 12, 48]
    sim_time      = str(args[0])
    back_time     = str(args[1])
    rl            = str(args[2])
    rd            = str(args[3])
    mass_l        = str(args[4])
    mass_d        = str(args[5])
    names   = ['ft', 'rad', 'rr', 'mass', 'mr_50bins']
    folder = "parameter_sweep_hists/"
    
    hist_range = [2., 1200.0, 23.0]
    hist_correct = folder + names[4] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm " + names[4] + ".txt")
    while(name <= hist_range[1]):
        mass_d = str(name)
        hist_name = folder + names[4] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', names[4])
        name += hist_range[2]
    mass_d = str(args[5])
    
    hist_range = [8.0, 16.0, 0.25]
    hist_correct = folder + names[3] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm mass.txt")
    while(name <= hist_range[1]):
        mass_l = str(name)
        hist_name = folder + names[3] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'mass')
        name += hist_range[2]
    mass_l = str(args[4])
    
    hist_range = [0.7, 0.9, 0.01]
    hist_correct = folder + names[2] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm rr.txt")
    while(name <= hist_range[1]):
        rd = str(name)
        hist_name = folder + names[2] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'rr')
        name += hist_range[2]
    rd = str(args[3])
    
    
    hist_range = [0.1, 0.3, 0.01]
    hist_correct = folder + names[1] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm rad.txt")
    while(name <= hist_range[1]):
        rl = str(name)
        hist_name = folder + names[1] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'rad')
        name += hist_range[2]
    rl = str(args[2])    
        
    args = [3.95, 0.98, 0.2, 0.8, 12, 48]
    sim_time      = str(args[0])
    back_time     = str(args[1])
    rl            = str(args[2])
    rd            = str(args[3])
    mass_l        = str(args[4])
    mass_d        = str(args[5])
    
    hist_range = [3.85, 4.3, 0.025]
    hist_correct = folder + names[0] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + "_correct"
    name = hist_range[0]
    os.system("rm ft.txt")
    while(name <= hist_range[1]):
        sim_time = str(name)
        hist_name = folder + names[0] + "_hists/arg_" + sim_time + "_" + back_time + "_" + rl + "_" + rd + "_" + mass_l + "_" + mass_d + ""
        match_hists_piped(hist_correct, hist_name, '', 'ft')
        name += hist_range[2]

    os.system("mv " + names[4] + ".txt " + path + "like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv mass.txt " + path + "like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv rad.txt " + path + "like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv rr.txt  " + path + "like_surface/1D_like_surface/parameter_sweeps")
    #os.system("mv ft.txt " + path + "like_surface/1D_like_surface/parameter_sweeps")
    os.chdir("like_surface")
    os.system("./one_like_script.py")
    return 1
# # # # # # # # # # # # # # # # # # # # # #
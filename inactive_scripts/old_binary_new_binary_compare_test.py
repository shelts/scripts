def old_new_binary_compare():
    binary_run_nbody = n
    binary_match_histograms = n
    binary_plot_hists = n
    binary_calc_chi_sq = n
    
    versions = ['_154', '_158']
    time  = "1"
    binary_outputs = [with_lua_correction_on_old_binary + time + "gy.out", with_correction_on_new_binary + time + "gy.out"]
    binary_hists   = [with_lua_correction_on_old_binary + time + "gy.hist", with_correction_on_new_binary + time + "gy.hist"]
    folder = "/home/sidd/Desktop/research/outputs/"
    binary_lua = "EMD_20k_1_54_fixed_seed_cm_correction.lua"
    
    if(binary_run_nbody == True):
        nbody(args, binary_lua, binary_hists[0], binary_outputs[0], versions[0], 0)
        nbody(args, binary_lua, binary_hists[1], binary_outputs[1], versions[1], 1)
    
    if(binary_match_histograms == True):
        match_hists(binary_hists[0], binary_hists[0], versions[0]) #match old hist on the old binary
        match_hists(binary_hists[1], binary_hists[1], versions[0]) #match new hist on the old binary
        
        match_hists(binary_hists[0], binary_hists[0], versions[1]) #match old hist on the new binary
        match_hists(binary_hists[1], binary_hists[1], versions[1]) #match old hist on the new binary
        
    if(binary_plot_hists == True):
        plot(hists[0], hists[1])
        
    #os.system("mv " + names[0] + " " + names[1] + " quick_plots")
    
    if(binary_calc_chi_sq == True):
        os.system("./scripts/old_new_binary_chi_sq.py " + folder + outputs[0] + " " + folder + outputs[1] + " " + "output")
        
        
# # # # # # # # # # # # # # # # # # # # # #
#/* Copyright (c) 2016 Siddhartha Shelton */
#these are functions that were removed intact from one_script.py

def diff_OS_test_v158():
    v = ''
    #windows
    args = [4.29822369291337, 0.903418915209326, 0.96168017496667, 0.636458776995275, 34.646854473218, 0.310731262105537]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_3_1453826702_1539995 [1126649807]
    #MW_like = -3.941582191124151
    #laptop_like = 3.380992366981500
    hist = 'OS_test/windows_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)

    args =  [3.64909463274645, 0.800092264528703, 1.29968128990876, 0.572091462517946, 119.996024088228, 0.294493798125456]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_1_1453826702_1691839 [1129898216]
    #MW_like =  0.668375079402415
    #laptop_like =  0.881392082076118
    hist = 'OS_test/windows_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.65144453661503, 0.919067429256722, 1.22340315081706, 0.854927185363449, 39.0082337940657, 0.500514083832232]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_3_1453826702_1708283 [1130209342]
    #MW_like =  0.140110685580532
    #laptop_like =  0.182138917764999
    hist = 'OS_test/windows_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)   
    
    args =  [4.19661544276295, 0.897629903758155, 1.29495109835948, 0.896362260366003, 52.5909815487292, 0.542975688910794]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_8_16_orphansim_v156_1_1453826702_1415872 [1122507395]
    #MW_like =  1.132654164145936
    #laptop_like =  10.256920398728917
    hist = 'OS_test/windows_multithreaded4'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [3.59013215543578, 0.8, 1.3, 0.61475411883109, 120, 0.310571082931839]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_1_1453826702_1694659 [1129955208]
    #MW_like =  21.420239313972647
    #laptop_like =  20.349634374025626
    hist = 'OS_test/windows_multithreaded5'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.59379936660717, 0.917773637213971, 1.23133908813293, 0.852202997878081, 39.1675896978381, 0.503544745988189]
    #OS: milkyway_nbody 1.58 Windows x86_64 double  OpenMP
    #workunit:  ps_nbody_3_21_16_orphansim_v158_3_1453826702_1694823 [1129959188]
    #MW_like =  0.701643535578343
    #laptop_like =  2.412993814130235
    hist = 'OS_test/windows_multithreaded6'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    #linux:    
    args = [3.54663939082478, 0.817954573674686, 1.27616329135743, 0.615843914911811, 118.889074577371, 0.325446608590623]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1551799 [1126955705]
    #MW_like = -447.279182742111402
    #laptop_like = 436.441079660549804
    hist = 'OS_test/linux_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args = [3.55130600333676, 0.8, 1.3, 0.64627393759699, 120, 0.335997932965623]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1683119 [1129726733]
    #MW_like = -37.147633105012268
    #laptop_like = 31.344591576360859
    hist = 'OS_test/linux_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    args = [3.70941156624545, 0.8, 1.3, 0.594552172354105, 120, 0.296728543273283]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1706469 [1130177360]
    #MW_like = -1.158941882456867
    #laptop_like = 0.153304537068448
    hist = 'OS_test/linux_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args = [4.19661544276295, 0.897629903758155, 1.29495109835948, 0.896362260366003, 52.5909815487292, 0.542975688910794]
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_8_16_orphansim_v156_1_1453826702_1415872 [1122507395]
    #MW_like = -1.132654164145936
    #laptop_like =  10.256920398728917
    hist = 'OS_test/linux_multithreaded4'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args = [3.56693763038042, 0.8, 1.3, 0.554551674635198, 119.854123758034, 0.305987721006952] 
    #OS: milkyway_nbody 1.58 Linux x86_64 double  OpenMP
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1697633 [1130014242]
    #MW_like = -4.074673238994799 
    #laptop_like =  5.045502971691247
    hist = 'OS_test/linux_multithreaded5'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v158, hist, v)
    
    #mac
    args = [4.85215253988281, 0.811699599213898, 0.259284052159637, 0.892385273054242, 101.71602185443, 0.366507535497658]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit: ps_nbody_3_21_16_orphansim_v158_1_1453826702_1419252 [1122650947]
    #MW_like = -568.469347072597884
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded1'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    
    args =  [3.48619072407142, 0.93569692173099, 0.997117511086704, 0.88680122652172, 29.086175902524, 0.309459403191991]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit:  ps_nbody_3_8_16_orphansim_v156_2_1453826702_1418150 [1122562759]
    #MW_like =  -0.709366128677001
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded2'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    args =  [4.32493866118717, 0.90350496717366, 1.29756680316448, 0.891263826616564, 48.8403305705139, 0.544722103651006]
    #OS: milkyway_nbody 1.58 Darwin x86_64 double
    #workunit:  ps_nbody_3_8_16_orphansim_v156_1_1453826702_1390970 [1121841784]
    #MW_like =  -2.121557178729414
    #laptop_like = 
    hist = 'OS_test/mac_multithreaded3'
    output = hist
    #nbody(args, lua, hist, output, v)
    #match_hists(histogram_mw_1d_v158, hist, v)
    
    return 1
# # # # # # # # # # # # # # # # # # # # # #
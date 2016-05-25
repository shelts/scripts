def diff_OS_test_v160():
    v = ''
    linux = n
    windows = n
    
    args = [4.99437258372485, 0.891649783307308, 1.10684417920164, 2.28622114462683, 58.8750832674317, 460.143966582794]
    #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm 
    #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_3400209 [1153419819]
    #MW_like = -295.632987377041790
    #LMC_with_parameters directly written in lua = -295.632992528164323
    #laptop_like_multi = -308.238341155806722
    #laptop_after_matching_windows = -304.164914230333522
    hist = 'OS_test/windows_multithreaded5'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    
    args = [3.87427734322731, 1.01387196544634, 1.29523584391164, 2.99564367318775, 26.1017521350673, 131.258621913187]
    #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
    #workunit: ps_nbody_4_14_16_orphansim_v160_3_1453826702_3302962 [1152540540]
    #MW_like = -1591.646667079636500
    #LMC_with_parameters directly written in lua = -1591.646645167359111
    #laptop_like_multi = -1591.649439867483352
    #laptop_multi_static = -1591.649439867483352
    #laptop_after_matching_windows = -1591.646622880012274
    hist = 'OS_test/windows_multithreaded1_0gy_null'
    output = hist
    #nbody(args, lua, hist, output, v)
    match_hists(histogram_mw_1d_v160, hist, v)
    
    if(windows == True):
        #windows
        args = [3.87427734322731, 1.01387196544634, 1.29523584391164, 2.99564367318775, 26.1017521350673, 131.258621913187]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
        #workunit: ps_nbody_4_14_16_orphansim_v160_3_1453826702_3302962 [1152540540]
        #MW_like = -1591.646667079636500
        #LMC_with_parameters directly written in lua = -1591.646645167359111
        #laptop_like_multi = -1591.649439867483352
        #laptop_single = 
        #laptop_multi_static = -1591.649439867483352
        hist = 'OS_test/windows_multithreaded1'
        output = hist
        #nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [4.99591109942796, 0.893963217080646, 1.09139516383981, 2.2505519089581, 57.769204038868, 477.39115356239]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
        #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_3187656 [1151509194]
        #MW_like = -35.961996959483578
        #laptop_like_multi = -35.353030758426641
        #laptop_single = 
        #laptop_multi_static =-35.353030758426641
        hist = 'OS_test/windows_multithreaded2'
        output = hist
        #nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [4.99518109716855, 0.894630524992357, 1.12697810375362, 2.29332302971577, 58.9627482245134, 477.75245822501]
        #OS:  milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
        #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_3302452 [1152536278]
        #MW_like = -32.820805876368382
        #laptop_like_multi = -32.010253463412312
        #laptop_single = -32.010253463412312
        hist = 'OS_test/windows_multithreaded3'
        output = hist
        #nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.59371228338975, 0.960668713401728, 0.599260189737485, 2.89204324566376, 22.6509509936559, 300.154841212772]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
        #workunit: ps_nbody_4_14_16_orphansim_v160_1_1453826702_3396367 [1153385353]
        #MW_like = -143.192302468235600
        #laptop_like_multi = -142.994280153233319
        hist = 'OS_test/windows_multithreaded4'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [4.99437258372485, 0.891649783307308, 1.10684417920164, 2.28622114462683, 58.8750832674317, 460.143966582794]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm 
        #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_3400209 [1153419819]
        #MW_like = -295.632987377041790
        #laptop_like_multi = -308.238341155806722
        hist = 'OS_test/windows_multithreaded5'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.62651407569746, 0.958136076049239, 0.635878941348239, 2.889179456962, 20.1302128506159, 288.408902457954]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  , Crlibm 
        #workunit:  ps_nbody_4_14_16_orphansim_v160_1_1453826702_3409800 [1153508410]
        #MW_like = -28.714008474268674
        #laptop_like_multi = -28.817376017023140
        hist = 'OS_test/windows_multithreaded6'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [5, 0.940125402763589, 1.09842030523995, 2.1362602293744, 60, 600]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm
        #workunit:  ps_nbody_4_14_16_orphansim_v160_2_1453826702_3314505 [1152638824]
        #MW_like = -3090.048639610829500
        #laptop_like_multi = -3067.649968787237412
        hist = 'OS_test/windows_multithreaded7'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.61617100791001, 0.957377619356007, 0.642877878545248, 2.89266208243634, 19.7837628572825, 289.153996968709]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm 
        #workunit:  ps_nbody_4_14_16_orphansim_v160_1_1453826702_3404893 [1153463266]
        #MW_like = -19.584715268589605
        #laptop_like_multi = -20.048038924522746
        hist = 'OS_test/windows_multithreaded8'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.37866157256478, 0.934105725918354, 1.29499184441929, 2.99692050296758, 43.4836358484412, 1]
        #OS: milkyway_nbody 1.60 Windows x86_64 double  OpenMP, Crlibm 
        #workunit:  ps_nbody_4_14_16_orphansim_v160_3_1453826702_3081538 [1150480556]
        #MW_like = -133.299125231486300
        #laptop_like_multi = -133.299122418788841
        hist = 'OS_test/windows_multithreaded9'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
    if(linux == True):
        #linux
        args = [3.70778452511877, 1.01667175907642, 0.254742649011314, 0.143711601383984, 11.3450273240451, 574.759386941092]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_2757434 [1146228735]
        #MW_like = 579.736066389484677
        #laptop_like_multi = -564.961726428886095
        #laptop_single = 
        #laptop_multi_static =-564.961726428886095
        hist = 'OS_test/linux_multithreaded1'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        
        args = [4.27052977262065, 0.898590506706387, 1.13573807105422, 1.05763955467846, 4.26117976009846, 505.117312682793]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit:ps_nbody_4_14_16_orphansim_v160_1_1453826702_2757546 [1146230255]
        #MW_like = -2411.196889060096055
        #laptop_like_multi = -2407.992198395417290
        #laptop_single = 
        #laptop_multi_static =-2407.992198395417290
        hist = 'OS_test/linux_multithreaded2'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [4.28939779102802, 1.1479856419377, 0.81844124076888, 1.40610990077257, 42.8358124603983, 493.859601157717]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit: ps_nbody_4_14_16_orphansim_v160_2_1453826702_2757751 [1146232693]
        #MW_like = -12991.388977929243993
        #laptop_like_multi = -13097.004861729281401
        #laptop_single = 
        #laptop_multi_static =-13097.004861729281401
        hist = 'OS_test/linux_multithreaded3'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.90124507574365, 0.940801729913801, 0.864376512635499, 0.365644396073185, 54.3746401073877, 376.632761744782]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit: ps_nbody_4_14_16_orphansim_v160_1_1453826702_2757837 [1146235164]
        #MW_like = -1103.915226218623047
        #laptop_like_multi = -1059.128753402558232
        #laptop_single = 
        #laptop_multi_static =-1059.128753402558232
        hist = 'OS_test/linux_multithreaded4'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.15275016007945, 1.01077198171988, 0.518699688930064, 1.16948326204438, 45.0927923207637, 224.0722140742]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit: ps_nbody_4_14_16_orphansim_v160_1_1453826702_2758001 [1146237706]
        #MW_like = -7276.429429114665254
        #laptop_like_multi = -7253.815399924838857
        #laptop_single = 
        #laptop_multi_static =-7253.815399924838857
        hist = 'OS_test/linux_multithreaded5'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
        
        args = [3.47986795054749, 1.13666507601738, 0.755570971686393, 1.23453689094167, 50.398002382135, 426.925432941876]
        #OS: milkyway_nbody 1.60 Linux x86_64 double  OpenMP
        #workunit: ps_nbody_4_14_16_orphansim_v160_3_1453826702_2758209 [1146240830]
        #MW_like = -17637.067619180670590
        #laptop_like_multi = -17812.410820521141432
        #laptop_single = 
        #laptop_multi_static =-17812.410820521141432
        hist = 'OS_test/linux_multithreaded6'
        output = hist
        nbody(args, lua, hist, output, v)
        match_hists(histogram_mw_1d_v160, hist, v)
# # # # # # # # # # # # # # # # # # # # # #
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
        X = float(tokens[1])
        Y = float(tokens[2])
        Z = float(tokens[3])
        mass = float(tokens[10])
        r = (X * X + Y * Y + Z * Z)**0.5
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
    plot_output  = n
    plot_hists   = y
    run          = n
    move_ro_fo   = n
    get_from_lmc = n
    get_from_tel = n
    list_of_runs = n
    
    #settings#
    lua_file = "charles_EMD_v162.lua"
    ver = ''
    ft = 2.02 #gyr
    bt = 2.0   #gyr
    rl = 0.01  #kpc
    rd = 0.01 #kpc
    ml = 5e4   #solar
    md = 1e6   #solar
    
    args = [ft, bt, rl, rd, ml, md]
    
    
    
    #output = 'ft2.02gy_bt2gy_massl5e4_massd1e6_rl0.01_rd0.175_for_paper'
    #output = 'charles/ft2.02gy_bt2gy_mass1e6_r0.175_single_dwarf'
    #output = 'ft2.02gy_bt2gy_mass5e4_r0.01_single_globular'
    #output = 'ft2.02gy_bt2gy_massl5e4_massd5e4_rl0.01_rd0.01_both_globular'
    #output = 'ft2.02gy_bt2gy_massl1e6_massd1e6_rl0.175_rd0.175_both_dwarf'
    output = 'ft2.02gy_bt2gy_massl5e4_massd1e6_rl0.01_rd0.01'
    
    if(run == True):
        nbody(args, lua_file, output, output, ver, False)
        os.system("mv quick_plots/outputs/" + output + ".out quick_plots/outputs/charles/")
        
    if(move_ro_fo == True):
        os.system("mv reverse_orbit.out quick_plots/outputs/charles/")
        os.system("mv forward_orbit.out quick_plots/outputs/charles/")
        
    if(get_from_lmc == True):
        os.system("scp $lmc:~/research/quick_plots/outputs/" + output + ".out quick_plots/outputs/charles/")
        
    if(get_from_tel == True):
        os.system("scp $teletraan:~/research/quick_plots/outputs/charles/" + output + ".out quick_plots/outputs/charles/")
        
    if(list_of_runs == True):
        ft = 2.02 #gyr
        bt = 2.0   #gyr
        rl = 0.175  #kpc
        rd = 0.175 #kpc
        ml = 5e4   #solar
        md = 1e6   #solar
        args = [ft, bt, rl, rd, ml, md]
        output = 'charles/ft2.02gy_bt2gy_mass1e6_r0.175_single_dwarf'
        nbody(args, lua_file, output, output, ver, False)
        
        ft = 2.02 #gyr
        bt = 2.0   #gyr
        rl = 0.01  #kpc
        rd = 0.01 #kpc
        ml = 5e4   #solar
        md = 5e4   #solar
        args = [ft, bt, rl, rd, ml, md]
        output = 'charles/ft2.02gy_bt2gy_mass5e4_r0.01_sinle_globular'
        nbody(args, lua_file, output, output, ver, False)
        
    if(plot_output == True):
        lb_plot(output)
        
    return 0
# # # # # # # # # # # # # # # # # # # # # #



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
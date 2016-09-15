def lb_plot_charles(file_name):
    path_charles = 'quick_plots/outputs/charles/'
    path = 'quick_plots/outputs/'
    print file_name
    plot_lbr = y
    plot_light_and_dark = n
    plot_dm = n
    plot_xyz = n
    plot_orbit = n
    plot_orbit_points = n
    plot_poly_points = n
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
    #print(len(light_l))
    #print(len(dark_l))
    
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
        #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_light', format='png')
        print("plotting:", len(light_l), " points")
        plt.show()
        # # # # # # # # # #
        if(plot_light_and_dark == True):#plot lm and dm overlapping
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(dark_l, dark_b, '.', markersize = 1.5, color = 'purple', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter', format='png')
            print("plotting:", len(light_l) + len(dark_l), " points")
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
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')

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
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name, format='png')
            
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
            plt.title('l vs b ' + file_name)
            plt.plot(orbpoly_l, orbpoly_b, '.', markersize = 3, color = 'g', alpha= 1.0, marker = 'o')
            #os.system("mpg123  rasengan.mp3 ")
            #plt.show()
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/' + file_name + 'with_poly', format='png')
            
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



def multiple_plot():
    run_disp = n
    coors = 'lambda_beta'
    #coors = 'lb'
    which_matter = 'light'
    save_folder = 'quick_plots/comp_hist_plots/'
    
    rows = 3
    columns = 2
    
    ylimit = 1500
    xlower = 180 
    xupper = -180
    w_overlap = 2.5
    w_adjacent = 1.5
    ylimit2 = 30
    ylimit3 = 30

    name = 'output_vs_vel_disp_' + coors + "_orphan_" + which_matter
    hists = ['ft3.945gy_bt4.02gy_massl6.0_massd6.0_rl0.2_rd0.2_both_globular_orphan',
             'ft2.02gy_bt2gy_mass5e4_r0.01_single_globular',
             'ft3.945gy_bt4.02gy_massl12.0_massd78.1_rl0.2_rd0.2_orphan',
             'ft3.945gy_bt4.02gy_massl12_massd1039.21_rl0.2_rd0.8_orphan',
             'hermus.1e5.10pc.orb31.2.1.nbody',
             'hermus.1.05e6.10pc.1.nbody']
    
    #lb_plot('ft2.02gy_bt2gy_massl5e4_massd5e4_rl0.01_rd0.01_both_globular_orphan')
    #os.system("" + path + "scripts/plot_matching_hist.py " + hist1 + " " + hist2)
    for i in range(1, len(hists) + 1):
        print "plot histogram " + str(i) + ": ", hists[i - 1]

    # # # # # 1 # # # # #
    l1    = []; n1    = []
    l1_vd = []; n1_vd = []
    #l1, n1        = l_count_data_from_hist(hists[0] + ".hist" )
    l1, n1        = l_counts_from_output_data(hists[0], run_disp, 'mw' , coors, which_matter )
    l1_vd, n1_vd  = l_vel_disp_count_data(hists[0], n, 'mw' , coors, which_matter  )
    #l1_vd, n1_vd        = l_count_data_from_hist(hists[0] + ".hist" )
    
    leg1 = Rectangle((0, 0), 0, 0, alpha=0.0)
    plt.figure(figsize=(20,10))
    plt.rc('xtick', labelsize=20) 
    plt.rc('ytick', labelsize=20) 
    plt.subplot(rows, columns, 1)
    #plt.title('Position Histogram After 3.945 Gy')
    #f, (f1, f2) = plt.subplots(2, sharex = True, sharey = True)
    plt.bar(l1, n1, width = w_adjacent, color='b')
    plt.legend([leg1], ['Stars Only'], handlelength=0, frameon=False, framealpha=0)
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'Stars Only',handlelength=0)])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit))
    plt.ylabel('counts', fontsize=20)
    
    plt.subplot(rows, columns, 2)
    #plt.title('Velocity Dispersion After 3.945 Gy')
    plt.bar(l1_vd, n1_vd, width = w_adjacent, color='b')
    plt.legend([leg1], ['Stars Only'], handlelength=0, framealpha=0)
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'Stars Only')])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit2))
    plt.ylabel('$\sigma$', fontsize=20)
    
    ## # # # # 2 # # # # # 
    #l2 = []; n2 = []
    #l2_vd = []; n2_vd = []
    ##l2, n2 = l_count_data_from_hist(hists[1] + ".hist")
    #l2, n2        = l_counts_from_output_data(hists[1], run_disp, 'mw' , coors, which_matter  )
    #l2_vd, n2_vd  = l_vel_disp_count_data(hists[1], n, 'mw' , coors, which_matter  )
    ##l2_vd, n2_vd = l_count_data_from_hist(hists[1] + ".hist")
    
    #plt.subplot(rows, columns, 3)
    #plt.bar(l2, n2, width = w_adjacent, color='b')
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'single_glob')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit))
    #plt.ylabel('counts')
    
    #plt.subplot(rows, columns, 4)
    #plt.bar(l2_vd, n2_vd, width = w_adjacent, color='b')
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'single_glob')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit2))
    #plt.ylabel('$\sigma$')
   
    # # # # # 3 # # # # # 
    l3 = []; n3 = []
    l3_vd = []; n3_vd = []
    #l3, n3 = l_count_data_from_hist(hists[2] + ".hist")   
    l3, n3        = l_counts_from_output_data(hists[2], run_disp, 'mw' , coors, which_matter  )
    l3_vd, n3_vd  = l_vel_disp_count_data(hists[2], n, 'mw' , coors, which_matter  )        
    #l3_vd, n3_vd = l_count_data_from_hist(hists[2] + ".hist")   
    
    plt.subplot(rows, columns, 3)
    plt.bar(l3, n3, width = w_adjacent, color='b')
    plt.legend([leg1], ['Mass Follows Light'], handlelength=0, framealpha=0)
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'Mass Follows Light')])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit))
    plt.ylabel('counts', fontsize=20)
    
    plt.subplot(rows, columns, 4)
    plt.bar(l3_vd, n3_vd, width = w_adjacent, color='b')
    plt.legend([leg1], ['Mass Follows Light'], handlelength=0, framealpha=0)
    #plt.legend(handles=[mpatches.Patch(color='b', label= 'Mass Follows Light')])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit3))
    plt.ylabel('$\sigma$', fontsize=20)
    
    # # # # # 4 # # # # # 
    l4 = []; n4 = []
    l4_vd = []; n4_vd = []
    #l4, n4 = l_count_data_from_hist(hists[3] + ".hist")
    l4, n4        = l_counts_from_output_data(hists[3], run_disp, 'mw' , coors, which_matter  )
    l4_vd, n4_vd  = l_vel_disp_count_data(hists[3], n, 'mw' , coors, which_matter  )
    #l4_vd, n4_vd = l_count_data_from_hist(hists[3] + ".hist")
    
    plt.subplot(rows, columns, 5)
    plt.bar(l4, n4, width = w_adjacent, color='b')
    plt.legend([leg1], ['Extended Dark Matter Halo'], handlelength=0, framealpha=0)
    #plt.legend(handles=[mpatches.Patch(color='b', label='Extended Dark Matter Halo')])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit))
    #plt.xlabel('l')
    plt.ylabel('counts', fontsize=20)
    plt.xlabel('$\Lambda$', fontsize=20)
    
    plt.subplot(rows, columns, 6)
    plt.bar(l4_vd, n4_vd, width = w_adjacent, color='b')
    plt.legend([leg1], ['         Extended Dark Matter Halo'], handlelength=0, framealpha=0, loc= 9)
    #plt.legend(handles=[mpatches.Patch(color='b', label='Extended Dark Matter Halo')])
    plt.xlim((xlower, xupper))
    plt.ylim((0.0, ylimit3))
    plt.ylabel('$\sigma$', fontsize=20)
    
    # # # # # 5 # # # # # 
    #l5 = []; n5 = []
    #l5_vd = []; n5_vd = []
    #l5, n5        = l_counts_from_output_data(hists[4], run_disp, 'nemo' , coors, which_matter  )
    #l5_vd, n5_vd  = l_vel_disp_count_data(hists[4], n, 'nemo' , coors, which_matter  )
    
    #plt.subplot(rows, columns, 9)
    #plt.bar(l5, n5, width = w_adjacent, color='k')
    #plt.legend(handles=[mpatches.Patch(color='k', label='nemo glob')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit))
    ##plt.xlabel('l')
    #plt.ylabel('counts')
    
    #plt.subplot(rows, columns, 10)
    #plt.bar(l5_vd, n5_vd, width = w_adjacent, color='b')
    #plt.legend(handles=[mpatches.Patch(color='b', label='nemo glob')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit3))
    #plt.ylabel('$\sigma$')
    
    ## # # # # 6 # # # # # 
    #l6 = []; n6 = []
    #l6_vd = []; n6_vd = []
    #l6, n6        = l_counts_from_output_data(hists[5], run_disp, 'nemo' , coors, which_matter  )
    #l6_vd, n6_vd  = l_vel_disp_count_data(hists[5], n, 'nemo' , coors, which_matter  )
    
    #plt.subplot(rows, columns, 11)
    #plt.bar(l6, n6, width = w_adjacent, color='k')
    #plt.legend(handles=[mpatches.Patch(color='k', label='nemo light fol dark')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit))
    #plt.xlabel('$\Lambda$')
    #plt.ylabel('counts')
    
    #plt.subplot(rows, columns, 12)
    #plt.bar(l6_vd, n6_vd, width = w_adjacent, color='b')
    #plt.legend(handles=[mpatches.Patch(color='b', label='nemo mass fol light')])
    #plt.xlim((xlower, xupper))
    #plt.ylim((0.0, ylimit3))
    plt.xlabel('$\Lambda$', fontsize=20)
    plt.ylabel('$\sigma$', fontsize=20)
    
    
    
    plt.savefig(save_folder + name + '.png', format='png')
    #plt.show()
    
    
    
    
    return 1


def l_vel_disp_count_data(hist_name, run_dispersion, output_type, coors, which_matter):
    if(run_dispersion == True):
        os.system("./scripts/velocity_dispersion.py " + hist_name + " " + output_type + " " + coors + " " + which_matter)
        hist_name = hist_name + "_vel_disp.hist"
        os.system("mv ./" + hist_name + " quick_plots/hists/")
    else:
        hist_name = hist_name + "_vel_disp.hist"
        
    folder = 'quick_plots/hists/'
    
    lines = []
    lines = open(folder + hist_name).readlines();
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("#")):
            break 
        
    lines = lines[starting_line:len(lines)]
    l = []
    nd= []
    for line in lines:
        tokens = line.split(',\t');
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            bda = float(tokens[2])
            cts = float(tokens[4])
            l.append(lda)
            nd.append(cts)
            
    return l, nd

def l_counts_from_output_data(hist_name, run_dispersion, output_type, coors, which_matter):
    if(run_dispersion == True):
        os.system("./scripts/velocity_dispersion.py " + hist_name + " " + output_type + " " + coors + " " + which_matter)
        hist_name = hist_name + "_vel_disp.hist"
        os.system("mv ./" + hist_name + " quick_plots/hists/")
    else:
        hist_name = hist_name + "_vel_disp.hist"
        
    folder = 'quick_plots/hists/'
    
    lines = []
    lines = open(folder + hist_name).readlines();
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("#")):
            break 
        
    lines = lines[starting_line:len(lines)]
    l = []
    nd = []
    for line in lines:
        tokens = line.split(',\t');
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            bda = float(tokens[2])
            cts = float(tokens[3])
            l.append(lda)
            nd.append(cts)
            
    return l, nd

def l_count_data_from_hist(hist_name):
    folder = 'quick_plots/hists/'
    lines = []
    lines = open(folder + hist_name).readlines();
    starting_line = 0
    for line in lines:
        starting_line += 1
        if (line.startswith("betaBins")):
            break 
    lines = lines[starting_line:len(lines)]
    l = []
    nd = []
    for line in lines:
        if (line.startswith("</histogram>")):
            continue
        tokens = line.split();
        if tokens: #tests to make sure tokens is not empty
            lda = float(tokens[1])
            cts = float(tokens[3])
            l.append(lda)
            nd.append(cts)
            
    return l, nd


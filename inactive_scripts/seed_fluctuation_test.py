def nbody_custom_lua(paras, lua_file, hist, out, ver, seed, bins):#this is for lua files that have non-normal parameters
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
        -n 8 -x -e " + seed + " -i " + (sim_time) + " " + back_time + " " + r0 + " " + light_r_ratio + " " + mass_l + " " + mass_ratio + " " + bins)
# # # # # # # # # # 


def different_seed_fluctuation():
    make_compare_hists = n
    make_correct_hists = n
    compare_only = n
    parse = n
    plot = y
    args = [3.95, 0.98, 0.2, 0.8, 12, 48]
    v = '_160'
    l = 'seed_test.lua'
    seed = [435833, 8376425, 34857265, 3462946, 8974526, 87625496, 76235986, 136725897, 39685235, 51699263]
    bins = [100, 200, 300, 400]
    if(make_correct_hists == True):
        for j in range(1, len(bins)):
            seed_default = '34086709' #this is the seed it was originally created with
            hist = 'hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16_bins' + str(bins[j])
            nbody_custom_lua(args, l, hist, hist, v, seed_default, str(bins[j]))
    
    if(make_compare_hists == True):
        for j in range(0, len(bins)):
            for i in range(0, len(seed)):
                hist = 'seed_test/seed' + str(seed[i]) + '_bins' + str(bins[j])  
                nbody_custom_lua(args, l, hist, hist, v, str(seed[i]), str(bins[j]))
                match_hists(histogram_mw_1d_v160, hist, v )
                
    if(compare_only == True):
        for j in range(0, len(bins)):
            for i in range(0, len(seed)):
                hist_correct = 'hist_v160_ft3p95_rt0p98_rl0p2_rd0p8_ml12_md48p0__4_14_16_bins' + str(bins[j])
                hist = 'seed_test/seed' + str(seed[i]) + '_bins' + str(bins[j])  
                match_hists(hist_correct, hist, v )
     
    if(parse == True):
        g = open('stderr.txt', 'r')
        f = open('seed_fluc_data.txt', 'w')
        for line in g:
            if (line.startswith("<search_likelihood>")):
                ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
                tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
                f.write("%s \n" % tt[0])#writes the first of the resplit lines
                
                
    if(plot == True):
        g = open('seed_fluc_data.txt', 'r')
        counter = 1
        data_lines = len(seed) * len(bins)
        section_size = len(seed)
        sections = data_lines / section_size
        #print(sections)
        section_number = 0
        temp_list = []
        data = []
        for line in g:
            if(counter < section_size + 1):#saves all the data in sections of how long 
                temp_list.append(float(line))
                counter += 1
            if(counter > section_size):
                counter = 1
                data.append(temp_list[:])
                #print data
                temp_list = []
                section_number += 1
        #print data[0]
        
        ylimit = -50
        plt.title('Histogram of Light Matter Distribution After 4 Gy')
        plt.xlim((0, 10))
        plt.ylim((ylimit, 0))
        labels = []
        plt.ylabel('likelihood')
        for i in range(0, len(bins)):
            labels.append(str(bins[i]))
        for i in range(0, sections):
            plt.plot(data[i], alpha=1, label = labels[i])
            
        plt.legend()
        plt.savefig('quick_plots/seed_fluctuations.png', format='png')
        plt.show()        
# # # # # # # # # # # # # # # # # # # # # #
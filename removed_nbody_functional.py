    def run_from_checkpoint(self, parameters, simulation_hist, output):#runs a sim using some provided checkpoint file
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody from checkpoint')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + self.version + " \
            -f " + path + "lua/" + self.lua_file + " \
            -z " + path + "quick_plots/hists/" + simulation_hist + ".hist \
            -o " + path + "quick_plots/outputs/" + output + ".out \
            -n 10 -b  -P --no-clean-checkpoint --checkpoint=CHECKPOINT_NAME " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr)
        
        
    
    def run_and_compare_from_checkpoint(self, parameters, comparison_hist, simulation_hist, output):
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody 2')
        os.system(" " + self.path + "nbody_test/bin/milkyway_nbody_1.66_x86_64-pc-linux-gnu__mt" + self.version + " \
            -f " + self.path + "lua/" + lua_file + " \
            -h " + self.path + "quick_plots/hists/" + comparison_hist + ".hist \
            -z " + self.path + "quick_plots/hists/" + simulation_hist + ".hist \
            -o " + self.path + "quick_plots/outputs/" + output + ".out \
            -n 10 -b -P -i --no-clean-checkpoint --checkpoint=CHECKPOINT_NAME " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr )

     
                os.system("./milkyway_nbody" + self.version + " \
            -f " + self.path + "lua/" + self.lua_file + " \
            -z " + self.path + "quick_plots/hists/" + simulation_hist + ".hist \
            -o " + self.path + "quick_plots/outputs/" + simulation_hist + ".out \
            -n 10 -b -u -i 100.0 ~/Desktop/research/test2.out" )
                
                
                
                
        if(plot_orbit):
            orb = nbody_outputs(path + 'reverse_orbit.out')
            orb.rescale_l()
            orb.dark_light_split()
            
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb.ls, orb.bs, '.', markersize = .15, color = 'g', alpha=1.0, marker = '.')
            #plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            
            
            orb = nbody_outputs(path + 'forward_orbit.out')
            orb.rescale_l()
            orb.dark_light_split()
                
            plt.xlim((xlower, xupper))
            plt.ylim((ylower, yupper))
            plt.xlabel('l')
            plt.ylabel('b')
            plt.title('l vs b')
            plt.plot(orb.ls, orb.bs, '.', markersize = .15, color = 'r', alpha=1.0, marker = '.')
            plt.savefig('/home/sidd/Desktop/research/quick_plots/tidal_stream_lbr_allmatter_orbit', format='png')
            plt.show()

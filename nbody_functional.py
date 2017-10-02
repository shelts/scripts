import os
import subprocess
from subprocess import call


class nbody_outputs:#a class that takes in data from nbody output files and makes them available
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_data()
        
    def get_data(self):
        self.xs = []; self.ys = []; self.zs = []
        self.ls = []; self.bs = []; self.rs = []
        self.vxs = []; self.vys = []; self.vzs = []
        self.vls = []; self.ms = []; self.tps = []
        
        f = open(self.file_name, 'r')
        read_data = False
        
        for line in f:
            if (line.startswith("# ignore")):
                read_data = True
                continue
            if(line.startswith("</bodies>")):
                break
            if(read_data):
                ss = line.split(', ')
                ty = int(ss[0])
                x = float(ss[1])
                y = float(ss[2])
                z = float(ss[3])
                
                l = float(ss[4])
                b = float(ss[5])
                r = float(ss[6])
                
                vx = float(ss[7])
                vy = float(ss[8])
                vz = float(ss[9])
                
                m  = float(ss[10])
                vl = float(ss[11])
                self.xs.append(x); self.ys.append(y); self.zs.append(z)
                self.ls.append(l); self.bs.append(b); self.rs.append(r)
                self.vxs.append(vx); self.vys.append(vy); self.vzs.append(vz)
                self.tps.append(ty); self.ms.append(m); self.vls.append(vl)
            
        f.close()
        
    def dark_light_split(self):#splits the data between light and dark
        self.light_x , self.light_y , self.light_z    = ([] for i in range(3))
        self.light_l , self.light_b , self.light_r    = ([] for i in range(3))
        self.light_vx , self.light_vy , self.light_vz = ([] for i in range(3))
        self.light_vl, self.light_m                   = ([] for i in range(2))
        
        self.dark_x , self.dark_y , self.dark_z       = ([] for i in range(3))
        self.dark_l , self.dark_b , self.dark_r       = ([] for i in range(3))
        self.dark_vx , self.dark_vy , self.dark_vz    = ([] for i in range(3))
        self.dark_vl, self.dark_m                     = ([] for i in range(2))
        
        for i in range(0, len(self.xs)):
            if(self.tps[i] == 0):
                self.light_x.append(self.xs[i])
                self.light_y.append(self.ys[i])
                self.light_z.append(self.zs[i])
                
                self.light_l.append(self.ls[i])
                self.light_b.append(self.bs[i])
                self.light_r.append(self.rs[i])
                
                self.light_vx.append(self.vxs[i])
                self.light_vy.append(self.vys[i])
                self.light_vz.append(self.vzs[i])
                
                self.light_vl.append(self.vls[i])
                self.light_m.append(self.ms[i])
                
            if(self.tps[i] == 1):
                self.dark_x.append(self.xs[i])
                self.dark_y.append(self.ys[i])
                self.dark_z.append(self.zs[i])
                
                self.dark_l.append(self.ls[i])
                self.dark_b.append(self.bs[i])
                self.dark_r.append(self.rs[i])
                
                self.dark_vx.append(self.vxs[i])
                self.dark_vy.append(self.vys[i])
                self.dark_vz.append(self.vzs[i])
                
                self.dark_vl.append(self.vls[i])
                self.dark_m.append(self.ms[i])    
                
    def rescale_l(self):#to change l range from [0:360] to [-180:180]
        for i in range(0, len(self.ls)):
            if(self.ls[i] > 180.0):
                self.ls[i] = self.ls[i] - 360.0
    
    def convert_lambda_beta(self, split):#to convert l,b to lambda, beta
        if(split):#if the data was split between light and dark
            self.light_lambda = []; self.light_beta = []
            self.dark_lambda  = []; self.dark_beta = []
        else:
            self.betas   = []
            self.lambdas = []
        
        for i in range(0, len(self.ls)):
            lmbda_tmp, beta_tmp = self.convert_to_Lambda_Beta(self.ls[i], self.bs[i], self.rs[i], False)
            if(split):
                if(self.tps[i] == 0):
                    self.light_lambda.append(lmbda_tmp)
                    self.light_beta.append(beta_tmp)
                    
                if(self.tps[i] == 1):
                    self.dark_lambda.append(lmbda_tmp)
                    self.dark_beta.append(beta_tmp)
            else:
                self.lambdas.append(lmbda_tmp)
                self.betas.append(beta_tmp)
            
        
        
    def convert_to_Lambda_Beta(self, x1, x2, x3, cartesian):#can convert l,b or x,y,z to lambda beta
        phi   = mt.radians(128.79)
        theta = mt.radians(54.39)
        psi   = mt.radians(90.70)
        
        if(cartesian):
            x_coor = x1
            y_coor = x2
            z_coor = x3
            x_coor += 8.0 #convert to solar centric
        else:
            l = mt.radians(x1)
            b = mt.radians(x2)
            r = x3
            
            x_coor = r * mt.cos(l) * mt.cos(b) #this is solar centered x
            y_coor = r * mt.sin(l) * mt.cos(b)
            z_coor = r * mt.sin(b)
        
        #A = MB
        B = [x_coor, y_coor, z_coor]
        M_row1 = [mt.cos(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.sin(psi),
                mt.cos(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.sin(psi),
                mt.sin(psi) * mt.sin(theta)]
        
        M_row2 = [-mt.sin(psi) * mt.cos(phi) - mt.cos(theta) * mt.sin(phi) * mt.cos(psi),
                -mt.sin(psi) * mt.sin(phi) + mt.cos(theta) * mt.cos(phi) * mt.cos(psi),
                mt.cos(psi) * mt.sin(theta)]
        
        M_row3 = [mt.sin(theta) * mt.sin(phi), 
                -mt.sin(theta) * mt.cos(phi),
                mt.cos(theta)]
        
        A1 = M_row1[0] * B[0] + M_row1[1] * B[1] + M_row1[2] * B[2]
        A2 = M_row2[0] * B[0] + M_row2[1] * B[1] + M_row2[2] * B[2]
        A3 = M_row3[0] * B[0] + M_row3[1] * B[1] + M_row3[2] * B[2]
        
        beta = mt.asin(-A3 / mt.sqrt(A1 * A1 + A2 * A2 + A3 * A3))
        lamb = mt.atan2(A2, A1)
        
        beta = mt.degrees(beta)
        lamb = mt.degrees(lamb)
        
        return lamb, beta
    
    
    def binner_vlos(self, angle_cuttoffs):
        self.binned_vlos = []
        self.which_bin   = []
        
        bin_size = abs(angle_cuttoffs[0] - angle_cuttoffs[1]) / angle_cuttoffs[2]
        mid_bins = []
        which_lambda = []
        which_beta = []
        #setting up the mid bin coordinates
        for i in range(0, angle_cuttoffs[2]):
            mid_bin = angle_cuttoffs[0] + i * bin_size + bin_size / 2.0
            mid_bins.append(mid_bin)
            
        #transform to lambda beta coordinates from lbr
        self.convert_lambda_beta(False)
        
        for i in range(0, len(self.lambdas)):#go through the different lambda coordinates
            if(self.betas[i] >= angle_cuttoffs[3] and self.betas[i] <= angle_cuttoffs[4]):#if it is between the beta cuttoffs
                for j in range(0, len(mid_bins)):#go through the bin coordinates
                    left_edge  = mid_bins[j] - bin_size / 2.0 #edges of the bin
                    right_edge = mid_bins[j] + bin_size / 2.0 #edges of the bin
                    
                    if(self.lambdas[i] >= left_edge and self.lambdas[i] <= right_edge):#check if the lambda coor falls in the bin
                        self.which_bin.append(mid_bins[j])#which mid bin it should be 
                        self.binned_vlos.append(self.vls[i])#the line of sight vel
                        
                        which_lambda.append(self.lambdas[i])#the coordinate that was put there
                        which_beta.append(self.betas[i])
                        break 

class nbody_histograms:#a class that takes in data from nbody histogram files and makes them available
    def __init__(self, file_name):
        self.file_name = file_name
        self.get_data()
        
    def get_data(self):
        self.lbins = []; self.counts = []; self.count_err = []; self.vd = []; self.vd_error = []
        read_data = False

        lines = open(self.file_name, 'r')
        for line in lines:
            if (line.startswith("betaBins")):
                read_data = True
                continue
            if(line.startswith("</histogram>")):
                break
            
            if(read_data):
                if(line.startswith("\n")):
                    continue
                else:
                    ss = line.split(' ')
                    self.lbins.append(    float(ss[1]))
                    self.counts.append(   float(ss[3]))
                    self.count_err.append(float(ss[4]))
                    self.vd.append(       float(ss[5]))
                    self.vd_error.append( float(ss[6]))
                    
        lines.close()
        
        
        
class nbody_running_env:
    def __init__(self, lua_file, version, path):
        self.lua_file      = lua_file
        self.version       = version
        self.path          = path
    
    def build(self):
        os.chdir("./")
        #-DCMAKE_C_COMPILER=/usr/bin/cc 
        os.system("rm -r nbody_test")
        os.system("mkdir nbody_test")
        os.chdir("nbody_test")
        os.system("cmake -DCMAKE_BUILD_TYPE=Release -DBOINC_RELEASE_NAMES=OFF -DNBODY_GL=OFF -DNBODY_STATIC=ON -DBOINC_APPLICATION=ON -DSEPARATION=OFF -DNBODY_OPENMP=ON    " + self.path + "milkywayathome_client/")
        os.system("make  ")
        os.chdir("../")
    
    
    def single_run(self, parameters, simulation_hist):
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody from checkpoint')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + self.version + " \
            -f " + self.path + "lua/" + self.lua_file + " \
            -z " + self.path + "quick_plots/hists/" + simulation_hist + ".hist \
            -o " + self.path + "quick_plots/outputs/" + simulation_hist + ".out \
            -n 10 -b -P  -i " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr)
        
    
    def run_and_compare(self, parameters, correctans_hist, comparison_hist):
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody 2')
        os.system(" " + self.path + "nbody_test/bin/milkyway_nbody_1.66_x86_64-pc-linux-gnu__mt" + self.version + " \
            -f " + self.path + "lua/" + lua_file + " \
            -h " + self.path + "quick_plots/hists/" + correctans_hist + ".hist \
            -z " + self.path + "quick_plots/hists/" + comparison_hist + ".hist \
            -o " + self.path + "quick_plots/outputs/" + comparison_hist + ".out \
            -n 10 -b -P -i  " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr )
        
        
    def match_hists(self, hist1, hist2):
        print "matching histograms: "
        #using call here instead so the format of using it is on record
        call([" " + self.path + "nbody_test/bin/milkyway_nbody" + self.version  
            + " -h " + self.path + "quick_plots/hists/" + hist1 + '.hist'
            + " -S " + self.path + "quick_plots/hists/" + hist2 + '.hist'], shell=True)
        print hist1, "\n", hist2
        print "\n"
        return 0
    
    
    
    def match_hists_pipe_output(hist1, hist2, pipe_name):
        print "matching histograms: "
        #using call here instead so the format of using it is on record
        call([" " + self.path + "nbody_test/bin/milkyway_nbody" + self.version  
            + " -h " + self.path + "" + hist1 + '.hist'
            + " -S " + self.path + "" + hist2 + '.hist' + " 2>>" + pipe_name], shell=True)
        print hist1, "\n", hist2
        print "\n"
        return 0
    

    def single_piping_output(self, parameters, simulation_hist, output):
        ft    = str(parameters[0])
        bt    = str(parameters[1])
        rl    = str(parameters[2])
        rr    = str(parameters[3])
        ml    = str(parameters[4])
        mr    = str(parameters[5])
        print('running nbody. piping output to file')
        os.chdir("nbody_test/bin/")
        os.system("./milkyway_nbody" + self.version + " \
            -f " + self.path + "lua/" + self.lua_file + " \
            -z " + self.path + "quick_plots/hists/" + simulation_hist + ".hist \
            -o " + self.path + "quick_plots/outputs/" + output + ".out \
            -n 12 -b -P  -i " + (ft) + " " + bt + " " + rl + " " + rr + " " + ml + " " + mr + " \
        2>> " + out + "_piped.out")
        
        
    def run_from_checkpoint(self, parameters, simulation_hist, output):
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

     
        
        #os.chdir("../")
    # #     




        
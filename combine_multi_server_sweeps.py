#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os

oneD_names   = ['ft', 'bt', 'r', 'rr', 'm', 'mr']
sweep_name = "parameter_sweeps_rand_iter/"


file_made  = [False, False, False, False, False, False]

lmc  = (os.path.exists("lmc"))
tel  = (os.path.exists("tel"))
fort = (os.path.exists("fortran"))

dirs = [lmc, tel, fort]
server_name = ["lmc", "tel", "fortran"]



def concat(new_file, old_file):
        tmp = open('tmp.txt', 'w')#opening a tmp file to copy the new and old stuff into
        new = open(new_file, 'r')#this is the file from the new server, not yet copied
        old = open(old_file, 'r')#file that was already copied over 
        
        for line in old:
            tmp.write(line)#write the old file into the tmp file

        for line in new:
            tmp.write(line)#write the new file into the tmp file
            
        tmp.close()#closing
        new.close()
        old.close()
        
        os.system("mv tmp.txt " + old_file)#replace the old file with the tmp








def main():
    for server in range(0, len(server_name)):#for each of the servers
        if(dirs[server]):#if the directory for that server exists
            for i in range(0, len(oneD_names)):#go over each of the different sweeps
                data_file_name = server_name[server] + "/" + sweep_name + oneD_names[i] + ".txt" #name of the likelihood files
                vals_file_name = server_name[server] + "/" + sweep_name + oneD_names[i] + "_vals.txt"#name of the parameter values
                
                if(os.path.exists(data_file_name) and (file_made[i] == False)): #if the file exists and has not yet been copied from a different server
                    os.system("cp " + data_file_name + " ./" + sweep_name)#copy data over
                    os.system("cp " + vals_file_name + " ./" + sweep_name)#copy values over
                    file_made[i] = True #mark that there has been a version copied over already.
                
                elif(os.path.exists(data_file_name) and file_made[i]): #check if the file exists and if a version from a different server was copied already
                    print "already cped. concating" #if there is a version from another server, concat the one from this server to the end of the existing one
                    concat(data_file_name, "./" + sweep_name + oneD_names[i] + ".txt")#the new server file and the file that was copied already
                    concat(vals_file_name, "./" + sweep_name + oneD_names[i] + "_vals.txt")
            print file_made
            
main()
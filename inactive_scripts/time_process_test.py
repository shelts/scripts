#! /usr/bin/python
import os
import time
from subprocess import call
import sys



start = time.time()
i = 10
os.chdir("/boinc/milkyway/bin" )
while(1):
    end = time.time()
    if(end - start == 5):
        s = "r_vs_rr_" + str(i) + ".txt"
        print s
        os.system("./tao_search_status --app milkyway_nbody --search_name ps_nbody_2_10_16_parametersweep_1_v154 --print_best 999 >~/data2_r_vs_rr/" + s)
        start = time.time()
        end   = start
        i = i + 1
        
    if(i > 15):
        break


#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import subprocess
from subprocess import call
import math as mt
from nbody_functional import *


def half_mass_radius():

    #found
    paras = [3.93649841565613, 1, 0.208372119674464, 0.235151860862976, 12.0055674149201, 0.306476628533526]

    rl_f = paras[2]
    rr_f = paras[3]
    ml_f = paras[4]
    mr_f = paras[5]
    
    rd_f = (rl_f / rr_f) * (1.0 - rr_f)
    md_f = (ml_f / mr_f) * (1.0 - mr_f)
    
    print "found rd, md:\t", rd_f, md_f
    
    #correct
    ml_c = 12.0
    rl_c = 0.2
    rr_c = 0.2
    mr_c = 0.2
    rd_c = (rl_c / rr_c) * (1.0 - rr_c)
    md_c = (ml_c / mr_c) * (1.0 - mr_c)
    print "correct rd, md:\t", rd_c, md_c
    
    cut = .5 * ml_c
    
    r = 0.001
    #calculates the density of the dm within the half mass radius of the correct baryon component
    while(1):
        m_enc_l   = ml_c * r**3.0 / (r * r + rl_c * rl_c )**(3.0 / 2.0)
        
        m_enc_d_c = md_c * r**3.0 / (r * r + rd_c * rd_c )**(3.0 / 2.0)
        m_enc_d_f = md_f * r**3.0 / (r * r + rd_f * rd_f )**(3.0 / 2.0)
        
        
        plummer_den_d_c = (3.0 / (4.0 * mt.pi * rd_c**3.0)) * md_c / (1.0 + (r * r)/ (rd_c * rd_c))**(5.0 / 2.0)
        plummer_den_d_f = (3.0 / (4.0 * mt.pi * rd_f**3.0)) * md_f / (1.0 + (r * r)/ (rd_f * rd_f))**(5.0 / 2.0)
        
        if(m_enc_l >= cut):
            break
        else:
            r += 0.001

    print 'plum den correct, found:\t', plummer_den_d_c, plummer_den_d_f   #density of DM within correct baryon extent     
    print 'DM enc correct, DM enc found :\t', m_enc_d_c, m_enc_d_f
    
    print 'BM enc, r:\t', m_enc_l, r
    
    
    r = 0.001
    #calculates the density of the dm within the half mass radius of the correct baryon component
    cut = 0.5 * ml_f
    while(1):
        m_enc_l = ml_f * r**3.0 / (r * r + rl_f * rl_f )**(3.0 / 2.0)
        
        m_enc_d_c = md_c * r**3.0 / (r * r + rd_c * rd_c )**(3.0 / 2.0)
        m_enc_d_f = md_f * r**3.0 / (r * r + rd_f * rd_f )**(3.0 / 2.0)
        
        
        plummer_den_d_c = (3.0 / (4.0 * mt.pi * rd_c**3.0)) * md_c / (1.0 + (r * r)/ (rd_c * rd_c))**(5.0 / 2.0)
        plummer_den_d_f = (3.0 / (4.0 * mt.pi * rd_f**3.0)) * md_f / (1.0 + (r * r)/ (rd_f * rd_f))**(5.0 / 2.0)
        if(m_enc_l >= cut):
            break
        else:
            r += 0.001

    print 'plum den correct, found:\t', plummer_den_d_c, plummer_den_d_f   #density of DM within correct baryon extent     
    print 'DM enc correct, DM enc found :\t', m_enc_d_c, m_enc_d_f
    
    print 'BM enc, r:\t', m_enc_l, r
    
    
    
    #rr_c = 0.2
    #rd_c = (rl_c / rr_c) * (1.0 - rr_c)
    #m_enc_d_c = md_c * r**3.0 / (r * r + rd_c * rd_c )**(3.0 / 2.0)
    
    if(False): #determines an combination of parameters which have constant mass within half light radius
        f = open('cons_den.txt', 'w')
        
        threshold = 0.2
        mr = 0.05
        while(1):
            rr = 0.05
            while(1):
                rd_f = (rl_c / rr) * (1.0 - rr)
                md_f = (ml_c / mr) * (1.0 - mr)
                #mdenc = (3.0 / (4.0 * mt.pi * rd_f**3.0)) * md_f / (1.0 + (r * r)/ (rd_f * rd_f))**(5.0 / 2.0)
                mdenc = md_f * r**3.0 / (r * r + rd_f * rd_f )**(3.0 / 2.0)
                #print mdenc, m_enc_d_c
                if(mdenc > (m_enc_d_c - threshold) and mdenc < (m_enc_d_c + threshold) ):
                    f.write("%0.15f\t%0.15f\t%0.15f\n" % (rr, mr, mdenc))
                
                if(rr > 0.5):
                    break
                else:
                    rr += 0.001
            if(mr > 0.95):
                break
            else:
                mr += 0.001
        f.close()
    #print m_enc_d_c

# #      
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
                #/# # # # # # # # # # # # # # \#
                #          Generator           #
                #\# # # # # # # # # # # # # # /#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
def main():
        
    half_mass_radius()
        
# spark plug #
main()

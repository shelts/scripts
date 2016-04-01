#! /usr/bin/python
import os
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
#parameter = [start, end, increment]
ft         = [0.25, 3.0, 0.05]
bt         = [0.25, 2.0, 0.05]
r          = [0.1, 1.0, 0.05]
r_r        = [0.1, 0.75, 0.05]
m          = [2.0, 50.0, 1.0]
m_r        = [0.1, 0.75, 0.05]
#--------------------------------------------------------------------------------------------------

#  FORWARD TIME VS BACKTIME #
f = open('./parameter_data/ft_vs_bt.txt', 'w')
fwt_counter = ft[0]
fwt = str(fwt_counter)
while fwt_counter < ft[1]:
    bwt_counter = bt[0]
    bwt = str(bwt_counter)
    while bwt_counter < bt[1]:
        f.write("%s \t %s \n" % (fwt_counter, bwt_counter))
        bwt_counter = bwt_counter + bt[2]
        bwt = str(bwt_counter)
    fwt_counter = fwt_counter + ft[2]
    fwt = str(fwt_counter)
f.close()
  
#  FORWARD TIME VS RAD #
f = open('./parameter_data/ft_vs_rad.txt', 'w')
fwt_counter = ft[0]
fwt = str(fwt_counter)
while fwt_counter < ft[1]:
    rad_counter = r[0]
    rad = str(rad_counter)
    while rad_counter < r[1]:
        f.write("%s \t %s \n" % (fwt_counter, rad_counter))
        rad_counter = rad_counter + r[2]
        rad = str(rad_counter)
    fwt_counter = fwt_counter + ft[2]
    fwt = str(fwt_counter)
f.close()


#  FORWARD TIME VS RAD RATIO #
f = open('./parameter_data/ft_vs_rr.txt', 'w')
fwt_counter = ft[0]
fwt = str(fwt_counter)
while fwt_counter < ft[1]:
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        f.write("%s \t %s \n" % (fwt_counter, rr_counter))
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
    fwt_counter = fwt_counter + ft[2]
    fwt = str(fwt_counter)
f.close()

#  FORWARD TIME VS MASS #
f = open('./parameter_data/ft_vs_m.txt', 'w')
fwt_counter = ft[0]
fwt = str(fwt_counter)
while fwt_counter < ft[1]:
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        f.write("%s \t %s \n" % (fwt_counter, m_counter))
        m_counter = m_counter + m[2]
        ms = str(m_counter) 
    fwt_counter = fwt_counter + ft[2]
    fwt = str(fwt_counter)
f.close()   
    
#  FORWARD TIME VS MASS RATIO #
f = open('./parameter_data/ft_vs_mr.txt', 'w')
fwt_counter = ft[0]
fwt = str(fwt_counter)
while fwt_counter < ft[1]:
    mr_counter = m_r[0]
    mr = str(mr_counter)
    while mr_counter < m_r[1]:
        f.write("%s \t %s \n" % (fwt_counter, mr_counter))
        mr_counter = mr_counter + m_r[2]
        mr = str(mr_counter) 
    fwt_counter = fwt_counter + ft[2]
    fwt = str(fwt_counter)
f.close()    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  BACKWARD TIME VS RAD #
f = open('./parameter_data/bt_vs_r.txt', 'w')
bwt_counter = bt[0]
bwt = str(bwt_counter)
while bwt_counter < bt[1]:
    rad_counter = r[0]
    rad = str(rad_counter)
    while rad_counter < r[1]:
        f.write("%s \t %s \n" % (bwt_counter, rad_counter))
        rad_counter = rad_counter + r[2]
        rad = str(rad_counter)
    bwt_counter = bwt_counter + bt[2]
    bwt = str(bwt_counter)
f.close()

#  BACKWARD TIME VS RAD RATIO #
f = open('./parameter_data/bt_vs_rr.txt', 'w')
bwt_counter = bt[0]
bwt = str(bwt_counter)
while bwt_counter < bt[1]:
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        f.write("%s \t %s \n" % (bwt_counter, rr_counter))
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
    bwt_counter = bwt_counter + bt[2]
    bwt = str(bwt_counter)
f.close()

#  BACKWARD TIME VS MASS #
f = open('./parameter_data/bt_vs_m.txt', 'w')
bwt_counter = bt[0]
bwt = str(bwt_counter)
while bwt_counter < bt[1]:
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        f.write("%s \t %s \n" % (bwt_counter, m_counter))
        m_counter = m_counter + m[2]
        ms = str(m_counter) 
    bwt_counter = bwt_counter + bt[2]
    bwt = str(bwt_counter) 
f.close()

#  BACKWARDS TIME VS MASS RATIO #
f = open('./parameter_data/bt_vs_mr.txt', 'w')
bwt_counter = bt[0]
bwt = str(bwt_counter)
while bwt_counter < bt[1]:
    mr_counter = m_r[0]
    mr = str(mr_counter)
    while mr_counter < m_r[1]:
        f.write("%s \t %s \n" % (bwt_counter, mr_counter))
        mr_counter = mr_counter + m_r[2]
        mr = str(mr_counter) 
    bwt_counter = bwt_counter + bt[2]
    bwt = str(bwt_counter)
f.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  RAD VS RAD RATIO #
f = open('./parameter_data/r_vs_rr.txt', 'w')
r_counter = r[0]
rad = str(r_counter)
while r_counter < r[1]:
    rr_counter = r_r[0]
    rr = str(rr_counter)
    while rr_counter < r_r[1]:
        f.write("%s \t %s \n" % (r_counter, rr_counter))
        rr_counter = rr_counter + r_r[2]
        rr = str(rr_counter)
    r_counter = r_counter + r[2]
    rad = str(r_counter)
f.close()

#  RAD VS MASS #
f = open('./parameter_data/r_vs_m.txt', 'w')
r_counter = r[0]
rad = str(r_counter)
while r_counter < r[1]:
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        f.write("%s \t %s \n" % (r_counter, m_counter))
        m_counter = m_counter + m[2]
        ms = str(m_counter) 
    r_counter = r_counter + r[2]
    rad = str(r_counter)
f.close()

#  RAD VS MASS RATIO #
f = open('./parameter_data/r_vs_mr.txt', 'w')
r_counter = r[0]
rad = str(r_counter)
while r_counter < r[1]:
    mr_counter = m_r[0]
    mr = str(mr_counter)
    while mr_counter < m_r[1]:
        f.write("%s \t %s \n" % (r_counter, mr_counter))
        mr_counter = mr_counter + m_r[2]
        mr = str(mr_counter) 
    r_counter = r_counter + r[2]
    rad = str(r_counter)
f.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  RAD RATIO VS MASS #
f = open('./parameter_data/rr_vs_m.txt', 'w')
rr_counter = r_r[0]
rr = str(rr_counter)
while rr_counter < r_r[1]:
    m_counter = m[0]
    ms = str(m_counter)
    while m_counter < m[1]:
        f.write("%s \t %s \n" % (rr_counter, m_counter))
        m_counter = m_counter + m[2]
        ms = str(m_counter) 
    rr_counter = rr_counter + r_r[2]
    rr = str(rr_counter)
f.close()

#  RAD RATIO VS MASS RATIO #
f = open('./parameter_data/rr_vs_mr.txt', 'w')
rr_counter = r_r[0]
rr = str(rr_counter)
while rr_counter < r_r[1]:
    mr_counter = m_r[0]
    mr = str(mr_counter)
    while mr_counter < m_r[1]:
        f.write("%s \t %s \n" % (rr_counter, mr_counter))
        mr_counter = mr_counter + m_r[2]
        mr = str(mr_counter) 
    rr_counter = rr_counter + r_r[2]
    rr = str(rr_counter)
f.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  MASS VS MASS RATIO #
f = open('./parameter_data/m_vs_mr.txt', 'w')
m_counter = m[0]
ms = str(m_counter)
while m_counter < m[1]:
    mr_counter = m_r[0]
    mr = str(mr_counter)
    while mr_counter < m_r[1]:
        f.write("%s \t %s \n" % (m_counter, mr_counter))
        mr_counter = mr_counter + m_r[2]
        mr = str(mr_counter) 
    m_counter = m_counter + m[2]
    ms = str(m_counter)
f.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



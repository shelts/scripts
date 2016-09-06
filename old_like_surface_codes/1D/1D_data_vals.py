#! /usr/bin/python
import os
#--------------------------------------------------------------------------------------------------
#       PARAMETER LIBRARY       #
#--------------------------------------------------------------------------------------------------
#parameter    = [start, end, increment]
ft         = [3.9, 4.2, 0.01]#
bt         = [0.96, 1.08, 0.005]#
r          = [0.1, 0.8, 0.01]#
r_r        = [0.1, 0.8, 0.01]#
m          = [1.0, 20.0, 0.25]#
m_r        = [0.17, 0.24, 0.001]#

c = [4, 1, 0.2, 0.25, 60, 0.2]
#--------------------------------------------------------------------------------------------------


#  FORWARD TIME #
f = open('./parameter_data/ft_vals.txt', 'w')
counter = ft[0]
while counter < ft[1]:
    f.write("%s \n" % counter)
    counter = counter + ft[2]
f.close()
  
#  BACKWARD TIME  #  
f = open('./parameter_data/bt_vals.txt', 'w')
counter = bt[0]
while counter < bt[1]:
    f.write("%s \n" % counter)
    counter = counter + bt[2]
f.close() 

#  RADIUS  #
f = open('./parameter_data/rad_vals.txt', 'w')
counter = r[0]
while counter < r[1]:
    f.write("%s \n" % counter)
    counter = counter + r[2]
f.close()
 
 #  RADIUS RATIO  #
f = open('./parameter_data/rr_vals.txt', 'w')
counter = r_r[0]
while counter < r_r[1]:
    f.write("%s \n" % counter)
    counter = counter + r_r[2]
f.close()

#  MASS  #
f = open('./parameter_data/mass_vals.txt', 'w')
counter = m[0]
while counter < m[1]:
    f.write("%s \n" % counter)
    counter = counter + m[2]
f.close()

#  MASS RATIO  #
f = open('./parameter_data/mr_vals.txt', 'w')
counter = m_r[0]
while counter < m_r[1]:
    f.write("%s \n" % counter)
    counter = counter + m_r[2]
f.close()

#    Correct Answers     #
f = open('./parameter_data/correct.txt', 'w')
for i in range(0,50):
    f.write("%f \t %f \t %f \t %f \t %f \t %f \t %f\n" % (-i, c[0], c[1], c[2], c[3], c[4], c[5]))
    
    
#--------------------------------------------------------------------------------------------------

#def oneD_data_vals():
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[0] + '_vals.txt', 'w')

    ##  FORWARD TIME #
    #counter = ft[0]
    #while counter < ft[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[0] and counter + ft[2] > c[0]):
            #f.write("%s \n" % c[0])
        #counter += ft[2]
    #f.close()
    
    ##  BACKWARD TIME  #  
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[1] + '_vals.txt', 'w')
    #counter = bt[0]
    #while counter < bt[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[1] and counter + bt[2] > c[1]):
            #f.write("%s \n" % c[1])
        #counter += bt[2]
    #f.close() 

    ##  RADIUS  #
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[2] + '_vals.txt', 'w')
    #counter = r[0]
    #while counter < r[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[2] and counter + r[2] > c[2]):
            #f.write("%s \n" % c[2])
        #counter += r[2]
    #f.close()
    
    ##  RADIUS RATIO  #
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[3] + '_vals.txt', 'w')
    #counter = r_r[0]
    #while counter < r_r[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[3] and counter + r_r[2] > c[3]):
            #f.write("%s \n" % c[3])
        #counter += r_r[2]
    #f.close()

    ##  MASS  #
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[4] + '_vals.txt', 'w')
    #counter = m[0]
    #while counter < m[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[4] and counter + m[2] > c[4]):
            #f.write("%s \n" % c[4])
        #counter += m[2]
    #f.close()

    ##  MASS RATIO  #
    #f = open('./1D_like_surface/parameter_data/' + oneD_names[5] + '_vals.txt', 'w')
    #counter = m_r[0]
    #while counter < m_r[1]:
        #f.write("%s \n" % counter)
        #if(counter < c[5] and counter + m_r[2] > c[5]):
            #f.write("%s \n" % c[5])
        #counter += m_r[2]
    #f.close()

    ##    Correct Answers     #
    #f = open('./1D_like_surface/parameter_data/correct.txt', 'w')
    #for i in range(0, 500):
        #f.write("%f \t %f \t %f \t %f \t %f \t %f \t %f\n" % (-i, c[0], c[1], c[2], c[3], c[4], c[5]))
    
    
#! /usr/bin/python
#/* Copyright (c) 2016 Siddhartha Shelton */
import os
import math as mt



#x1 = -13.583534393135377
#x2 = -5.698938916488823
#x3 = 1.872915545209894
#N = 3.

#ave = (x1 + x2 + x3)/N
#sigma = (x1 - ave )**2 + (x2 - ave )**2 + (x3 - ave )**2

#sigma *= 1./(N-1.)
#sigma = mt.sqrt(sigma)
##print sigma




#vsum = x1 + x2 + x3
#sqsum = x1**2. + x2**2. + x3**2.


#sigma2 = (sqsum/ (N-1.)) - ((N/(N-1.)) * (vsum/N)**2)



#bsum = -333.050590468065991
#bsqsum = 2769.804524377608686
#N = 93
#bsums = [-14.45944, -14.71392]
#bsqsums = [209.07541,216.49953]
#for i in range(0,len(bsums)):
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    ##print sigmasq
    #print mt.sqrt(sigmasq)
    #N -= 1.
    #bsum -= bsums[i]
    #bsqsum -= bsqsums[i]
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)

##print mt.sqrt(sigmasq) 
#sigmasq *= 1.111
#print '1', mt.sqrt(sigmasq)


#bsums = [-13.49586]
#bsqsums = [182.13822]
#for i in range(0,len(bsums)):
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    ##print sigmasq
    ##print mt.sqrt(sigmasq)
    #N -= 1.
    #bsum -= bsums[i]
    #bsqsum -= bsqsums[i]
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    
#sigmasq *= 1.111
#print '2', mt.sqrt(sigmasq)

#bsums = [-13.00600, -13.06441]
#bsqsums = [169.15593, 170.67871]
#for i in range(0,len(bsums)):
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    ##print sigmasq
    ##print mt.sqrt(sigmasq)
    #N -= 1.
    #bsum -= bsums[i]
    #bsqsum -= bsqsums[i]
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    
#sigmasq *= 1.111
#print '3', mt.sqrt(sigmasq)



#bsums = [-12.50976 ]
#bsqsums = [156.49420 ]
#for i in range(0,len(bsums)):
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    ##print sigmasq
    ##print mt.sqrt(sigmasq)
    #N -= 1.
    #bsum -= bsums[i]
    #bsqsum -= bsqsums[i]
    #sigmasq = (bsqsum/ (N-1.)) - ((N/(N-1.)) * (bsum/N)**2)
    
#sigmasq *= 1.111
#print '4', mt.sqrt(sigmasq)

    
#print mt.sqrt(sigmasq)




##sigmasq = 3.239263991718229
##N = 85
#err = (N+1.) / (N)
#err = err / (N-1.)
#err = mt.sqrt(err)
#err *= mt.sqrt(sigmasq)

#print  N, err


#vsum = 5247.812631100257022
#vsqsum = 667493.096225387183949
#N = 93
#vsums = [-142.08425, -147.79870, -146.69993]
#vsqsums = [20187.93533, 21844.45428, 21520.86847]

#for i in range(0, len(vsums)):
    #sigmasq = (vsqsum/ (N-1.)) - ((N/(N-1.)) * (vsum/N)**2)
    #print mt.sqrt(sigmasq)
    #N -= 1.
    #vsum -= vsums[i]
    #vsqsum -= vsqsums[i]
    #sigmasq = (vsqsum/ (N-1.)) - ((N/(N-1.)) * (vsum/N)**2)
    
#sigmasq *= 1.111
#print N,  mt.sqrt(sigmasq)


##vsum = 5247.812631100257022
##vsqsum = 667493.096225387183949
##N = 93
#vsums = [-80.76171]
#vsqsums = [6522.45410]

#for i in range(0, len(vsums)):
    #sigmasq = (vsqsum/ (N-1.)) - ((N/(N-1.)) * (vsum/N)**2)
    #print mt.sqrt(sigmasq)
    #N -= 1.
    #vsum -= vsums[i]
    #vsqsum -= vsqsums[i]
    #sigmasq = (vsqsum/ (N-1.)) - ((N/(N-1.)) * (vsum/N)**2)
    
#sigmasq *= 1.111
#print  N, mt.sqrt(sigmasq)

#betas1    = [7.256443469671583, 3.674912989179508, 6.969828569473862]
#betas2    = [7.111445743016753, 3.580265505599093, 6.998052013389252]

#betaerrs1 = [0.682576708910960, 0.166014959178720, 0.512417254887173]
#betaerrs2 = [0.671916295259007,0.162070327893450 ,0.510371185615074]

#vels1     = [49.875618659235229, 33.246342984720336, 84.198437548913461]
#vels2     = [55.288612310542732, 31.937102229560228, 85.249407583592443 ]

#velerr1   = [4.755071118134857, 1.491296295119528, 6.241018074036787]
#velerr2   = [5.271138296165012, 1.439829852907579, 6.250612035669136]

#n = 3
#beta_sigsq = 0
#vel_sigsq = 0
#for i in range(0, 3):
    #beta_sigsq += ( betas2[i] - betas1[i] )**2. / ( betaerrs1[i]**2. + betaerrs2[i]**2.)
    #vel_sigsq += ( vels2[i] - vels1[i] )**2. / ( velerr2[i]**2. + velerr1[i]**2.)

#print beta_sigsq, vel_sigsq

#c = (n/2.) - 1.
#p_beta = c * mt.log(beta_sigsq) - beta_sigsq /2.
#p_vel = c * mt.log(vel_sigsq) - vel_sigsq /2.

#print p_beta, p_vel

#mi = c * (mt.log(2. * c) - 1.)

#p_beta -= mi
#p_vel  -= mi

#print p_beta, p_vel










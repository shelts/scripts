#! /usr/bin/python
import os
#from subprocess import call

#old

rscale_l = 0.2
light_r_ratio = 0.25
rscale_d_old = rscale_l / light_r_ratio

#new
rscale_l = 0.2
light_r_ratio = 0.2
rscale_t = rscale_l / light_r_ratio
rscale_d = rscale_t *  (1.0 - light_r_ratio)



print rscale_d, rscale_d_old





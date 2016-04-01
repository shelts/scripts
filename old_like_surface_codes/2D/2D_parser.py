#! /usr/bin/python
import os

names   = [ 'ft_vs_bt', 'ft_vs_rad', 'ft_vs_rr', 'ft_vs_m', 'ft_vs_mr', 'bt_vs_r', 'bt_vs_rr', 'bt_vs_m', 'bt_vs_mr', 'r_vs_rr', 'r_vs_m', 'r_vs_mr', 'rr_vs_m', 'rr_vs_mr', 'm_vs_mr']
N  = 15
M  = 0

for i in range(M,N):
  g = open('./2d_parameter_sweeps/' + str(names[i]) + '.txt', 'r')
  f = open('./likelihood_data/' + str(names[i]) + '_data.txt', 'w')

  for line in g:
    if (line.startswith("<")):
      ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
      tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
      f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
  f.close()
  g.close()
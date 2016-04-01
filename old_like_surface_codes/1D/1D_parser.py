#! /usr/bin/python
import os

names   = ['ft', 'bt',  'rad', 'rr', 'mass', 'mr']


for i in range(0,6):
  g = open('./parameter_sweeps/' + str(names[i]) + '.txt', 'r')
  f = open('./likelihood_data/' + str(names[i]) + '_data.txt', 'w')

  for line in g:
    if (line.startswith("<")):
      ss = line.split('<search_likelihood>')#splits the line between the two sides the delimiter
      tt = ss[1].split('</search_likelihood>')#chooses the second of the split parts and resplits
      f.write("%s \n" % tt[0])#writes the first of the resplit lines
    
  f.close()
  g.close()



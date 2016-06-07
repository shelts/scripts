#! /usr/bin/python
import os
from subprocess import call
import matplotlib.pyplot as plt
import math







file1 = '../1.txt'
file2 = '../2.txt'

lines1 = []
lines2 = []

lines1 = open(file1).readlines();

lines2 = open(file2).readlines();

i = 0
diff = 0.0
for line in lines1:

    if(line != lines2[i]):
        diff += 1.0
        print("found difference in line %i\n" % (i + 1))
    i += 1
    
print("we found %f differences!\n" % (diff))
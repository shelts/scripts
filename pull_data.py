#! /usr/bin/python
import os
import time
from subprocess import call
import sys
import pxssh

s = pxssh.pxssh()
#hostname = ('fornax.phys.rpi.edu')
hostname = ('milkyway.cs.rpi.edu')
username = ('shelts')



start = time.time()
i = 1
while(1):
    end = time.time()
    if(end - start == 36000):
        name = "" + str(i) + ".txt"
        if not s.login(hostname, username):
            print "SSH session failed on login."
        else:
            print "SSH session login successful"
            s.sendline ('./pull_sweep_data.py ' + name)
            s.prompt()         # match the prompt
            print s.before  
            s.logout()
            s = pxssh.pxssh()
        start = time.time()
        end   = start
        i = i + 1
        



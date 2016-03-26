#! /usr/bin/python
import os
from subprocess import call
import sys
args = sys.argv;

def __main__(arg):
    s = str( args[1] )
    d = "email.dat"
    
    #os.system("mhonarc -single " + d + " > file.html")
    #os.system("cat file.html >> " + s)
    
    
    parsed = open("parsed.dat", 'w')
    input_file = open(s, 'r')
    gifts = open("gifts.dat", 'a')
    gifts_parsed = open("gifts_parsed.dat", 'w')
    start = False
    gift_lines = 0
    
    for line in input_file:
        if (line.startswith("Total:")):
            ss = line.split('Total: ')#splits the line between the two sides the delimiter
            tt = ss[1].split('Billing')#chooses the second of the split parts and resplits
            parsed.write("%s" % tt[0])#writes the first of the resplit lines
            
        if (line.startswith("Full Name:")):
            ss = line.split('Full Name:')
            tt = ss[1].split('Billing Email:')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("Billing Email:")):
            ss = line.split('Billing Email: ')
            tt = ss[1].split('Billing Phone: ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("Billing Phone:")):
            ss = line.split('Billing Phone: ')
            tt = ss[1].split('Billing Address: ')
            parsed.write("%s" % tt[0])
            
        if (line.startswith("Billing Address:")):
            ss = line.split('Billing Address: ')
            tt = ss[1].split('Credit ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("Address 2:")):
            ss = line.split('Address 2: ')
            tt = ss[1].split('City: ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("City:")):
            ss = line.split('City: ')
            tt = ss[1].split('State ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("State:")):
            ss = line.split('State:')
            tt = ss[1].split('Zip ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("Zip/Postal Code:")):
            ss = line.split('Zip/Postal Code:')
            tt = ss[1].split('Country ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("Country:")):
            ss = line.split('Country: ')
            tt = ss[1].split('Credit ')
            parsed.write("%s" % tt[0])
            gifts_parsed.write("%s" % tt[0])
            
        if (line.startswith("I Would Like to Designate my Gift for MilkyWay@home only")):
            next_line = input_file.next()
            parsed.write("%s" % next_line)
            
        if (line.startswith("I Would Like a Badge on my Milky Way User Profile")):
            next_line = input_file.next()
            parsed.write("%s" % next_line)   
            
        if (line.startswith("MilkyWay@home username (required for badge)")):
            next_line = input_file.next()
            parsed.write("%s" % next_line)   
            
        if (line.startswith("MilkyWay@home userID number (required for badge)")):
            next_line = input_file.next()
            parsed.write("%s" % next_line)
            
        if (line.startswith("Requested Gifts")):
            start = True
        if start:
            if (line.startswith("I Would Like to Designate my Gift for MilkyWay@home only")):
                start = False
            else:
                gifts_parsed.write("%s" % line)
                gift_lines = gift_lines + 1
 
    parsed = open("parsed.dat", 'r')
    data_file = open("fundraiser_spreadsheet_2015.dat", 'a')
    i = 0
    for line in parsed:
        if(i < 9):
            data_file.write("%s" % line.rstrip('\n'))
        else:
            data_file.write("%s\t" % line.rstrip('\n'))
        i = i + 1
    data_file.write("\n")
    
    os.system("rm parsed.dat")
    
    gifts_parsed = open("gifts_parsed.dat", 'r')
    i = 0
    j = 0
    for line in gifts_parsed:
        if(i < gift_lines):
            gifts.write(" %s" % line.rstrip('\n'))
        else:
            gifts.write("%s\t" % line.rstrip('\n'))
        i = i + 1
    gifts.write("\n")
    os.system("rm gifts_parsed.dat")
    
    
__main__(args);
#!/usr/bin/python
import csv
import sys


with open(sys.argv[1], newline='\n') as input:
    output = csv.reader(input, delimiter=",")
    for row in output:
        print("config firewall address")
        print("\tedit " + row[0])
        print("\tset type ipmask")
        print("\tset subnet " + row[1] + "/32")
        print("end")

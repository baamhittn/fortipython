#!/usr/bin/python
import csv
import sys


with open(sys.argv[1], newline='\n') as input:
    output = csv.reader(input, delimiter=",")
    for row in output:
        print("config firewall address")
        print("  edit " + row[0])
        print("  set type ipmask")
        print("  set subnet " + row[1] + "/32")
        print("end")

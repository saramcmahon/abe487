#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('usage')
    sys.exit(1)

infile = args[0]
if not os.path.isfile(infile):
    script = os.path.basename(sys.argv[1])
    print("\"%s\" is not a file" % (infile))
    sys.exit(1)

for line in open(infile):
    #line = line.rstrip() # this is another way, strip newline from RHS
    count = 0
    for char in line:
        if char == 'G' or char == 'g' or char == 'C' or char == 'c':
            count += 1

    linetot = len(line)
    print("%i" % (int((count/(linetot-1))*100)))

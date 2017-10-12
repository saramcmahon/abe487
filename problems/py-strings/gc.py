#!/usr/bin/env python3

from collections import Counter
import sys, string
import os

args = sys.argv

if len(args) < 2:
	script = os.path.basename(args[0])
	print('Usage: gc.py STRING'.format(script))
	sys.exit(1)

word = args[1]
nums = 0
nums2 = 0
cg1 = 'GCgc'
cg2 = 'ATat'

for char in word:
        if char in cg1:
                nums += 1
        else:
                nums2 += 1

percent = int(nums / (nums2 + nums) * 100)

print("%i%% GC" % (percent))










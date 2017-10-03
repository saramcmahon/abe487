#!/usr/bin/env python3

import sys, string
import sys
import os
	
args = sys.argv

if len(args) < 2:
	script = os.path.basename(args[0])
	print('Usage: vowel_counter.py STRING'.format(script))
	sys.exit(1)
	
numVowels = 0
strings = args[1:]

for char in strings:
	if char in 'aeiouAEIOU':
		numVowels += 1
		print('There is ' +(str(numVowels))+ 'vowels in' + "str")	
	else:
		numVowels += 0
		print('There is {} '.format(numVowels) + 'vowels in' + "args[1:]")


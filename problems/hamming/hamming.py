#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 2:
    print('usage')
    sys.exit(1)

a, b = args[0], args[1]

l1 = len(a)
l2 = len(b)
count = abs(l1 - l2)

for i in range(min(l1, l2)):
    c1 = a[i]
    c2 = b[i]
    if c1 != c2:
        count += 1   

print(count)

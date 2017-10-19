#!/usr/bin/env python3
import sys
import os

args = sys.argv[1:]
if len(args) < 1:
        print('usage: Input sequence for GC content')
        sys.exit(1)
Sequence = str(args[0])

GC= "GC"
count = 0
for char in Sequence:
	if char in GC:
		count = count +1	 
GC_Content = int((count / len(Sequence))*100)
print('{}% GC'.format(GC_Content))

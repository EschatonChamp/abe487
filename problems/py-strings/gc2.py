#!/usr/bin/env python3

import sys
import os 
args = sys.argv[1:]

if len(args) < 1:
	print('usage: Input file, return GC content by string.')
	sys.exit(1)

file = args[0]
if not os.path.isfile(file):
	print('"{}" is not a file'.format(file))
	sys.exit(1)

with open(file, 'r') as seqs:
	sequence = seqs.readlines()
	for line in sequence:
		Cytosine = 0
		Guanine = 0
		for char in line:
			if char == "C":
				Cytosine = Cytosine + 1
			elif char == "G":
				Guanine = Guanine + 1
		GC= Guanine + Cytosine
		GC_Content = int((GC / (len(line)-1))*100)
		print(GC_Content)


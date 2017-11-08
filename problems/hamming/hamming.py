#!/usr/bin/env python3
import os
import sys
args = sys.argv[1:]
if len(args) < 2:
	print('Usage: It takes two to tango')
	sys.exit(1)
list1 = list(args[0])
list2 = list(args[1])

def hammer(x, y):
	distance = 0 
	if x != y:
		distance += (len(y)-len(x))
	for seq1, seq2 in zip(x, y):
		if seq1 != seq2:
			distance += 1

	return(distance)

distance = hammer(list1, list2)
print(distance)

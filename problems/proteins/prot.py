#!/usr/bin/env python3

import os
import sys
args = sys.argv[1:]
if len(args) < 1:
	print('Usage: RNA')
	sys.exit(1)
seq = (str(args[0])).upper()
#print(seq)
codon = 3
frame = [seq[i:i+codon] for i in range(0, len(seq), codon)]
table_dict = {}
translation = []
with open("table.txt", "r") as f:
	for line in f:
		split = line.split()
		table_dict[split[0]] = "".join(split[1])

for i in frame:
	translation.append(table_dict[i])
	
print("".join(translation))
	


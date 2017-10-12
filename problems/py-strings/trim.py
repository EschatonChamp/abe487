#!/usr/bin/env python3

import sys 
import os

args = sys.argv[1:]
if len(args) < 1:
	print('usage: [Input] [Trim]')
	sys.exit(1)

file = args[0]
if len(args) > 1:
        Trim = int(args[1])

else:
        Trim = 5

if not os.path.isfile(file):
	Sequence_input = file
	print(Sequence_input[:Trim])
else:
	for Sequence in open(file, 'r'):
		print(Sequence[:Trim])		

#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 3:
	print('Usage: adder.py ARG1 ARG2')
	exit(1)

arg_one = sys.argv[1]
arg_two = sys.argv[2]


if arg_one.isdigit() and  arg_two.isdigit():
	add = int(arg_one) + int(arg_two)
	print(add)
else:
	if arg_one.isdigit():
		print('Cannot combine number and string')
		exit(1)
	elif arg_two.isdigit():
		print('Cannot combine number and string')
		exit(1)
	else:
		print(arg_one + ' and ' + arg_two)

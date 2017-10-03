#!/usr/bin/env python3

"""count the vowels in a word"""

import os
import sys 
args = sys.argv
if len(args) < 2:
	script = os.path.basename(args[0])
	print('Usage:', script , 'STRING')
	sys.exit(1)

S = ''.join(args[1:])
L = list(S)
count = 0
for let in str(L):
	if let  == 'a':
		count = count + 1
	elif let  == 'e':
		count = count + 1
	elif let == 'i':
		count = count + 1
	elif let =='o':
		count = count + 1
if count == 1:
	print('There is ' + str(count) + ' vowel in ' + '"{}."'.format(S))
else:
	print('There are ' + str(count) + ' vowels in ' + '"{}."'.format(S))

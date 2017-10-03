#!/usr/bin/env python3

import sys 
import os 

def main():
	"""main"""
	args = sys.argv
	names = args[1:]
	if len(args) < 2:
		script = os.path.basename(args[0])
		print('Usage: ' + script + ' NAME [NAME2 ...]')
		sys.exit(1)
	number = 0
	for i in names:
		number = number +1
	if number == 1:
		single = ''.join(names)
		print('Hello to the ' + str(number) + ' of you: ' + single + '!')
		sys.exit(0)
	if number == 2:
		double = ' and '.join(names)
		print('Hello to the ' + str(number) + ' of you: ' + double + '!')
		sys.exit(0)
	if number > 2:
		group = ', '.join(names[:-1])
		last_fella = ', and ' + names[-1]
		print('Hello to the ' + str(number) + ' of you: ' + group + last_fella + "!")
		sys.exit(0)  
if __name__ == '__main__':
    main()
    


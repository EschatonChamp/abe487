#!/usr/bin/env python3

import sys
import os 
args = sys.argv[1:]

file = args[0]
if len(file) < 1:
    print('usage: Input file, return GC content by string.')
    sys.exit(1)

if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)

# with open(file, 'r') as seqs:
#     sequences = seqs.read().splitlines()
#     for line in sequences:
#         gc = 0
#         for char in line.upper():
#             if char in "GC":
#                 gc += 1
# 
#         gc_content = int((gc / len(line))*100)
#         print(gc_content)

#seqs = open(file, 'r')
#sequences = seqs.read().splitlines()

for sequence in open(file, 'r'):
    sequence = sequence.rstrip()
    gc = 0
    for char in line.upper():
        if char in "GC":
            gc += 1

    gc_content = int((gc / len(line))*100)
    print(gc_content)


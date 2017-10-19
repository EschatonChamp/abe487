#!/usr/bin/env python3
#!/usr/bin/env python3

import os
import sys
from collections import Counter

args = sys.argv[1:]
if len(args) < 2:
        print('Usage: kmer_counter.py LEN STR')
        sys.exit(1)
kmer_str = args[0]
if kmer_str.isalpha():
        print('Kmer size \"{}\" is not a number'.format(kmer_str))
        sys.exit(1)
k= int(kmer_str)
if k < 1:
        print('Kmer size \"0\" must be > 0')
        sys.exit(1)
if k > len(args[1]):
        print('There are no {}-mers in \"{}\"'.format(kmer_str, args[1]))
        sys.exit(1)

Sequence = args[1]
print(Sequence)
kmer_dict = {}
possible = (len(Sequence) - k +1)
for i in range(possible):
        kmer = Sequence[i:i+k]
        if kmer not in kmer_dict:
                kmer_dict[kmer]  = 0
        kmer_dict[kmer] += 1
la = []
for x in kmer_dict:
    la.append(str(x) + ' ' + str(kmer_dict[x]))
lm = sorted(la)
print('\n'.join(lm))

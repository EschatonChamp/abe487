#!/usr/bin/env python3

import argparse
import os
import sys
#--------------------------------------------------------

def get_args():
	parser = argparse.ArgumentParser(description='Argparse Python script')
	parser.add_argument('file', metavar='file', help='BLAST tab output')
	parser.add_argument('-p', '--pct_id', help = 'Percent identity', metavar='float', type = float, default = 0) 
	parser.add_argument('-e', '--evalue', help = 'E-value', metavar='float', type=float, default = None)
	return parser.parse_args()
#--------------
def main():
	args = get_args()
	BLAST_file = args.file
	percent = args.pct_id
	eval = args.evalue
	fields = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
	if not os.path.isfile(BLAST_file):
		print('{} is not a file'.format(BLAST_file))
		sys.exit(1)
	for line in open(BLAST_file):
		stats = line.rstrip().split('\t')
		record = dict(zip(fields, stats))
		display = 'qseqid'
		count = 0
		final_product = [record['qseqid'], record['sseqid']]
		if float(record['pident']) >= percent:
			final_product.append(record['pident'])
			count +=1		
		if eval != None:
			if float(record['evalue']) < eval:
				final_product.append(record['evalue'])
				count +=1
		else:
			final_product.append(record['evalue'])
			count +=1
		if count == 2:
			yah = '\t'.join(final_product)
			print(yah)

#----------------------------
if __name__ == '__main__':
	main()

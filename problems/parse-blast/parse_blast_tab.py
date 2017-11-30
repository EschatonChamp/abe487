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
		final_product = [record['qseqid'], record['sseqid'], record['pident'], record['evalue']]
		for x in record:
			if record['evalue'] <= eval and record['pident'] >= percent:
				print(final_product)
		


#----------------------------
if __name__ == '__main__':
	main()

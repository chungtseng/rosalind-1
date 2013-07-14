import sys
import re
import os
from Bio import SeqIO
from Bio.Seq import Seq
import json
def main(filename):
	f = open(filename,'r')
	sequence = f.readline().strip('\n\r')
	freqs = json.loads(open('/home/kovarsky/rosalind/aminfreq.json','r').read())
	f.close()
	varnum = 1
	for letter in sequence:
		varnum = varnum * freqs[letter]
	varnum = varnum * 3
	print varnum

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
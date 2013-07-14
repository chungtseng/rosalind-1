import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import string
def main(filename):
	f = open(filename,'r')
	sequence = f.readline().strip('\n\r')
	exons = []
	for line in f:
		exons.append(line.strip('\n\r'))
	f.close()
	print exons
	for exon in exons:
		sequence = string.replace(sequence,exon,'')
	print sequence
	protein = str(Seq(sequence).transcribe().translate())
	f = open('new'+filename,'w')
	f.write(protein[:-1])
	f.close()


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
import sys
import re
import os
from Bio import SeqIO
from Bio.Seq import Seq
def main(filename):
	f = open(filename,'r')
	sequence = f.readline().strip('\n\r')
	prots = ''
	for i in range(0,3):
		prots = prots + str(Seq(sequence[i:]).transcribe().translate()) + '\n'
		if i!= 0:
			prots = prots + str(Seq(sequence[:-i]).reverse_complement().transcribe().translate()) + '\n'
		else:
			prots = prots + str(Seq(sequence).reverse_complement().transcribe().translate()) + '\n'
	orfs = re.findall('(?=(M\w*\*))',prots)
	orfs = set(orfs)
	f.close()
	f = open('new'+filename,'w')
	for orf in orfs:
		f.write(orf[:-1]+'\n')
	f.close()


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
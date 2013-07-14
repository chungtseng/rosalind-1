import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import string
def main(filename):
	f = open(filename,'r')
	sequence = f.readline().strip('\n\r')
	mf = open('masses.txt','r')
	mass_table = {}
	for line in mf:
		row = line.split()
		mass_table[row[0]] = float(row[1])
	mass = 0
	for  aminoacid in sequence:
		mass += mass_table[aminoacid]
	mass = mass + 2*1.00794 + 15.9994
	print '%.2f' % mass
	f.close()
	mf.close()


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
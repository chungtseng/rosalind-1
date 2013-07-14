import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import string


def main(filename):

	mf = open('masses.txt','r')
	mass_table = {}
	for line in mf:
		row = line.split()
		mass_table[round(float(row[1]),2)] = row[0]

	f = open(filename,'r')
	data = sorted(data,reverse=True)[1:]
	while len(data)!=0:

	pref_m = [ float(num.strip('\n\r')) for num in f]
	pref_m = sorted(pref_m)
	diffs = [round(pref_m[i+1] - pref_m[i],2) for i in range(len(pref_m)-1)]
	print diffs
	print mass_table
	prot = ''
	for diff in diffs:
		prot += mass_table[diff]

	f.close()
	mf.close()
	f = open('new'+filename,'w')
	f.write(prot)

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
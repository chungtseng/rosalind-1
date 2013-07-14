import sys
import re
from string import maketrans

def main(handler):
	f = open(handler,'r')
	seq = f.read()
	inv_seq = seq[::-1]
	intab = 'ATGC'
	outtab = 'TACG'
	transtab = maketrans(intab,outtab)
	inv_seq = inv_seq.translate(transtab)
	f.close()
	f = open ('new_'+handler,'w')
	f.write(inv_seq)


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
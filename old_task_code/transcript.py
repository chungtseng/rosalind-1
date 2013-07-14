import sys
import re
from string import maketrans

def main(handler):
	f = open(handler,'r')
	seq = f.read()
	intab = 'T'
	outtab = 'U'
	transtab = maketrans(intab,outtab)
	seq = seq.translate(transtab)
	f.close()
	f = open ('new_'+handler,'w')
	f.write(seq)


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
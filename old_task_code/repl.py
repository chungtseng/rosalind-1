import sys
import os
import re

def main(handler):
	f = open(handler,'r')
	sequence = f.read()
	A = len(re.findall('A',sequence))
	C = len(re.findall('C',sequence))
	G = len(re.findall('G',sequence))
	U = len(re.findall('U',sequence))
	print 'A: {0}; C {1}; G {2}; U {3}.'.format(A,C,G,U) 

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tcount_base.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
import sys
import os
import re

def main(handler):
	input_ = open(handler,'r')
	output = open('new_'+handler,'w')
	string = input_.readline()
	substring = input_.readline()
	print(len(string))
	N = len(re.findall('(?=('+substring+'))',string))
	print(N)
 	for occ in re.finditer('(?=('+substring+'))',string):
 		output.write(str(occ.start()+1)+' ')
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tsubs.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
import sys
import os
import re

def main(handler):
	input_ = open(handler,'r')
	output = open('new_'+handler,'w')
	string1 = input_.readline()
	string2 = input_.readline()
	index1 = []
	index2 = []
	for i in range(len(string2)):
		index1.append((string1[i],i))
		index2.append((string2[i],i))
	index1 = set(index1)
	index2 = set(index2)
	diff = index1 - index2
	print(diff)
	print(len(diff))
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tsubs.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
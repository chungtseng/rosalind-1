import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import string


def lexis(index,alphabet):
	newlist = []
	for letter in alphabet:
		if index > 1:
			for subs in lexis(index-1,alphabet):
				newlist.append(letter+subs)
		else:
			newlist.append(letter)
	return(newlist)



def main(filename):
	f = open(filename,'r')
	alphabet = f.readline().strip('\n\r').split()
	number = int(f.readline().strip('\n\r'))
	my_dict = lexis(number,alphabet)
	print(my_dict)
	f.close()
	f = open('new'+filename,'w')
	for word in my_dict:
		f.write(word+'\n')
	f.close()
	

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
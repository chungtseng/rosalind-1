import sys
import re
import math

def lexis(index,alphabet):
	newlist = []
	for letter in alphabet:
		if index > 1:
			for subs in lexis(index-1,alphabet):
				newlist.append(letter+subs)
		else:
			newlist.append(letter)
	return(newlist)



def fastaread(handler):
	f = open(handler,'r')
	seq = ''
	data = {}
	for line in f:
		if line[0] == '>':
			name = line[1:].rstrip('\n\r')
			seq = ''
			data[name] = seq
		else:
			data[name] = data[name] + line.rstrip('\n\r')
	f.close()
	return data

def main(handler):
	kmers = {}
	lex = lexis(4,['A','C','G','T'])
	for el in lex:
		if len(el) == 4:
			kmers[el] = 0
	data = fastaread(handler)
	seq = data[data.keys()[0]]
	klength = len(seq) - 3
	for j in range(0,klength):
		kmer = seq[j:j+4]
		kmers[kmer]+=1
	ls = []
	for el in lex:
		ls.append(kmers[el])
	print ' '.join(map(str,ls))

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tgraph.py <fasta file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


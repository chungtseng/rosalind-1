import sys
import os
from Bio import Phylo
import string
import re




def main(filename):
	f = open(filename,'r')
	line = f.readline().strip('\n\r')
	tree = f.readline().strip('\n\r')
	#t = Phylo.read(tree,'newick')
	#Phylo.draw_ascii(t)
	species = f.readline().strip('\n\r').split()
	start = re.search(species[0],tree).end()
	end = re.search(species[1],tree).start()
	path = tree[start:end]
	path = re.sub('[^\(\)]','',path)
	length = 0
	while (len(path)!=length):
		length = len(path)
		path = re.sub('\(\)','',path)
	print path



if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttree.py <file>'
		sys.exit(0)
	else:
		main(sys.argv[1])

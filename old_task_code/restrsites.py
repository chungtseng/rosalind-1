import sys
import re
from Bio.Seq import Seq

global restr_sites
restr_sites = []

def substr(seq,rseq,index,length):
	slength = len(seq)
	#Condition  statement here
	s1 = seq[index:index+length]
	s2 = rseq[-(index+length):-index]
	if index == 0: 
		s2 = rseq[-(index+length):]
	if s1 == s2:
		restr_sites.append([index+1,length])
		if (index - 1) >= 0 and (index + length + 1) <= slength:
			substr(seq,rseq,index-1,length+2)

def main(handler):
	f = open(handler,'r')
	print('hello')
	seq = f.readline().strip('\t\n')
	rseq = str(Seq(seq).reverse_complement())
	slength = len(seq)
	for i in range(0,(slength - 4)):
		substr(seq,rseq,i,4)
		substr(seq,rseq,i,5)
	f.close()
	for site in sorted(restr_sites):
		if site[1]<=8:
			print ' '.join(map(str,site))


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
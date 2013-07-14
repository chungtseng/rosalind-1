import sys
import os

def main(handler):
	input_ = open(handler,'r')
	seq = input_.readline().strip('\n\r')
	indices = [0]
	for i in range(1,len(seq)):
		subseq1 = seq[0:indices[i-1]+1]
		subseq2 = seq[i+1-len(subseq1):i+1]
		while (subseq1!= subseq2) and (len(subseq1)!=0):
			subseq1 = subseq1[:-1]
			subseq2 = subseq2[1:]
		indices.append(len(subseq2))
	s = ' '.join(map(str,indices))
	input_.close()
	output = open('new'+handler,'w')
	output.write(s)
	output.close()
	
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tspeedmotif.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
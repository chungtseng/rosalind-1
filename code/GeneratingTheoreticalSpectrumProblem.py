import os
import sys
from itertools import product


f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
f_iter = (line.strip().split() for line in f)
masses = {acid: int(val) for acid, val in f_iter}

def cyclic_subseq(seq, pos, subseqlen):
	seqlen = len(seq)
	irange = range(pos, pos + subseqlen)
	subseq = ''.join((seq[i % seqlen] for i in irange))
	return subseq

def subseq_mass_iter(seq, pos, subseqlen):
	seqlen = len(seq)
	irange = range(pos, pos + subseqlen)
	for i in irange:
		yield masses[seq[i % seqlen]]


def get_all_submasses(seq):
	seqlen = len(seq)
	submasses = []
	for i,j in product(range(seqlen), range(1, seqlen)):
		print i, j, cyclic_subseq(seq, i, j)
		submass = sum(subseq_mass_iter(seq, i, j))
		submasses.append(submass)
	return submasses

def main():
	f = open(sys.argv[1], "r")
	seq = f.readline().strip()
	submasses = get_all_submasses(seq)
	submasses.append(0)
	submasses.append(sum(subseq_mass_iter(seq, 0, len(seq))))
	print ' '.join(str(submass) for submass in sorted(submasses))
	f.close()


if __name__ == '__main__':
    main()
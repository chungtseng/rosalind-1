import os
import sys

def load_codon_table(handler):
	codons = {}
	for line in handler:
		els = line.strip().split()
		try:
			codons[els[0]] = els[1]
		except IndexError:
			codons[els[0]] = ''
	return codons


# def load_codon_table(handler):
# 	counts = {}
# 	for line in handler:
# 		els = line.strip().split()
# 		try:
# 			counts[els[1]] = counts.setdefault(els[1],0)+1
# 		except IndexError:
# 			pass
# 	return counts

# def count_vars(seq, counts):
# 	tcount = 1
# 	for base in seq:
# 		print counts[base], base
# 		tcount = tcount * counts[base]
# 	return tcount

def translate(codons, seq):
	seqlen = len(seq)
	out_seq = ''
	for i in xrange(0, seqlen, 3):
		out_seq += codons[seq[i:i+3]]
	return out_seq

def main():
	codon_f = open("/home/kovarsky/rosalind/code/RNA_codon_table_1.txt", "r")
	codons = load_codon_table(codon_f)
	seq = open(sys.argv[1], "r").readline().strip()
	print translate(codons, seq)



if __name__ == '__main__':
    main()
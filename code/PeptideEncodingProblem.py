import os
import sys


complements = {"A": "U",
                "G": "C",
                "U": "A",
                "C": "G"}

def get_complement(sequence):
    r_complement = ''
    for symb in sequence[::-1]:
        r_complement += complements[symb]
    return(r_complement)


def load_codon_table(handler):
	codons = {}
	for line in handler:
		els = line.strip().split()
		try:
			codons[els[0]] = els[1]
		except IndexError:
			codons[els[0]] = ''
	return codons

codon_f = open("/home/kovarsky/rosalind/code/RNA_codon_table_1.txt", "r")
codons = load_codon_table(codon_f)

def check_prot_match(protseq, nucseq):
	seqlen = len(nucseq)
	for i in xrange(0, seqlen, 3):
		codon = nucseq[i:i+3]
		aacid = protseq[i/3]
		if codons.get(codon, "-") != aacid:
			return False
	return True

def main():
	f = open(sys.argv[1], "r")
	seq = f.readline().strip().replace("T", "U")
	protseq = f.readline().strip()
	protlen = len(protseq)
	seqlen = len(seq)
	nucseqlen = protlen * 3

	peptides = []
	for i in xrange(seqlen - nucseqlen + 1):
		nucseq = seq[i:i + nucseqlen]
		if check_prot_match(protseq, nucseq) or check_prot_match(protseq, get_complement(nucseq)):
			peptides.append(nucseq)

	print '\n'.join(peptides).replace("U", "T")
	f.close()


if __name__ == '__main__':
    main()
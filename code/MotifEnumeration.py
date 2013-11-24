import FreqMismWordsProblem as freqs
from ApproxPatternMatchingProblem import is_equal
from ApproxPatternMatchingProblem import get_next_pos
import sys

def gen_kmers(dna, kmer_len):
    for seq in dna:
        length = len(seq)
        for i in xrange(length - kmer_len + 1):
            kmer = seq[i : i + kmer_len]
            yield(kmer)

def each_string(kmer, dna, mismnum):
    for seq in dna:
        if not appears(kmer, seq, mismnum):
            return False
    return True

def appears(kmer, seq, mismnum):
    i = 0
    seq_len = len(seq)
    kmer_len = len(kmer)
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        if is_equal(subseq, kmer, mismnum):
            return True
        i += get_next_pos(subseq, kmer, mismnum)
    return False
    


def main():
    f = open(sys.argv[1], "r")
    kmer_len, mismnum = f.readline().strip().split()
    kmer_len = int(kmer_len)
    mismnum = int(mismnum)

    dna = [line.strip() for line in f]

    motifs = set()
    for kmer in gen_kmers(dna, kmer_len):
        for rel_kmer in freqs.get_relatives(kmer, mismnum):
            if each_string(rel_kmer, dna, mismnum):
                motifs.add(rel_kmer)
    print ' '.join(str(motif) for motif in motifs)
    f.close()

if __name__ == '__main__':
    main()




import sys
from itertools import product


def hamming_dist(seq1, seq2):
    misms = (seq1[i] != seq2[i] for i in range(len(seq1)))
    return sum(misms)


def get_min_hamming_dist(kmer, seq):
    seq_len = len(seq)
    kmer_len = len(kmer)
    dist = kmer_len
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        new_dist = hamming_dist(kmer, subseq)
        if new_dist < dist:
            dist = new_dist
        i += 1
    return dist

bases = ["A", "T", "G", "C"]
def main():
    f = open(sys.argv[1], "r")
    kmer_len = int(f.readline().strip())
    dna = [line.strip() for line in f]
    min_total_dist = len(dna) * kmer_len

    for nucls in product(bases, repeat=kmer_len):
        kmer = ''.join(nucls)
        min_hamm_dists = (get_min_hamming_dist(kmer, seq) for seq in dna)
        total_dist = sum(min_hamm_dists)
        print kmer, total_dist
        if total_dist < min_total_dist:
            min_kmer = kmer
            min_total_dist = total_dist
    print "Answer: %s" % min_kmer

    f.close()


if __name__ == '__main__':
    main()
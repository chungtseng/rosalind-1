import sys
import operator


def prod(factors):
    return reduce(operator.mul, factors, 1)

def fetch_kmers(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        i += 1
        yield subseq

def main():
    f = open(sys.argv[1], "r")
    seq = f.readline().strip()
    kmer_len = int(f.readline())
    bases = f.readline().strip().split()
    prob_matrix = [{bases[i]: float(prob) for i, prob in enumerate(line.strip().split())} for line in f]
    max_prob = 0
    for kmer in fetch_kmers(seq, kmer_len):
        prob = prod(prob_matrix[i][base] for i, base in enumerate(kmer))
        if prob > max_prob:
            max_prob = prob
            max_kmer = kmer
    print max_kmer
    
    f.close()


if __name__ == '__main__':
    main()
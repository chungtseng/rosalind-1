import sys


def fetch_kmers(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        i += 1
        yield subseq

def main():
    with open(sys.argv[1]) as f:
        seq_1 = f.readline().strip()
        seq_2 = f.readline().strip()

    shared_pairs = []
    for i, kmer_1 in enumerate(fetch_kmers(seq_1, kmer_len)):
        for j, kmer_2 in enumerate(fetch_kmers(seq_2, kmer_len)):
            if kmer_1 == kmer_2 or kmer_1 == kmer_2[::-1]:
                shared_pairs.append((i, j))

    print shared_pairs

if __name__ == '__main__':
    main()
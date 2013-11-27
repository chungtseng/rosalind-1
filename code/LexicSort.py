from GibbsSampling import fetch_kmers
import sys

def main():
    with open(sys.argv[1]) as input_f:
        kmer_len = int(input_f.readline().strip())
        seq = input_f.readline().strip()
        kmers = list(fetch_kmers(seq, kmer_len))
        for kmer in sorted(kmers):
            print kmer

if __name__ == '__main__':
    main()

import sys


def fetch_kmers(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        i += 1
        yield subseq


def get_kmer_profile(kmers):
    profile = {}
    kmer_num = float(len(kmers))
    for kmer in kmers:
        for pos, base in enumerate(kmers):
            profile[pos][base] = profile.setdefault(pos,{}).setdefault(base, 0) + 1 / kmer_num

    return profile


def get_max_probable_kmer(kmers, profile):
    max_prob = 0
    for kmer in kmers:
        prob = sum(profile[i][base] for i, base in enumerate(kmer))
        if prob > max_prob:
            max_kmer = kmer
            max_prob = prob
    return max_kmer


def main():
    f = open(sys.argv[1], "r")
    seq = f.readline().strip()
    kmer_len = int(f.readline())
    bases = f.readline().strip().split()

    
    f.close()


if __name__ == '__main__':
    main()
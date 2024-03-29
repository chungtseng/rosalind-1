import sys
from math import log
from MedianString import hamming_dist
import operator

def fetch_kmers(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        i += 1
        yield subseq


def prod(factors):
    return reduce(operator.mul, factors, 1)

NUCLS = ("A", "T", "G", "C")

def get_kmer_profile(kmers):
    kmer_num = float(len(kmers))
    kmer_len = len(kmers[0])
    delta = 1 / (kmer_num + 1)
    profile = []
    for kmer in kmers:
        for pos, base in enumerate(kmer):
            if len(profile) <= pos:
                profile.append({nucl: delta for nucl in NUCLS})
            profile[pos][base] += delta
    return profile


def get_max_probable_kmer(kmers, profile):
    max_prob = -1
    consensus = get_consensus(profile)
    for kmer in kmers:
        prob = prod(profile[i].get(base, 0) for i, base in enumerate(kmer))
        if prob > max_prob:
            max_prob_kmer = kmer
            max_prob = prob
    res = max_prob_kmer

    return res

def get_consensus(profile):
    consensus = ''
    for bases in profile:
        consensus += max(bases, key=bases.get)
    return consensus

def get_kmer_score(kmers):
    profile = get_kmer_profile(kmers)
    consensus = get_consensus(profile)
    res = sum(hamming_dist(kmer, consensus) for kmer in kmers)
    return res

def greedy_search(kmer_len, seq_num, dna):
    best_kmer_score = kmer_len * seq_num
    # print dna[0]
    for kmer in fetch_kmers(dna[0], kmer_len):
        print '------'
        print kmer
        motifs = []
        motifs.append(kmer)
        for i in range(1, seq_num):
            profile = get_kmer_profile(motifs)
            ith_kmers = fetch_kmers(dna[i], kmer_len)
            motifs.append(get_max_probable_kmer(ith_kmers, profile))
        motif_score = get_kmer_score(motifs)
        if motif_score < best_kmer_score:
            best_kmer_score = motif_score
            best_motifs = motifs
    return best_motifs



def main():
    with open(sys.argv[1], "r") as f:
        nums = f.readline().strip().split()
        kmer_len = int(nums[0])
        seq_num = int(nums[1])
        dna = [line.strip() for line in f]
        best_motifs = greedy_search(kmer_len, seq_num, dna)
        print '\nAnswer:'
        for best_motif in best_motifs:
            print best_motif
    

if __name__ == '__main__':
    main()
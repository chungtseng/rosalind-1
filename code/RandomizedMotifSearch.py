import sys
from math import log
from MedianString import hamming_dist
import operator
from random import choice

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


def get_random_kmer(seq, kmer_len):
    kmers = list(fetch_kmers(seq, kmer_len))
    return choice(kmers)


def randomized_search(kmer_len, seq_num, dna):
    best_motifs = [get_random_kmer(seq, kmer_len) for seq in dna]
    # print best_motifs
    best_motif_score = get_kmer_score(best_motifs)
    profile = get_kmer_profile(best_motifs)
    # print profile
    for i in xrange(3):
        # print i, best_motif_score
        motifs = []
        for seq in dna:
            kmers = fetch_kmers(seq, kmer_len)
            most_prob_kmer = get_max_probable_kmer(kmers, profile)
            motifs.append(most_prob_kmer)
        motif_score = get_kmer_score(motifs)
        # print motifs, motif_score
        if motif_score < best_motif_score:
            # print motif_score, best_motif_score
            best_motif_score = motif_score
            best_motifs = motifs
            profile = get_kmer_profile(motifs)
    return best_motifs, best_motif_score



def main():
    with open(sys.argv[1], "r") as f:
        nums = f.readline().strip().split()
        kmer_len = int(nums[0])
        seq_num = int(nums[1])
        dna = [line.strip() for line in f]
        best_motif_score = seq_num * kmer_len
        for i in range(1000):
            motifs, motif_score = randomized_search(kmer_len, seq_num, dna)
            print i, best_motif_score
            if motif_score < best_motif_score:
                best_motifs = motifs
                best_motif_score = motif_score


        print '\nAnswer:'
        for best_motif in best_motifs:
            print best_motif
    

if __name__ == '__main__':
    main()
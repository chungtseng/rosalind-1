import sys
import itertools
import operator
import sets
#import collections


complements = {"A": "T",
                "G": "C",
                "T": "A",
                "C": "G"}

def get_complement(sequence):
    out_seq = ''
    for base in sequence:
        out_seq += complements[base]
    return out_seq[::-1]

def get_counts(sequence, kmer_len):
    length = len(sequence)
    counts = {}
    for i in xrange(length - kmer_len + 1):
        subseq = sequence[i : i + kmer_len]
        counts[subseq] = counts.setdefault(subseq, 0) + 1
    return counts

bases = ["A", "T", "G", "C"]

def get_relatives(sequence, mismnum):
    l = len(sequence)
    relatives = sets.Set([])
    for positions in itertools.combinations(xrange(l), mismnum):
        for variants in itertools.product(bases, repeat = mismnum):
            repseq = replace(sequence, variants, positions)
            relatives.add(repseq)
            # relatives.add(get_complement(repseq))
    return relatives

def replace(sequence, variants, positions):
    out_seq = ''
    j = 0
    for i, base in enumerate(sequence):
        if i in positions:
            out_seq += variants[j]
            j += 1
        else:
            out_seq += base
    return out_seq

def recount(counts, mismnum):
    newcounts = {}
    for kmer, count in counts.items():
        for relative_kmer in get_relatives(kmer, mismnum):
            newcounts[relative_kmer] = newcounts.setdefault(relative_kmer, 0) + count
    return newcounts

def recount_complement(counts):
    newcounts = {}
    for seq, count in counts.items():
        newcounts[seq] = counts.get(seq, 0) + counts.get(get_complement(seq), 0)
    return newcounts

def get_top_kmers(counts):
    top_kmers = []
    maxcount = 0
    for kmer, count in counts.items():
        if count > maxcount:
            top_kmers = [kmer]
            maxcount = count
        elif count == maxcount:
            top_kmers.append(kmer)
        else:
            pass
    return top_kmers



def main():
    f = open(sys.argv[1])
    sequence = f.readline().strip()
    elems = f.readline().strip().split()
    kmer_len = int(elems[0])
    mismnum = int(elems[1])
    counts = get_counts(sequence, kmer_len)


    counts = recount(counts, mismnum)
    counts = recount_complement(counts)
    top_kmers = get_top_kmers(counts)
    print ' '.join(top_kmers)


if __name__ == '__main__':
    main()
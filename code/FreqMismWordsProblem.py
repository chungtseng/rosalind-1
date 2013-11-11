import sys
import itertools
import operator
import sets
#import collections

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
            relatives.add(replace(sequence, variants, positions))
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
    elems = f.readline().strip().split()
    sequence = elems[0]
    kmer_len = int(elems[1])
    mismnum = int(elems[2])
    counts = get_counts(sequence, kmer_len)
    counts = recount(counts, mismnum)
    top_kmers = get_top_kmers(counts)
    print ' '.join(top_kmers)
    # print counts["GCGCACACAC"]
    # print counts["GCACACAGAC"]
if __name__ == '__main__':
    main()
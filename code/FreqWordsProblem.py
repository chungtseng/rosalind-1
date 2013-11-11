import sys



def get_top_kmers(sequence, kmer_len):
    length = len(sequence)
    counts = {}
    maxcount = 0
    for i in xrange(length - kmer_len + 1):
        subseq = sequence[i : i + kmer_len]
        count = counts.setdefault(subseq, 0) + 1
        counts[subseq] = count
        if count > maxcount:
            top_kmers = [subseq]
            maxcount = count
        elif count == maxcount:
            top_kmers.append(subseq)
        else:
            pass
    return top_kmers


def main():
    f = open(sys.argv[1])
    sequence = f.readline().strip()
    kmer_len = int(f.readline().strip())
    top_kmers = get_top_kmers(sequence, kmer_len)
    print ' '.join(top_kmers)
if __name__ == '__main__':
    main()
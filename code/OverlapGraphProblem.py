import sys
from itertools import combinations


def is_overlapped(suffix, prefix, min_overlap):
    max_overlap = len(prefix)
    for overlap in range(min_overlap, max_overlap):
        if prefix[:overlap] == suffix[max_overlap - overlap:]:
            return True
    return False


def main():
    with open(sys.argv[1], "r") as f:
        seqs = [line.strip() for line in f]
        min_overlap = len(seqs[0]) - 1
        for seq1, seq2 in combinations(seqs, 2):
            if is_overlapped(seq1, seq2, min_overlap):
                print "%s -> %s" % (seq1, seq2)
            if is_overlapped(seq2, seq1, min_overlap):
                print "%s -> %s" % (seq2, seq1)


if __name__ == '__main__':
    main()
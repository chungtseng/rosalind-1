import sys
import sets


class Clump():
    """docstring for Clump"""
    def __init__(self, sequence, kmer_len, window_len, min_ocnum):
        self.sequence = sequence
        sequence = sequence[0:window_len]
        length = len(sequence)
        clumps = sets.Set([])
        counts = {}
        for i in xrange(length - kmer_len + 1):
            kmer = sequence[i : i + kmer_len]
            count = counts.setdefault(kmer, 0) + 1
            counts[kmer] = count
            if count >= min_ocnum:
                clumps.add(kmer)

        self.counts = counts
        self.clumps = clumps
        self.kmer_len = kmer_len
        self.min_ocnum = min_ocnum
        self.first = sequence[0:kmer_len]
        self.window_len = window_len

    def next_step(self, pos):
        delta = self.window_len - self.kmer_len
        kmer = self.sequence[pos + delta:pos + self.window_len]
        self.counts[self.first] -= 1
        count = self.counts.setdefault(kmer, 0) + 1
        self.counts[kmer] = count
        if count >= self.min_ocnum:
            self.clumps.add(kmer)
        self.first = self.sequence[pos:pos + self.kmer_len]


def main():
    f = open(sys.argv[1])
    sequence = f.readline().strip()
    nums = [int(el) for el in f.readline().strip().split()]
    kmer_len, window_len, min_ocnum = nums
    clump_obj = Clump(sequence, kmer_len, window_len, min_ocnum)
    pos = 1
    seq_len = len(sequence)
    while pos <= seq_len - window_len:
        clump_obj.next_step(pos)
        pos += 1
    # print len(clump_obj.clumps)
    print ' '.join(clump_obj.clumps)
if __name__ == '__main__':
    main()
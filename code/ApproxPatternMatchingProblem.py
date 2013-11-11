import sys


def is_equal(str1, str2, maxmismnum = 3):
    if len(str1) != len(str2):
        return False
    else:
        length = len(str1)
        mismnum = 0
        for i in xrange(length):
            mismnum += (str1[i] != str2[i])
            # print str1[i], str2[i], mismnum
            if mismnum > maxmismnum:
                return False
            else:
                pass
        return True

def get_next_pos(subseq, pattern, mmnum):
    l = len(pattern)
    for i in xrange(1, l):
        if is_equal(subseq[i:], pattern[:l-i], mmnum):
            return i
    return l
    

def main():
    f = open(sys.argv[1])
    pattern = f.readline().strip()
    # pattern = "CTTGATCAT"
    pat_len = len(pattern)
    seq = f.readline().strip()
    seq_len = len(seq)
    mmnum = int(f.readline().strip())
    matched_pos = []
    i = 0
    while i <= seq_len - pat_len:
        subseq = seq[i:i+ pat_len]
        if is_equal(subseq, pattern, mmnum):
            matched_pos.append(str(i))
        i += get_next_pos(subseq, pattern, mmnum)
    print ' '.join(matched_pos)
    f.close()
if __name__ == '__main__':
    main()
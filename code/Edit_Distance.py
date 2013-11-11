import sys
import numpy as np
import itertools

def fill(size, value):
    if size:
        return([fill(size[1:], value) for i in range(size[0])])
    else:
        return(value)

def align(seq1, seq2):
    l1 = len(seq1) + 1
    l2 = len(seq2) + 1
    counts = np.zeros((l1, l2))
    for i,j in itertools.product(range(l1), range(l2)):
        if (i & j):
            counts[i, j] = min(counts)
        else:
            pass
def distance(seq1, seq2):
    l1 = len(seq1) + 1
    l2 = len(seq2) + 1
    distance = np.zeros((l1, l2))
    for i, j in itertools.product(range(l1), range(l2)):
        if (i and j):
            cond = (seq1[i -1] != seq2[j - 1])
            distance[i, j] = min(distance[i, j - 1] + 1,
                                 distance[i - 1, j] + 1,
                                 distance[i - 1, j - 1] + cond)
        else:
            distance[i, j] = i + j
    return(distance[i, j])

def common_subsequence(seq1, seq2):
    l1 = len(seq1) + 1
    l2 = len(seq2) + 1
    distance = np.zeros((l1, l2))
    direct = np.zeros((l1, l2))
    for i, j in itertools.product(range(l1), range(l2)):
        if (i and j):
            cond = (seq1[i -1] == seq2[j - 1])
            if cond:
                distance[i, j] = max(distance[i, j - 1],
                               distance[i - 1, j] ,
                               distance[i - 1, j - 1] + 1)
                direct[i, j] = np.argmax([distance[i, j - 1],
                                   distance[i - 1, j],
                                   distance[i - 1, j - 1] + 1])
            else:
                distance[i, j] = max(distance[i, j - 1],
                               distance[i - 1, j])
                direct[i, j] = np.argmax([distance[i, j - 1],
                                   distance[i - 1, j]])
        else:
            distance[i, j] = 0

    resseq = ''
    print direct
    print distance
    while (min(i, j) != 0):
        print resseq
        print (i,j)
        if direct[i, j] == 2:
            resseq = seq1[i - 1] + resseq
            i, j = i - 1, j - 1
        elif direct[i, j] == 0:
            i, j = i, j - 1
        else:
            i, j = i - 1, j
    return(resseq)

def common_suprestring(seq1, seq2):
    l1 = len(seq1) + 1
    l2 = len(seq2) + 1
    distance = np.zeros((l1, l2))
    direct = np.zeros((l1, l2))
    for i, j in itertools.product(range(l1), range(l2)):
        if (i and j):
            cond = (seq1[i -1] == seq2[j - 1])
            if cond:
                distance[i, j] = max(distance[i, j - 1],
                               distance[i - 1, j] ,
                               distance[i - 1, j - 1] + 1)
                direct[i, j] = np.argmax([distance[i, j - 1],
                                   distance[i - 1, j],
                                   distance[i - 1, j - 1] + 1])
            else:
                distance[i, j] = max(distance[i, j - 1],
                               distance[i - 1, j],
                               distance[i - 1, j - 1])
                direct[i, j] = np.argmax([distance[i, j - 1],
                                   distance[i - 1, j],
                                   distance[i - 1, j - 1]])
        else:
            distance[i, j] = 0

    resseq = ''
    print direct
    print distance
    while (min(i, j) != 0):
        print resseq
        print (i,j)
        if direct[i, j] == 2:
            if distance[i, j] == distance[i - 1, j - 1]:
                resseq = seq1[i - 1] + seq2[j - 1]+ resseq
            else:
                resseq = seq1[i - 1]+ resseq
            i, j = i - 1, j - 1
        elif direct[i, j] == 0:
            resseq = seq2[j - 1] + resseq
            i, j = i, j - 1
        else:
            resseq = seq1[i - 1] + resseq
            i, j = i - 1, j
    print resseq
    return(resseq)


def main():
    s1 = "ATCTGAT"
    s2 = "TGCATA"
    print(common_suprestring(s1 , s2))

if __name__ == '__main__':
    main()
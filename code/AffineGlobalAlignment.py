import numpy as np
import sys
from itertools import product


def main():
    gap_open_penalty = -11
    gap_extension_penalty = -1
    blosum = {}
    with open('/home/kovarsky/rosalind/code/BLOSUM62.txt', 'r') as tf:
        acids = tf.readline().split()
        for line in tf:
            fields = line.strip().split()
            acid = fields[0]
            scores = (int(field) for field in fields[1:])
            for i, score in enumerate(scores):
                blosum[(acid, acids[i])] = score


    with open(sys.argv[1], "r") as f:
        seq1 = f.readline().strip()
        n = len(seq1)
        seq2 = f.readline().strip()
        m = len(seq2)
    
    backtracker = {}
    low_weight_m = np.zeros((n+1, m+1))
    upp_weight_m = np.zeros((n+1, m+1))
    mid_weight_m = np.zeros((n+1, m+1))

    # low_weight_m[1:n+1,0] = [gap_open_penalty + gap_extension_penalty * (i-1) for i in range(1,n+1)]
    # upp_weight_m[0,1:m+1] = [gap_open_penalty + gap_extension_penalty * (j-1) for j in range(1,m+1)]
    # weight_m[0,0:m+1] = [indel_penalty * j for j in range(m+1)]

    for i, j in product(range(1, n+1), range(1, m+1)):
        mism_penalty = blosum[(seq1[i-1], seq2[j-1])]

        low_weight_m[i,j], backtracker[(i,j,0)] = max(
                        [(low_weight_m[i-1,j]+gap_extension_penalty, (i-1,j,0)),
                         (mid_weight_m[i-1,j]+gap_open_penalty, (i-1,j,1))])
        upp_weight_m[i,j], backtracker[(i,j,2)] = max(
                        [(upp_weight_m[i,j-1]+gap_extension_penalty, (i,j-1,2)),
                         (mid_weight_m[i,j-1]+gap_open_penalty, (i,j-1,1))])
        mid_weight_m[i,j], backtracker[(i,j,1)] = max(
                        [(low_weight_m[i,j], (i,j,0)),
                         (upp_weight_m[i,j], (i,j,2)),
                         (mid_weight_m[i-1,j-1] + mism_penalty, (i-1,j-1,1))])
        # directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
        #               (weight_m[i-1,j] + indel_penalty, (i-1, j)),
        #               (weight_m[i-1,j-1] + mism_penalty, (i-1, j-1))]
        # weight_m[i,j], backtracker[(i,j)] = max(directions)

    # print low_weight_m
    # print upp_weight_m
    # print mid_weight_m

    state = (n, m, 1)
    align_seq1 = ''
    align_seq2 = ''
    print int(mid_weight_m[n, m])
    while True:
        # print state
        i, j, layer = state

        if i == 0:
            next_state = (i, j - 1, 2)
        elif j == 0:
            next_state = (i - 1, j, 0)
        else:
            next_state = backtracker[state]
        i_new, j_new, layer_new = next_state

        if  (i_new, j_new) != (i, j):
            if i - i_new:
                align_seq1 = seq1[i_new] + align_seq1
            else:
                align_seq1 = '-' + align_seq1
            if j - j_new:
                align_seq2 = seq2[j_new] + align_seq2
            else:
                align_seq2 = '-' + align_seq2    
        state = next_state
        if (i_new, j_new) == (0, 0):
            break

    print align_seq1
    print align_seq2

if __name__ == '__main__':
    main()
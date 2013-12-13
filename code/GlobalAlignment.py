import numpy as np
import sys
from itertools import product


def main():
    indel_penalty = -5
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
    weight_m = np.zeros((n+1, m+1))
    weight_m[0:n+1,0] = [indel_penalty * j for j in range(n+1)]
    weight_m[0,0:m+1] = [indel_penalty * j for j in range(m+1)]
    for i, j in product(range(1, n+1), range(1, m+1)):
        mism_penalty = blosum[(seq1[i-1], seq2[j-1])]
        directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
                      (weight_m[i-1,j] + indel_penalty, (i-1, j)),
                      (weight_m[i-1,j-1] + mism_penalty, (i-1, j-1))]
        weight_m[i,j], backtracker[(i,j)] = max(directions)

    state = (n, m)
    align_seq1 = ''
    align_seq2 = ''
    print int(weight_m[n, m])
    while state != (0,0):
        i, j = state
        if i == 0:
            next_state = (i, j - 1)
        elif j == 0:
            next_state = (i - 1, j)
        else:
            next_state = backtracker[state]
        i_new, j_new = next_state

        if i - i_new:
            align_seq1 = seq1[i_new] + align_seq1
        else:
            align_seq1 = '-' + align_seq1
        if j - j_new:
            align_seq2 = seq2[j_new] + align_seq2
        else:
            align_seq2 = '-' + align_seq2
        
        state = next_state

    print align_seq1
    print align_seq2

if __name__ == '__main__':
    main()
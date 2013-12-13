import numpy as np
import sys
from itertools import product


def main():
    indel_penalty = -5
    blosum = {}
    with open('/home/kovarsky/rosalind/code/PAM250_1.txt', 'r') as tf:
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
    max_weight = 0
    max_weighted_state = (0, 0)
    for i, j in product(range(1, n+1), range(1, m+1)):
        mism_penalty = blosum[(seq1[i-1], seq2[j-1])]
        directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
                      (weight_m[i-1,j] + indel_penalty, (i-1, j)),
                      (weight_m[i-1,j-1] + mism_penalty, (i-1, j-1)),
                      (0, (0,0))]
        weight_m[i,j], backtracker[(i,j)] = max(directions)
        if weight_m[i,j] > max_weight:
            max_weight = weight_m[i,j]
            max_weighted_state = (i, j) 

    state = max_weighted_state
    align_seq1 = ''
    align_seq2 = ''
    print int(max_weight)    
    while state != (0,0) and weight_m[(state)] != 0:
        i, j = state
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
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

    print weight_m
    state = (n, m)
    common_str = ''
    print backtracker
    while 0 not in state:
        print state
        next_state = backtracker[state]
        # i, j = next_state
        # if weight_m[state] - weight_m[next_state]:
        #     common_str = seq1[i] + common_str
        state = next_state

    print common_str

if __name__ == '__main__':
    main()
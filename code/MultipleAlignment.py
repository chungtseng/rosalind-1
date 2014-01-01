import numpy as np
import sys
from itertools import product


def main():
    with open(sys.argv[1], "r") as f:
        seq1 = f.readline().strip()
        # print seq1
        n = len(seq1)
        seq2 = f.readline().strip()
        # print seq2
        m = len(seq2)
        seq3 = f.readline().strip()
        # print seq3
        p = len(seq3)
        
    
    backtracker = {}
    weight_m = np.zeros((n+1, m+1, p+1))
    for i, j, k in product(range(1, n+1), range(1, m+1), range(1,p+1)):
        all_equal = (seq1[i-1] == seq2[j-1] == seq3[k-1])
        directions = [(weight_m[i,j-1,k-1], (i,j-1,k-1)),
                      (weight_m[i-1,j,k-1], (i-1,j,k-1)),
                      (weight_m[i-1,j-1,k], (i-1,j-1,k)),
                      (weight_m[i-1,j,k], (i-1,j,k)),
                      (weight_m[i,j-1,k], (i,j-1,k)),
                      (weight_m[i,j,k-1], (i,j,k-1)),
                      (weight_m[i-1,j-1,k-1] + all_equal, (i-1,j-1,k-1))]
        weight_m[i,j,k], backtracker[(i,j,k)] = max(directions)

    state = (n, m, k)
    align_seq1 = ''
    align_seq2 = ''
    align_seq3 = ''
    print int(weight_m[n, m, k])
    # print weight_m
    while state != (0,0,0):
        # print state
        i, j, k = state
        if any(el == 0 for el in state):
            next_state = tuple(el if el == 0 else el-1 for el in state)
        else:
            next_state = backtracker[state]
        i_new, j_new, k_new = next_state

        if i - i_new:
            align_seq1 = seq1[i_new] + align_seq1
        else:
            align_seq1 = '-' + align_seq1
        if j - j_new:
            align_seq2 = seq2[j_new] + align_seq2
        else:
            align_seq2 = '-' + align_seq2
        if k - k_new:
            align_seq3 = seq3[k_new] + align_seq3
        else:
            align_seq3 = '-' + align_seq3
        
        state = next_state

    print align_seq1
    print align_seq2
    print align_seq3

if __name__ == '__main__':
    main()
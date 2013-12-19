import numpy as np
import sys
from itertools import product


def main():
    indel_penalty = -1
    mism_penalty = -1
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
        is_mism = (seq1[i-1] != seq2[j-1])
        directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
                      (weight_m[i-1,j] + indel_penalty, (i-1, j)),
                      (weight_m[i-1,j-1] + mism_penalty * is_mism, (i-1, j-1))]
        weight_m[i,j], backtracker[(i,j)] = max(directions)

    print -int(weight_m[n, m])

if __name__ == '__main__':
    main()
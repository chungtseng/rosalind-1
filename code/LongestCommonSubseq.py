import numpy as np
import sys
from itertools import product


def main():
    with open(sys.argv[1]) as f:
        seq1 = f.readline().strip()
        n = len(seq1)
        seq2 = f.readline().strip()
        m = len(seq2)
    
    backtracker = {}
    weight_m = np.zeros((n+1, m+1))
    for i, j in product(range(1, n+1), range(1, m+1)):
        cond = seq1[i-1] == seq2[j-1]
        directions = [(weight_m[i,j-1], (i, j-1)),
                      (weight_m[i-1,j], (i-1, j)),
                      (weight_m[i-1,j-1] + cond, (i-1, j-1))]
        weight_m[i,j], backtracker[(i,j)] = max(directions)

    state = (n, m)
    common_str = ''
    while state != (0, 0):
        next_state = backtracker[state]
        i, j = next_state
        if weight_m[state] - weight_m[next_state]:
            common_str = seq1[i] + common_str
        state = next_state

    print common_str

if __name__ == '__main__':
    main()
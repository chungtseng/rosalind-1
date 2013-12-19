import numpy as np
import sys
from itertools import product


def main():
    indel_penalty = -1
    mism_penalty = -1
    with open(sys.argv[1], "r") as f:
        long_seq = f.readline().strip()
        n = len(long_seq)
        short_seq = f.readline().strip()
        m = len(short_seq)
    
    backtracker = {}
    weight_m = np.zeros((n+1, m+1))
    # weight_m[0:n+1,0] = [indel_penalty * j for j in range(n+1)]
    # weight_m[0,0:m+1] = [indel_penalty * j for j in range(m+1)]
    for i, j in product(range(1, n+1), range(1, m+1)):
        is_mism = (long_seq[i-1] != short_seq[j-1])
        factor = 2 * is_mism - 1
        directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
                      (weight_m[i-1,j] + indel_penalty, (i-1, j)),
                      (weight_m[i-1,j-1] + mism_penalty * factor, (i-1, j-1)),
                      (0, (0,0))]
        weight_m[i,j], backtracker[(i,j)] = max(directions)

    max_weight = max(weight_m[n,])
    ind = max([i for i, weight in enumerate(weight_m[n,]) if weight == max_weight])

    state = (n, ind)
    align_long_seq = ''
    align_short_seq = ''
    while j != 0:
        i, j = state
        if i == 0:
            next_state = (i, j - 1)
        elif j == 0:
            next_state = (i - 1, j)
        else:
            next_state = backtracker[state]
        i_new, j_new = next_state

        if i - i_new:
            align_long_seq = long_seq[i_new] + align_long_seq
        else:
            align_long_seq = '-' + align_long_seq
        if j - j_new:
            align_short_seq = short_seq[j_new] + align_short_seq
        else:
            align_short_seq = '-' + align_short_seq
        
        state = next_state

    print align_long_seq
    print align_short_seq

if __name__ == '__main__':
    main()
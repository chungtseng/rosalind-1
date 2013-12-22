import numpy as np
import sys
from itertools import product


def align_seqs(seq1, seq2, indel_penalty=-1, mism_penalty=-1, match_score=1):
    n = len(seq1)
    m = len(seq2)
    backtracker = {}
    weight_m = np.zeros((n+1, m+1))

    # if not local:
        # weight_m[0:n+1,0] = [indel_penalty * j for j in range(n+1)]
        # weight_m[0,0:m+1] = [indel_penalty * j for j in range(m+1)]

    for i, j in product(range(1, n+1), range(1, m+1)):
        is_mism = (seq1[i-1] != seq2[j-1])
        score = mism_penalty * is_mism + (not is_mism) * match_score
        # print seq1[i-1],seq2[j-1],is_mism,score
        directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
                          (weight_m[i-1,j] + indel_penalty, (i-1, j)),
                          (weight_m[i-1,j-1] + score, (i-1, j-1))]
        # if local: directions.append((0, (0,0)))
        weight_m[i,j], backtracker[(i,j)] = max(directions)
        # print (i, j), weight_m[i,j], backtracker[(i,j)]
    return weight_m, backtracker

def restore_seqs(seq1, seq2, backtracker, state):
    align_seq1 = ''
    align_seq2 = ''
    while True:
        i, j = state
        if i == 0:
            next_state = (i, j - 1)
        elif j == 0:
            next_state = (i - 1, j)
        else:
            next_state = backtracker[state]
        i_new, j_new = next_state

        if j - j_new > 1:
            return None

        if i - i_new:
            align_seq1 = seq1[i_new] + align_seq1
        else:
            align_seq1 = '-' + align_seq1
        if j - j_new:
            align_seq2 = seq2[j_new] + align_seq2
        else:
            align_seq2 = '-' + align_seq2

        if i_new and j_new:
            state = next_state
        else:
            break    
        
    return align_seq1, align_seq2



def main():
    indel_penalty = -2
    mism_penalty = -2
    match_score = 1
    with open(sys.argv[1], "r") as f:
        suffix = f.readline().strip()
        prefix = f.readline().strip()
        n = len(suffix)
        m = len(prefix)

        
    weight_m, backtracker = align_seqs(suffix, prefix, indel_penalty, mism_penalty, match_score)
    max_weight = max(weight_m[n,])
    # inds = [i for i, weight in enumerate(weight_m[n,]) if weight == max_weight]
    inds = sorted(range(m+1), key=lambda key: weight_m[n, key], reverse=True)
    for ind in inds:
        state = (n, ind)
        seqs = restore_seqs(suffix, prefix, backtracker, state)
        if seqs:
            align_suffix, align_prefix = seqs
            print int(weight_m[n,ind])
            print align_suffix
            print align_prefix
            break

if __name__ == '__main__':
    main()
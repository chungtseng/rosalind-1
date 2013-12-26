import numpy as np
import sys
from itertools import product



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

def linear_space_alignment(seq1, seq2):
    # print seq1,seq2
    # raw_input("-")
    if seq1 and seq2:
        if len(seq1) == 1 or len(seq2) == 1:
            # l1 = len(seq1)
            # l2 = len(seq2)
            # seqs = (seq1 + '-' * (l2 - 1), seq2 + '-' * (l1 - 1))
            # score = blosum[seq1[0],seq2[0]] + indel_penalty * (max(l1, l2) - 1)
            return align(seq1, seq2)
        else:
            mid_1, mid_2 = get_mid_node(seq1, seq2)
            left_seq, left_score = linear_space_alignment(seq1[:mid_1], seq2[:mid_2])
            right_seq, right_score = linear_space_alignment(seq1[mid_1:], seq2[mid_2:])
            return tuple(s1+s2 for s1, s2 in zip(left_seq, right_seq)), left_score + right_score
    else:
        if seq1:
            return (seq1, '-' * len(seq1)), indel_penalty * len(seq1)
        elif seq2:
            return ('-' * len(seq2), seq2), indel_penalty * len(seq2)



def get_state(seq1, seq2, ini_state=None):
    n = len(seq1)
    m = len(seq2)
    if ini_state is None:
        state = [indel_penalty * i for i in xrange(n + 1)]
    else:
        state = ini_state
    for i in xrange(m):
        new_state = [state[0] + indel_penalty]
        for j in xrange(n):
            score = max(new_state[-1] + indel_penalty,
                        state[j+1] + indel_penalty,
                        state[j] + blosum[seq1[j], seq2[i]])
            new_state.append(score)
        state = new_state
    return state


def align(seq1, seq2):
    n = len(seq1)
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
    return (align_seq1, align_seq2), int(weight_m[n, m])

def get_mid_node(seq1, seq2):
    half = len(seq2) / 2
    left_subseq = seq2[:half]
    right_subseq = seq2[half:]
    left_state = get_state(seq1, left_subseq)
    right_state = get_state(seq1[::-1], left_subseq[::-1])

    fin_state = [l + r for l,r in zip(left_state, right_state[::-1])]
    # print fin_state
    return fin_state.index(max(fin_state)), half

def main():
    with open(sys.argv[1], "r") as f:
        seq1 = f.readline().strip()
        seq2 = f.readline().strip()

    (align_seq1, align_seq2), score = linear_space_alignment(seq1, seq2)
    print score
    print align_seq1
    print align_seq2


    # ini_state = [indel_penalty * i for i in xrange(n + 1)]

    # backtracker = {}


    # # low_weight_m = np.zeros((n+1, m+1))
    # # upp_weight_m = np.zeros((n+1, m+1))
    # # mid_weight_m = np.zeros((n+1, m+1))

    # # low_weight_m[1:n+1,0] = [gap_open_penalty + gap_extension_penalty * (i-1) for i in range(1,n+1)]
    # # upp_weight_m[0,1:m+1] = [gap_open_penalty + gap_extension_penalty * (j-1) for j in range(1,m+1)]
    # # weight_m[0,0:m+1] = [indel_penalty * j for j in range(m+1)]

    # for i, j in product(range(1, n+1), range(1, m+1)):
    #     mism_penalty = blosum[(seq1[i-1], seq2[j-1])]

    #     low_weight_m[i,j], backtracker[(i,j,0)] = max(
    #                     [(low_weight_m[i-1,j]+gap_extension_penalty, (i-1,j,0)),
    #                      (mid_weight_m[i-1,j]+gap_open_penalty, (i-1,j,1))])
    #     upp_weight_m[i,j], backtracker[(i,j,2)] = max(
    #                     [(upp_weight_m[i,j-1]+gap_extension_penalty, (i,j-1,2)),
    #                      (mid_weight_m[i,j-1]+gap_open_penalty, (i,j-1,1))])
    #     mid_weight_m[i,j], backtracker[(i,j,1)] = max(
    #                     [(low_weight_m[i,j], (i,j,0)),
    #                      (upp_weight_m[i,j], (i,j,2)),
    #                      (mid_weight_m[i-1,j-1] + mism_penalty, (i-1,j-1,1))])
    #     # directions = [(weight_m[i,j-1] + indel_penalty, (i, j-1)),
    #     #               (weight_m[i-1,j] + indel_penalty, (i-1, j)),
    #     #               (weight_m[i-1,j-1] + mism_penalty, (i-1, j-1))]
    #     # weight_m[i,j], backtracker[(i,j)] = max(directions)

    # # print low_weight_m
    # # print upp_weight_m
    # # print mid_weight_m

    # state = (n, m, 1)
    # align_seq1 = ''
    # align_seq2 = ''
    # print int(mid_weight_m[n, m])
    # while True:
    #     # print state
    #     i, j, layer = state

    #     if i == 0:
    #         next_state = (i, j - 1, 2)
    #     elif j == 0:
    #         next_state = (i - 1, j, 0)
    #     else:
    #         next_state = backtracker[state]
    #     i_new, j_new, layer_new = next_state

    #     if  (i_new, j_new) != (i, j):
    #         if i - i_new:
    #             align_seq1 = seq1[i_new] + align_seq1
    #         else:
    #             align_seq1 = '-' + align_seq1
    #         if j - j_new:
    #             align_seq2 = seq2[j_new] + align_seq2
    #         else:
    #             align_seq2 = '-' + align_seq2    
    #     state = next_state
    #     if (i_new, j_new) == (0, 0):
    #         break

    # print align_seq1
    # print align_seq2

if __name__ == '__main__':
    main()
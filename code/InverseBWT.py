import sys
from collections import defaultdict



def get_inverse_dict(seq):
    count = defaultdict(int)
    occurence = []
    for symb in seq:
        occurence.append(count[symb])
        count[symb] += 1

    count_less = {}
    prev = 0
    for key in sorted(count.keys()):
        count_less[key] = prev
        prev += count[key]

    inverse_dict = {}
    for i, symb in enumerate(seq):
        val = count_less[symb] + occurence[i]
        inverse_dict[i] = val

    return inverse_dict

def inverse_bwt(seq):
    inverse_dict = get_inverse_dict(seq)
    sorted_seq = sorted(seq)
    L = len(seq)
    res = ''
    ind = seq.index('$')
    while len(res) < L:
        ind = inverse_dict[ind]
        res = sorted_seq[ind] + res
    return res

def main():
    with open(sys.argv[1]) as f:
        seq = f.readline().strip()

    print inverse_bwt(seq)



if __name__ == '__main__':
    main()
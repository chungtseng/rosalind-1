import sys
from collections import defaultdict



def get_inverse_vector(seq):
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

    inverse_vector = []
    for i, symb in enumerate(seq):
        val = count_less[symb] + occurence[i]
        inverse_vector.append(val)

    print count_less
    print occurence
    print count
    print inverse_vector
    return inverse_vector

def inverse_bwt(seq):
    inverse_vector = get_inverse_vector(seq)
    L = len(seq)
    res = '$'
    ind = seq.index('$')
    while len(res) < L:
        ind = inverse_vector[ind]
        res = seq[ind] + res
    return res

def main():
    with open(sys.argv[1]) as f:
        seq = f.readline().strip()

    print inverse_bwt(seq)



if __name__ == '__main__':
    main()
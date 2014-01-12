import sys
from itertools import tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def get_num_of_breaks(permutation):
    length = len(permutation)
    num_of_breaks = 0
    for prev_el, el in pairwise(permutation):
        num_of_breaks += (el != prev_el + 1)
    num_of_breaks += (abs(permutation[0]) != 1) + (abs(permutation[-1]) != length)
    return num_of_breaks

def main():
    with open(sys.argv[1], "r") as f:
        raw_str = f.readline().strip('()\n').split()
        permutation = [int(el) for el in raw_str]
    print get_num_of_breaks(permutation)

if __name__ == '__main__':
    main()
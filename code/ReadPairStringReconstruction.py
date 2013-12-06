import sys
from itertools import combinations
from collections import defaultdict
from EulerianPath import get_eulerian_path
from itertools import izip


def are_pairs_overlapped(head, tail):
    suffix = head[0][1:], head[1][1:]
    prefix = tail[0][:-1], tail[1][:-1]
    return suffix == prefix

def main():
    read_pairs = []
    with open(sys.argv[1], "r") as f:
        gap_len = int(f.readline())
        # print gap_len
        read_pairs = [tuple(line.strip().split("|")) for line in f]
    pair_num = len(read_pairs)

    node_dict = defaultdict(list)
    for i, j in combinations(range(pair_num), 2):
        pair1 = read_pairs[i]
        pair2 = read_pairs[j]
        if are_pairs_overlapped(pair1, pair2):
            node_dict[i].append(j)
        if are_pairs_overlapped(pair2, pair1):
            node_dict[j].append(i)

    path = get_eulerian_path(node_dict)
    rpath = (read_pairs[node] for node in path)

    headseq, tailseq = rpath.next()
    read_len = len(headseq)
    for head, tail in rpath:
        headseq += head[-1]
        tailseq += tail[-1]

    res = headseq + tailseq[-(gap_len+read_len):]
    print res

    
        

if __name__ == '__main__':
    main()
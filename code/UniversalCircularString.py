import sys
from collections import deque
from EulerianCycle import get_eulerian_cycle
# from datetime import datetime


def get_bin_kmer(num, kmer_len):
    return bin(num)[2:].rjust(kmer_len, '0')


def get_universal_graph(kmer_len):
    node_dict = {}
    kmer_num = 2 ** (kmer_len - 1)
    for out_node in xrange(kmer_num):
        in_node = (out_node << 1) & (kmer_num - 1)
        node_dict[out_node] = [in_node, in_node + 1]
    return node_dict

def get_binary_string(cycle, kmer_len):
    bins = (get_bin_kmer(node, kmer_len) for node in cycle)
    # bin_seq = bins.next()
    bin_seq = ''
    bin_seq += ''.join(bin_subseq[-1:] for bin_subseq in bins)
    return bin_seq

def main():
    # startTime = datetime.now()
    with open(sys.argv[1], "r") as f:
        kmer_len = int(f.readline().strip())
    node_dict = get_universal_graph(kmer_len)
    cycle = get_eulerian_cycle(node_dict)
    print get_binary_string(cycle, kmer_len - 1)
    # print(datetime.now()-startTime)
        
if __name__ == '__main__':

    main()

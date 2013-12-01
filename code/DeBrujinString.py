import sys

def fetch_kmer_pairs(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len -1:
        head = seq[i : i + kmer_len]
        tail = seq[i + 1 : i + kmer_len + 1]
        i += 1
        yield (head, tail)


def make_graph(seq, edge_kmer_len):
    kmer_len = edge_kmer_len - 1
    graph = {}
    for head, tail in fetch_kmer_pairs(seq, kmer_len):
        graph.setdefault(head, []).append(tail)
    return graph

def main():
    with open(sys.argv[1], "r") as f:
        edge_kmer_len = int(f.readline().strip())
        seq = f.readline().strip()
        graph = make_graph(seq, edge_kmer_len)

        for head, tails in graph.items():
            print "%s -> %s" % (head, ','.join(tails))


if __name__ == '__main__':
    main()
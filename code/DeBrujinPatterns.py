import sys

def make_pattern_graph(kmers):
    graph = {}
    for kmer in kmers:
        head = kmer[ : -1]
        tail = kmer[1 : ]
        graph.setdefault(head, []).append(tail)
    return graph

def main():
    with open(sys.argv[1], "r") as f:
        kmers = (line.strip() for line in f)
        graph = make_pattern_graph(kmers)

        for head, tails in graph.items():
            print "%s -> %s" % (head, ','.join(tails))


if __name__ == '__main__':
    main()
import sys
from collections import defaultdict

def make_graph(kmers):
    graph = defaultdict(list)

    def __():
        return [0, 0]
    degrees = defaultdict(__)

    for kmer in kmers:
        head = kmer[ : -1]
        degrees[head][0] += 1
        tail = kmer[1 : ]
        degrees[tail][1] += 1
        graph[head].append(tail)
    return graph, degrees


def get_chain(starts, graph):
    chain = []
    start = starts.pop()
    current_node = start
    while True:
        chain.append(current_node)
        neighbours = graph[current_node]
        if ((current_node in starts 
            and current_node != start) or not neighbours):
            break
        else:
            current_node = neighbours.pop()
    return chain



def main():
    with open(sys.argv[1]) as f:
        kmers = (line.strip() for line in f)
        graph, degrees = make_graph(kmers)

    starts = []
    for node, val in degrees.iteritems():
        if not (val[0] == val[1] == 1):
            starts += [node] * val[0]
    
    chains = []
    while starts:
        chain = get_chain(starts, graph)
        chainseq = chain.pop(0) + ''.join(seq[-1] for seq in chain)
        chains.append(chainseq)
    print ' '.join(chains)

if __name__ == '__main__':
    main()
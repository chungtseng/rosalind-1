import sys
import re
from collections import defaultdict


def main():
    pattern = re.compile("(\d+)->(\d+):(\d+)")
    out_graph = defaultdict(list)
    in_graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        start = int(f.readline())
        end = int(f.readline())
        for line in f:
            out_node, in_node, weight = [int(field) for field
                             in pattern.match(line).groups()]
            out_graph[out_node].append(in_node)
            in_graph[in_node].append((out_node, weight))


    backtracker = defaultdict(int)
    counts = {}
    
    node = start
    node_applicants = []
    visited_nodes = []
    while True:
        in_nodes = [(out_node, weight) for out_node, weight in in_graph[node] if out_node in visited_nodes]
        if in_nodes:
            count, max_in_node = max([(weight + counts[out_node], out_node )
                                         for out_node, weight in in_nodes])
        else:
            count, max_in_node = 0, None
        backtracker[node] =  max_in_node
        counts[node] = count

        node_applicants += out_graph[node]
        for applicant in list(node_applicants):
            if any(out_node in node_applicants for out_node, weight in in_graph[applicant]):
                pass
            else:
                next_node = applicant
                node_applicants.remove(applicant)
                break

        visited_nodes.append(node)
        if node == end:
            break
        node = next_node
    
    track = []
    node = end
    while True:
        track.append(node)
        if node == start:
            break
        node = backtracker[node]

    print counts[end]
    print "->".join(str(node) for node in track[::-1])

if __name__ == '__main__':
    main()
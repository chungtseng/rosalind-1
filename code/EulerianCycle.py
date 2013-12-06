import sys
from collections import deque


def get_eulerian_cycle(node_dict):
    ini_node =  max(node_dict, key=node_dict.get)
    cycle = []
    candidates = [ini_node]
    while True:
        cycle, candidates = get_cycle(candidates, cycle, node_dict)
        # print cycle, candidates
        if candidates:
            ini_node = candidates[0]
            ini_node_ind = list(cycle).index(ini_node)
            cycle = cycle[ini_node_ind + 1:] + cycle[:ini_node_ind + 1]
        else:
            return cycle


def get_cycle(candidates, cycle, node_dict):
    current_node = candidates[0]
    while True:
        neighbours = node_dict[current_node]
        if neighbours:
            next_node = neighbours.pop()
            candidates.append(next_node)
            if not neighbours and current_node:
                # del neighbours
                candidates.remove(current_node)
            cycle.append(next_node)
            current_node = next_node
        else:
            # del neighbours
            candidates.remove(current_node)
            return cycle, candidates

def main():
    node_dict = {}
    with open(sys.argv[1], "r") as f:
        for i, line in enumerate(f):
            out_node, in_nodes = line.strip().split('->')
            in_nodes = [int(node) for node in in_nodes.split(',')]
            node_dict[int(out_node)] = in_nodes
    cycle = get_eulerian_cycle(node_dict)
    cycle = cycle + cycle[:1]
    print '->'.join(str(node) for node in cycle)

        
if __name__ == '__main__':

    main()
import sys
from collections import deque

# class Node():
#     def __init__(self, arg):
#         self.outnodes = []

#     def degree(self):
#         return len(self.outnodes)

#     def add_node(self, outnode):
#         self.outnodes.append(self.outnodes)

#     def get_node(self):
#         return self.outnodes.pop()

def rotate_cycle(cycle, ini_node):
    ind = cycle.index


def build_node_dict(adj_list):
    node_dict = {}
    for out_node, in_node in adj_list:
        node_dict.setdefault(out_node, []).append(in_node)
    return node_dict


def get_eulerian_cycle(node_dict):
    ini_node =  max(node_dict, key=node_dict.get)
    cycle = deque([])
    while True:
        cycle, candidates = get_cycle(cycle, node_dict, ini_node)
        print cycle, candidates
        if candidates:
            ini_node = candidates.pop()
            ini_node_ind = cycle.index(ini_node)
            cycle = cycle.rotate(- 1 - ini_node)
        else:
            return cycle


def get_cycle(cycle, node_dict, ini_node):
    current_node = ini_node
    candidates = [current_node]
    while True:
        print current_node
        neighbours = node_dict[current_node]
        if neighbours:
            next_node = neighbours.pop()
            candidates.append(next_node)
            if not neighbours:
                # del neighbours
                candidates.remove(current_node)
            cycle.append(next_node)
            current_node = next_node
        else:
            return cycle, candidates

def main():
    node_dict = {}
    with open(sys.argv[1], "r") as f:
        for line in f:
            out_node, in_nodes = line.strip().split('->')
            in_nodes = [int(node) for node in in_nodes.split(',')]
            node_dict[int(out_node)] = in_nodes
    print node_dict
    cycle = get_eulerian_cycle(node_dict)
    print cycle

        
if __name__ == '__main__':

    main()
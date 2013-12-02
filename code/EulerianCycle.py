import sys


class Node():
    def __init__(self, arg):
        self.outnodes = []

    def degree(self):
        return len(self.outnodes)

    def add_node(self, outnode):
        self.outnodes.append(self.outnodes)

    def get_node(self):
        return self.outnodes.pop()


def build_node_dict(adj_list):
    node_dict = {}
    for out_node, in_node in adj_list:
        node_dict.setdefault(out_node, []).append(in_node)
    return node_dict

def get_cycle(node_dict, ini_node):
    current_node = ini_node
    cycle = []
    while len(current_node) != 0:
        cycle.append(current_node)
        neighbours = node_dict[current_node]
        next_node = neighbours.pop()
        if not len(neighbours):
            del neighbours
            candidates.remove(current_node)

        candidates.append(next_node)
        current_node = next_node
    return cycle


if __name__ == '__main__':
    main()
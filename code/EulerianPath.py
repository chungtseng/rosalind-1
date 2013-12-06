import sys
from collections import deque
from collections import defaultdict


def get_eulerian_cycle(node_dict):
    ini_node =  max(node_dict, key=node_dict.get)
    cycle = []
    candidates = [ini_node]
    while True:
        cycle, candidates = get_cycle(candidates, cycle, node_dict)
        # print cycle, candidates
        if candidates:
            ini_node = candidates[0]
            ini_node_ind = cycle.index(ini_node)
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
            candidates.remove(current_node)
            return cycle, candidates

def get_eulerian_path(node_dict):
    degree_balance = defaultdict(int)
    for out_node, in_nodes in node_dict.iteritems():
        for in_node in in_nodes:
            degree_balance[in_node] += 1
            degree_balance[out_node] -= 1

    start = [key for key, val in degree_balance.iteritems() if val < 0].pop()
    end = [key for key, val in degree_balance.iteritems() if val > 0].pop()
    print "start: %d, end: %d" % (start, end)

    node_dict.setdefault(end, []).append(start)
    cycle = get_eulerian_cycle(node_dict)
    start_node_ind = cycle.index(start)
    cycle = cycle[start_node_ind:] + cycle[:start_node_ind]

    return cycle


def main():
    node_dict = {}
    with open(sys.argv[1], "r") as f:
        for i, line in enumerate(f):
            out_node_str, in_nodes_str = line.strip().split('->')
            out_node = int(out_node_str)
            in_nodes = [int(node) for node in in_nodes_str.split(",")]
            node_dict[out_node] = in_nodes

    cycle = get_eulerian_path(node_dict)
    print '->'.join(str(node) for node in cycle)

        
if __name__ == '__main__':

    main()
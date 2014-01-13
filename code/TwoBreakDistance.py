import sys
import os
from collections import defaultdict
from re import findall

def int_el(el):
    print el
    return int(el)

def get_synteny_block_array(str_line):
    chroms = findall("[\+\-\d\s]+", str_line.strip())
    block_array = [[int(el) for el in chrom.split(" ")] for chrom in chroms]
    return block_array


def make_graph(block_array):
    graph = defaultdict(list)
    for synteny_blocks in block_array:
        l = len(synteny_blocks)
        for i, node in enumerate(synteny_blocks):
            graph[node].append( - synteny_blocks[(i+1) % l])
            graph[ - node].append(synteny_blocks[i-1])
    return graph

def get_num_of_cycles(graph):
    # print graph
    nodes = graph.keys()
    current_node = nodes[0]
    num_of_cycles = 0
    # print nodes
    while True:
        neighbours = graph[current_node]
        if neighbours:
            next_node = neighbours.pop()
            # print "%d -> %d" % (current_node, next_node)
            graph[next_node].remove(current_node)
            nodes.remove(next_node)
            # print nodes
            current_node = next_node
        else:
            num_of_cycles += 1
            if nodes:
                current_node = nodes[0]
            else:
                return num_of_cycles



def main():
    with open(sys.argv[1]) as f:
        block_array_1 = get_synteny_block_array(f.readline())
        block_array_2 = get_synteny_block_array(f.readline())

    block_array = block_array_1 + block_array_2
    graph = make_graph(block_array)
    print len(graph)/2 - get_num_of_cycles(graph)

if __name__ == '__main__':
    main()
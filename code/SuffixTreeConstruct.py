import sys
from itertools import izip

def get_lcp_array(suff_array, text):
    lcp_array = []
    for i in range(len(suff_array)):
        lcp = 0
        if i:
            pos1 = suff_array[i]
            pos2 = suff_array[i-1]
            for s1, s2 in izip(text[pos1:],text[pos2:]):
                if s1 == s2:
                    lcp += 1
                else:
                    break
        lcp_array.append(lcp)
    return lcp_array

def get_suff_array(text):
    suff_array = range(len(text))
    return sorted(suff_array, key=lambda x: text[x:x+1000])
    # return sorted(suff_array, cmp=lambda x, y :cmp(text[x:],text[y:]))

import sys

class Trie(object):
    """docstring for Trie"""
    def __init__(self):
        self.trie = {}

    def add(self, word):
        subtrie = self.trie
        for s in word:
            subtrie[s] = subtrie.setdefault(s, {})
            subtrie = subtrie[s]

    def in_trie(self, word):
        subtrie = self.trie
        for s in word:
            if s in subtrie.keys():
                subtrie = subtrie[key]
            else:
                return False
        return True

class SuffixTree(object):
    """docstring for SuffixTree"""
    def __init__(self):
        self.tree = 
        





class Edge():
    """docstring for Branch"""
    def __init__(self, data, parent=None):
        self.parent = parent
        self.data = data
        self.children = [] 
        
    def add(self, pattern):
        for child in self.children:
            l = 0
            for s1, s2 in izip(pattern,child.data):
                if s1 != s2:
                    break
                else:
                    l += 1
            if l:
                if len(child.data ) == l:
                    child.add(pattern[l:])
                else:
                    child.data = pattern[:l]
                    child.children = 
                break


        if not l:
            self.children.append(Edge(pattern, self))



def bypass_trie(trie, root_node = 1):
    node = root_node
    for key, subtrie in trie.items():
        next_node = node + 1
        print root_node, next_node, key
        node = bypass_trie(subtrie, next_node)
    return node


def main():
    trie = Trie()
    with open(sys.argv[1], "r") as f:
        for line in f:
            trie.add(line.strip())

    bypass_trie(trie.trie)


        

if __name__ == '__main__':
    main()
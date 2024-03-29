import sys
from itertools import izip
from copy import copy

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


class Tree():
    """docstring for Branch"""
    def __init__(self, data, parent=None):
        self.parent = parent
        self.data = data
        self.children = [] 
        
    def add(self, pattern):
        l = 0
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
                    child_copy = copy(child)

                    child.children = [child_copy, Tree(pattern[l:], child)]
                    child.data = pattern[:l]

                    child_copy.data = child_copy.data[l:]
                break
        if not l:
            self.children.append(Tree(pattern, self))



def bypass_tree(tree):
    print tree.data
    for subtree in tree.children:
        bypass_tree(subtree)


def main():
    tree = Tree('')
    with open(sys.argv[1], "r") as f:
        seq = f.readline().strip()

    for i in range(len(seq)):
        tree.add(seq[i:])
    

    bypass_tree(tree)


        

if __name__ == '__main__':
    main()
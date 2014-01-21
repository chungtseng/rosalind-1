import sys
from itertools import izip
from copy import copy
from itertools import chain
from copy import deepcopy

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
    def __init__(self, data, signature=None, parent=None):
        self.parent = parent
        self.data = data
        self.children = []
        if signature:
            self.signature = set([signature])
        else:
            self.signature = set([]) 
        
    def add(self, pattern, signature):
        l = 0
        # print signature
        self.signature.add(signature)
        for child in self.children:
            l = 0
            for s1, s2 in izip(pattern,child.data):
                if s1 != s2:
                    break
                else:
                    l += 1
            if l:
                if len(child.data ) == l:
                    child.add(pattern[l:], signature)
                    child.signature.add(signature)
                else:
                    child_copy = copy(child)
                    child_copy.data = child_copy.data[l:]
                    child_copy.parent = child
                    child_copy.signature = deepcopy(child.signature)


                    child.children = [child_copy, Tree(pattern[l:], signature, child)]
                    child.data = pattern[:l]
                    child.signature.add(signature)
                break
        if not l:
            self.children.append(Tree(pattern, signature,self))


# class Tree():
#     """docstring for Branch"""
#     def __init__(self, data, signature=None, parent=None):
#         self.parent = parent
#         self.data = data
#         self.children = []
#         if signature:
#             self.signature = set([signature])
#         else:
#             self.signature = set([])
        
#     def construct(self, suffix, lcp, signature):
#         if not lcp:
#             self.children.append(Tree(suffix, signature, self))
#         else:
#             child = self.children[-1]
#             L = len(child.data)
#             if L < lcp:
#                 child.signature.add(signature)
#                 child.construct(suffix[L:], lcp-L, signature)
#             else:
#                 child_copy = copy(child)

#                 child.children = [child_copy, Tree(suffix[lcp:], signature, child)]
#                 child.data = suffix[:lcp]

#                 child_copy.data = child_copy.data[lcp:]


def bypass_tree(tree):
    if tree.data:
        print tree.data, tree.signature
    for subtree in tree.children:
        bypass_tree(subtree)

def get_max_shared_substr(tree):
    shared_seqs = ['']
    for subtree in tree.children:
        if len(subtree.signature) > 1:
            seq = tree.data + get_max_shared_substr(subtree)
            print seq
            shared_seqs.append(seq)
        else:
            pass
    print shared_seqs
    return max(shared_seqs)


def main():
    tree = Tree('')
    with open(sys.argv[1], "r") as f:
        seq1 = f.readline().strip() + '$1'
        seq2 = f.readline().strip() + '$2'
    
        # suff_array_1 = get_suff_array(seq1)
        # lcp_array_1 = get_lcp_array(suff_array_1, seq1)

    iter1 = ((seq1[i:], 1) for i in range(len(seq1)))
    iter2 = ((seq2[j:], 2) for j in range(len(seq2)))

    # for suff_pos, lcp in zip(suff_array_2, lcp_array_2):
    #     tree.construct(seq2[suff_pos:], lcp, 2)

    for pattern, signature in chain(iter1, iter2):
    # for pattern, signature in iter1:
        # print pattern, signature
        tree.add(pattern, signature)
    
    for subtree in tree.children:
        print subtree.data, subtree.signature

    bypass_tree(tree)
    print get_max_shared_substr(tree)


        

if __name__ == '__main__':
    main()
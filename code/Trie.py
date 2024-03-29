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
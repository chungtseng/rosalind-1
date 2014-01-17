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


def match_trie(trie, text):
    subtrie = trie
    for i, s in enumerate(text):
        if s in subtrie.keys():
            subtrie = subtrie[s]
            if not subtrie:
                return True
        else:
            return False
    return False


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
        text = f.readline().strip()
        for line in f:
            trie.add(line.strip())

    poses = []
    for i in range(len(text)):
        text = text[1:]
        if match_trie(trie.trie, text):
            poses.append(i + 1)

    print ' '.join(str(pos) for pos in poses)



        

if __name__ == '__main__':
    main()
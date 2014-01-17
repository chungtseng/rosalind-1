import sys


basedict = {'A':0,
            'T': 1,
            'G': 2,
            'C': 3}

class Trie(object):
    """docstring for Trie"""
    def __init__(self):
        self.trie = {}

    def add(self, word):
        subtrie = self.trie
        for s in word:
            key = basedict[s]
            subtrie = subtrie.setdefault(key, {})

    def in_trie(self, word):
        subtrie = self.trie
        for s in word:
            if s in subtrie.keys():
                subtrie = subtrie[key]
            else:
                return False
        return True

def longest_repeat(trie):
    res = ''
    for key, branch in trie.items():
        repeat = get_repeat(key, branch)
        if len(res) < len(repeat):
            res = repeat
    return res


def get_repeat(key, branch):
    subtrie = branch
    repeat = key
    while True:
        if len(subtrie) == 1:
            key = subtrie.keys()[0]
            subtrie = subtrie[key]
            repeat += key
        elif len(subtrie) == 0:
            return ''
        else:
            return repeat + longest_repeat(subtrie)


def main():
    trie = Trie()
    with open(sys.argv[1], "r") as f:
        text = f.readline().strip()

    for i in range(len(text)):
        trie.add(text[i:])
    print len(text)
    # for key, branch in trie.trie.items():
        # print key, branch
    # print longest_repeat(trie.trie)

    

        

if __name__ == '__main__':
    main()


# A TATCGTTTTATCGTT
#   TATCGTT
# {'A': {'T': {'C': {'G': {'T': {'T': {'T': {'T': {'A': {'T': {'C': {'G': {'T': {'T': {}}}}}}}}}}}}}}, 'C': {'G': {'T': {'T': {'T': {'T': {'A': {'T': {'C': {'G': {'T': {'T': {}}}}}}}}}}}}, 'T': {'A': {'T': {'C': {'G': {'T': {'T': {}}}}}}, 'T': {'A': {'T': {'C': {'G': {'T': {'T': {}}}}}}, 'T': {'A': {'T': {'C': {'G': {'T': {'T': {}}}}}}}}}}
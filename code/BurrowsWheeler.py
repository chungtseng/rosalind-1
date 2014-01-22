from collections import deque
import sys


def main():
    with open(sys.argv[1]) as f:
        seq = f.readline().strip()

    seq_deque = deque(seq)
    cyclic_rotations = []
    for i in range(len(seq)):
        cyclic_rotations.append(list(seq_deque))
        seq_deque.rotate(1)

    cyclic_rotations = sorted(cyclic_rotations)
    res = ''.join(r[-1] for r in cyclic_rotations)
    print res

if __name__ == '__main__':
    main()
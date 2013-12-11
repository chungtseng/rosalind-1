import numpy as np
import sys
from itertools import product


def main():
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        m = int(f.readline())
        down = np.matrix([[int(num) for num in f.readline().split()] for i in range(n)])
        f.readline()
        right = np.matrix([[int(num) for num in f.readline().split()] for j in range(n+1)])
    print n, m
    print down
    print right
    weight_m = np.zeros((n+1, m+1))
    for i in range(1, n+1):
        weight_m[i,0] = weight_m[i-1,0] + down[i-1,0]
    for j in range(1, m+1):
        weight_m[0,j] = weight_m[0,j-1] + right[0,j-1]
    for i, j in product(range(1, n+1), range(1, m+1)):
        r_w = weight_m[i,j-1] + right[i,j-1]
        d_w = weight_m[i-1,j] + down[i-1,j]
        weight_m[i,j] = max(r_w, d_w)

    print int(weight_m[n,m])



if __name__ == '__main__':
    main()
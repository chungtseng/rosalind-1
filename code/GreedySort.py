import sys
import os

def flip(array, num):
    ind = [abs(el) for el in array].index(num)
    reverse = [-el for el in array[num - 1:ind + 1][::-1]]
    return array[:num - 1] + reverse + array[ind + 1:]


def perm_print(permutation):
    print '(%s)' % ' '.join(str(el) if el < 0 else  '+' + str(el) for el in permutation)


def greedy_sort(permutation):
    for i in range(len(permutation)):
        if abs(permutation[i]) != i + 1:
            permutation = flip(permutation, i + 1)
            perm_print(permutation)
        if permutation[i] == -(i+1):
            permutation = flip(permutation, i + 1)
            perm_print(permutation)
    return permutation

def main():
    with open(sys.argv[1], "r") as f:
        raw_str = f.readline().strip('()\n').split()
        permutation = [int(el) for el in raw_str]
    greedy_sort(permutation)

if __name__ == '__main__':
    main()
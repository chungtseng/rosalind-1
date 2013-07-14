import sys

def main(handler):
    f = open(handler,'r')
    array = [int(el) for el in f.readline().strip().split(' ')]
    probabilities = [1.0,1.0,1.0,0.75,0.5,0.0]
    expectation = sum(map(lambda x, y: x * y, array, probabilities)) * 2
    print expectation
    
if __name__ == '__main__':
    flag = 'none'
    if (len(sys.argv) < 2):
        print 'usage:\tcalculate_expected_offspring.py <in: file with six integers corresponding to number of particular pairs>'
        sys.exit(0)
    else:
        main(sys.argv[1])






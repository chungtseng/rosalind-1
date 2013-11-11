import sys

class Fib(dict):
    """docstring for FibSeries"""
    def getz(self, arg):
        return(self.get(arg, 0))

def Fibonacci(lim):
    fib_series = Fib({})
    for i in xrange(1,lim + 1):
        if i == 1:
            fib_series[i] = 1
        else:
            fib_series[i] = fib_series.getz(i - 1) + fib_series.getz(i - 2)
    return(fib_series[lim])

def MortalFibonacci(lim, mortality):
    fib_series = Fib({})
    m = mortality
    for i in xrange(1,lim + 1):
        if i == 1:
            fib_series[i] = 1
        else:
            fib_series[i] = (fib_series.getz(i - 1) + fib_series.getz(i - 2) - 
                            fib_series.getz(i - m - 1) - fib_series.getz(i - m - 2))
    return(fib_series[lim])

def main():
    lim = int(sys.argv[1])
    mortality = int(sys.argv[2])
    for i in xrange(1,lim+1):
        print(MortalFibonacci(i, mortality))
    

if __name__ == '__main__':
    main()
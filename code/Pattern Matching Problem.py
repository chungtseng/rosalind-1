import sys

complements = {"A": "T",
                "G": "C",
                "T": "A",
                "C": "G"}

def get_complement(sequence):
    r_complement = ''
    for symb in sequence[::-1]:
        r_complement += complements[symb]
    return(r_complement)

def main():
    f = open(sys.argv[1],"r")
    r_complement = get_complement(f.readline().strip())
    print r_complement

if __name__ == '__main__':
    main()
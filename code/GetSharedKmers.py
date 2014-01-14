import sys
from collections import defaultdict
from itertools import product
import re

complements = {"A": "T",
                "G": "C",
                "T": "A",
                "C": "G"}

def get_complement(sequence):
    r_complement = ''
    for symb in sequence[::-1]:
        r_complement += complements[symb]
    return(r_complement)



def fetch_kmers(seq, kmer_len):
    seq_len = len(seq)
    i = 0
    while i <= seq_len - kmer_len:
        subseq = seq[i:i + kmer_len]
        i += 1
        yield subseq

def get_kmer_dict(kmer_iter, complement=True):
    kmer_dict = defaultdict(list)
    for i, kmer in enumerate(kmer_iter):
        kmer_dict[kmer].append(i)
        if complement:
            kmer_dict[get_complement(kmer)].append(i)
    return kmer_dict

def main():
    with open(sys.argv[1]) as f:
        kmer_len = int(f.readline().strip())
        seq_1 = f.readline().strip()
        seq_2 = f.readline().strip()

    kmer_dict_1 = get_kmer_dict(fetch_kmers(seq_1, kmer_len), complement=False)
    kmer_dict_2 = get_kmer_dict(fetch_kmers(seq_2, kmer_len))

    sorted_keys_1 = set(kmer_dict_1.keys())
    sorted_keys_2 = set(kmer_dict_2.keys())

    shared_pos = []

    for kmer in sorted_keys_1 & sorted_keys_2:
        for pos in product(kmer_dict_1[kmer],kmer_dict_2[kmer]):
            shared_pos.append(pos)

    # for kmer in sorted_keys_1 & comp_sorted_keys_2:
    #     comp = get_complement(kmer)
    #     for pos in product(kmer_dict_1[kmer],kmer_dict_2[comp]):
    #         shared_pos.append(pos)

    for p in sorted(shared_pos):
        print p

    # for kmer, coord in kmer_dict_1.items():
    #     if kmer in kmer_dict_2.keys():
    #         
    #     elif get_complement(kmer) in kmer_dict_2.keys():
    #         comp = get_complement(kmer)
    #         for pos in product(kmer_dict_1[kmer],kmer_dict_2[comp]):
    #             print pos
    #     else:
    #         pass

    # for kmer in fetch_kmers(seq_1,kmer_len):
    #     s1 = re.findall(kmer, seq_2)
    #     s2 = re.findall(get_complement(kmer), seq_2)
    #     if s1 or s2:
    #         print s1 + s2


if __name__ == '__main__':
    main()
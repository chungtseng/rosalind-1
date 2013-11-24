import sys
from itertools import product
from itertools import combinations

# f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
# acid_masses = list(set([int(line.strip().split()[1]) for line in f]))

def spec_convolution(spectrum):
	spectrum = sorted(spectrum)
	L = len(spectrum)
	nonzero_els = []
	for pept1, pept2 in combinations(spectrum, 2):
		delta = pept2 - pept1
		if delta != 0:
			nonzero_els.append(delta)
	return nonzero_els




def main():
	spec_f = open(sys.argv[1])
	spectrum = [int(num) for num in spec_f.readline().strip().split()]
	spec_f.close()
	convolves = sorted(spec_convolution(spectrum))
	print ' '.join([str(el) for el in convolves])
	# pepts = get_peptides(spectrum, N_tresh)
	# output = ' '.join('-'.join(str(mass) for mass in pept)
	# 									for pept in pepts)
	# res2 = set(['-'.join(str(mass) for mass in pept)
										# for pept in pepts])
	# res1 = open("~/")

	# print output
if __name__ == '__main__':
    main()
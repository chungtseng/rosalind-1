import sys
from itertools import product
from itertools import combinations
import LeaderboardCyclopeptideSequencing as LCS

# f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
# acid_masses = list(set([int(line.strip().split()[1]) for line in f]))

def spec_convolution(spectrum):
	spectrum = sorted(spectrum)
	L = len(spectrum)
	multiplicity = {}
	for pept1, pept2 in combinations(spectrum, 2):
		delta = pept2 - pept1
		if 57 <= delta <= 200:
			multiplicity[delta] = multiplicity.setdefault(delta, 0) + 1
	reverse_multiplicity = {}

	for delta, mult in multiplicity.items():
		reverse_multiplicity.setdefault(mult, []).append(delta)

	return reverse_multiplicity


def cut_by_score(dict_obj, tresh):
	top = []
	score_list = sorted(dict_obj.keys(),reverse=True)
	for score in score_list:
		top += dict_obj[score]
		if len(top) > tresh:
			break
		else:
			pass
	return top


def main():
	spec_f = open(sys.argv[1])
	M_tresh = int(spec_f.readline().strip())
	N_tresh = int(spec_f.readline().strip())
	spectrum = [int(num) for num in spec_f.readline().strip().split()]
	spec_f.close()

	multiplicity = spec_convolution(spectrum)
	LCS.acid_masses = cut_by_score(multiplicity, M_tresh)
	pepts = LCS.get_peptides(spectrum, N_tresh)
	print len(pepts)
	output = ' '.join('-'.join(str(mass) for mass in pept)
										for pept in pepts[0:24])

	print "Answer:\n%s" % output



if __name__ == '__main__':
    main()
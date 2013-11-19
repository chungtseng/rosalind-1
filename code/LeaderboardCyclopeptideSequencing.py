import sys
from itertools import product

f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
acid_masses = list(set([int(line.strip().split()[1]) for line in f]))

def get_theoretical_spectrum(pept):
	L = len(pept)
	spectrum = []
	for i,j in product(range(L), range(1, L)):
		spectrum.append(sum(pept[i % L] for i in range(i, i + j)))
	spectrum += [0, sum(pept)]
	return spectrum



def get_score(pept,spectrum):
	spectrum = spectrum[:]
	pept_spectrum = get_theoretical_spectrum(pept)
	score = 0
	for mass in pept_spectrum:
		if mass in spectrum:
			score += 1
			spectrum.remove(mass)
	return score


def extend_pept_list(pept_list, spectrum, N_tresh):
	pept_dict = {}
	score_set = set()
	parent_mass = max(spectrum)

	for pept in pept_list:
		for mass in acid_masses:
			newpept = pept + [mass]
			pept_mass = sum(newpept)
			if pept_mass <= parent_mass:
				score = get_score(newpept, spectrum)
				score_set.add(score)
				pept_dict.setdefault(score, []).append(newpept)
			else:
				pass

	length = len(score_set)
	print score_set#, pept_dict
	score_list = list(score_set)[length - N_tresh:length]

	new_pept_list = []
	for key, val in pept_dict.items():
		if key in score_list:
			new_pept_list += val
	return new_pept_list


def get_peptides(spectrum, N_tresh):
	new_pept_list = [[]]
	i = 0
	while len(new_pept_list) > 0:
	# while i < 3:
		pept_list = new_pept_list
		new_pept_list = extend_pept_list(pept_list, spectrum, N_tresh)
		i += 1
		# print new_pept_list, len(new_pept_list)
	return pept_list


def main():
	spec_f = open(sys.argv[1])
	N_tresh = int(spec_f.readline().strip())
	spectrum = [int(num) for num in spec_f.readline().strip().split()]
	spec_f.close()
	pepts = get_peptides(spectrum, N_tresh)
	output = ' '.join('-'.join(str(mass) for mass in pept)
										for pept in pepts)
	# res2 = set(['-'.join(str(mass) for mass in pept)
										# for pept in pepts])
	# res1 = open("~/")

	# print output
if __name__ == '__main__':
    main()
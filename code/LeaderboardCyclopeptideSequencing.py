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


def cut_pept_list(pept_dict, N_tresh):
	pept_list = []
	score_list = sorted(pept_dict.keys(),reverse=True)
	for score in score_list:
		pept_list += pept_dict[score]
		if len(pept_list) > N_tresh:
			break
		else:
			pass
	return pept_list


def extend_pept_list(pept_list, spectrum, N_tresh):
	pept_dict = {}
	parent_mass = max(spectrum)

	for pept in pept_list:
		for mass in acid_masses:
			newpept = pept + [mass]
			pept_mass = sum(newpept)
			if pept_mass <= parent_mass:
				score = get_score(newpept, spectrum)
				pept_dict.setdefault(score, []).append(newpept)
			else:
				pass
	if len(pept_dict) != 0:
		max_score = max(pept_dict.keys())
		max_scored_pepts = pept_dict[max_score]
	else:
		max_score = 0
		max_scored_pepts = []
	new_pept_list = cut_pept_list(pept_dict, N_tresh)
	print len(new_pept_list)
	return new_pept_list, max_score, max_scored_pepts


def get_peptides(spectrum, N_tresh):
	new_pept_list = [[]]
	i = 0
	max_score = 0
	max_scored_pepts = [0]
	while len(new_pept_list) > 0:
	# while i < 3:
		pept_list = new_pept_list
		res = extend_pept_list(pept_list, spectrum, N_tresh)
		new_pept_list, new_max_score, new_max_scored_pepts = res
		if new_max_score > max_score:
			max_score = new_max_score
			max_scored_pepts = new_max_scored_pepts
		elif new_max_score == max_score:
			max_scored_pepts += new_max_scored_pepts
		i += 1
		# print new_pept_list, len(new_pept_list)
	print max_score, max_scored_pepts, len(max_scored_pepts)
	return max_scored_pepts


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

	print output
if __name__ == '__main__':
    main()
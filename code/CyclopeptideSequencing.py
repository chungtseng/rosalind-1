import sys

f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
acid_masses = list(set([int(line.strip().split()[1]) for line in f]))

def get_theoretical_spectrum(pept):
	L = len(pept)
	spectrum = []
	for sublen in range(1, L + 1):
		for i in range(L + 1 - sublen):
			spectrum.append(sum(pept[i:i + sublen]))
	return spectrum



def is_consistent(pept, spectrum):
	pept_spectrum = get_theoretical_spectrum(pept)
	spectrum = list(spectrum)
	for mass in pept_spectrum:
		if mass in spectrum:
			spectrum.remove(mass)
		else:
			return False
	return True



def extend_pept_list(pept_list, spectrum):
	new_pept_list = []
	for pept in pept_list:
		for mass in acid_masses:
			newpept = pept + [mass]
			if is_consistent(newpept, spectrum):
				new_pept_list.append(newpept)
	return new_pept_list


def get_peptides(spectrum):
	new_pept_list = [[]]
	while len(new_pept_list) > 0:
		pept_list = new_pept_list
		new_pept_list = extend_pept_list(pept_list, spectrum)
		# print new_pept_list, len(new_pept_list)
	return pept_list


def main():
	spec_f = open(sys.argv[1])
	spectrum = [int(num) for num in spec_f.readline().strip().split()]
	spec_f.close()
	pepts = get_peptides(spectrum)
	output = ' '.join('-'.join(str(mass) for mass in pept)
										for pept in pepts)
	res2 = set(['-'.join(str(mass) for mass in pept)
										for pept in pepts])
	# res1 = open("~/")

	print output
if __name__ == '__main__':
    main()
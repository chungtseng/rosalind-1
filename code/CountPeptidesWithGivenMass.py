import os
import sys
# from itertools import product
# from itertools import chain
# from collections import Counter
# from sets import Set
from math import factorial
from operator import mul


f = open("/home/kovarsky/rosalind/code/integer_mass_table.txt")
masses = list(set([int(line.strip().split()[1]) for line in f]))
masses_inds = {val: i for i, val in enumerate(masses)}
min_mass = min(masses)


def get_peptides(protmass, masses):
	res = []
	if len(masses) > 0:
		peptmass = masses[0]
		masses = masses[1:]
		for i in xrange(protmass / peptmass + 1):
			new_protmass = protmass - i * peptmass
			if new_protmass == 0:
				res.append([i])
			elif new_protmass > 0:
				for pept in get_peptides(protmass - i * peptmass, masses):
					res.append([i] + pept)
	return res

def count_combinations(peptide_variants):
	totalcount = 0
	for variant in peptide_variants:
			summ = factorial(sum(variant))
			factorials = (factorial(el) for el in variant)
			mult = reduce(mul, factorials, 1)
			totalcount += summ / mult
	return totalcount


def main():
	for protmass in xrange(200,1200,10):
		pept_variants = get_peptides(protmass, masses)
		print protmass, count_combinations(pept_variants)


if __name__ == '__main__':
    main()



# masses = 
# mass_list = [el for el in f_iter]
# masses = {f_iter}


# peptides = {}
# def get_peptides(protmass):
# 	res = set()
# 	if protmass >= min_mass:
# 		for mass in masses:
# 			for peptide in peptides.get(protmass - mass, set()):
# 				newpeptide = list(peptide)
# 				newpeptide[masses_inds[mass]] += 1
# 				newpeptide = tuple(newpeptide)
# 				res.add(newpeptide)
# 	elif protmass == 0:
# 		res.add(tuple([0] * len(masses)))
# 	peptides[protmass] = res

# for i in xrange(100):
# 	print i
# 	get_peptides(i)


# def renorm_peptides(peptide_variant):
# 	variants = []
# 	for i, acid_count in enumerate(peptide_variant):
# 		if masses[mass_list[i]] == 2:
# 			two_pept_vars = [[j, acid_count - j] for j in range(acid_count + 1)]
# 			variants.append(two_pept_vars)
# 		else:
# 			variants.append([[acid_count]])
# 	return (chain(*variant) for variant in product(*variants))


# def count_combinations(peptide_variants):
# 	totalcount = 0
# 	for peptide_variant in peptide_variants:
# 		for variant in renorm_peptides(peptide_variant):
# 			summ = factorial(sum(variant))
# 			factorials = (factorial(el) for el in variant)
# 			mult = reduce(mul, factorials, 1)
# 			totalcount += summ / mult
# 	return totalcount
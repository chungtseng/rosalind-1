import sys
import os
import re
import json
from Bio import SeqIO
from Bio.Seq import Seq

def main(path):
	print 'dndsratio.py is running'
	os.chdir(path)
	json_list = []
	file_list = os.listdir(os.getcwd())
	for file_ in file_list:
		if re.search('(^nonsyn|^syn).+json$',file_) != None:
			json_list.append(file_)
	syn_snps = {}
	nonsyn_snps = {}
	for entry in json_list:
		f = open(entry,'r')
		buff = json.loads(f.read())
		snps = []
		for el in buff:
			snps.append(tuple(el))
		name = re.search('(^nonsyn|^syn)\.?(.+)\.json$',entry)
		if name.group(1) == 'nonsyn':
			nonsyn_snps[name.group(2)] = set(snps)
		else:
			syn_snps[name.group(2)] = set(snps)

	dnds = {}
	S_matches = {}
	N_matches = {}
	for key in syn_snps.keys():
		S = len(syn_snps[key])
		N = len(nonsyn_snps[key])
		dnds[key] = [N,S,float(N)/float(S)]
		S_matches[key] = []
		N_matches[key] = []
		for key2 in syn_snps.keys():
			S_matches[key].append(len(syn_snps[key] & syn_snps[key2]))
			N_matches[key].append(len(nonsyn_snps[key] & nonsyn_snps[key2]))

	print ('Writing output files')
	dnds_f = open('dnds.csv','w')
	dnds_f.write('\t'.join(['Name','N','S','dn/ds'])+'\n')
	N_matches_f = open('nonsyn_matches.csv','w')
	N_matches_f.write('\t'.join(['Name']+nonsyn_snps.keys())+'\n')	
	S_matches_f = open('syn_matches.csv','w')
	S_matches_f.write('\t'.join(['Name']+syn_snps.keys())+'\n')	


	for key in syn_snps.keys():
		dnds_f.write('\t'.join(map(str,dnds[key]))+'\n')
		N_matches_f.write('\t'.join(map(str,[key] + N_matches[key]))+'\n')
		S_matches_f.write('\t'.join(map(str,[key] + S_matches[key]))+'\n')
	
	N_matches_f.close()
	S_matches_f.close()
	dnds_f.close()


if __name__ == '__main__': 
	if (len(sys.argv) < 2):
		print 'usage:\tdnds.py <json snp directory>'
		sys.exit(0)
	else:
		main(sys.argv[1])
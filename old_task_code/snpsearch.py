import sys
import os
import re
import json
from Bio import SeqIO
from Bio.Seq import Seq


def main(fasta,path):
	os.chdir(path)
	json_list = []
	file_list = os.listdir(os.getcwd())
	for file_ in file_list:
		if file_[-4:] == 'json':
			json_list.append(file_)
			print file_
	print json_list
	fasta_dict = SeqIO.index(fasta,'fasta')
	print ('fasta index done')
	for json_file in json_list:
		f = open(json_file,'r')
		snps = json.loads(f.read())
		syn_pol = []
		nonsyn_pol = []
		all_snps = []
		for snp in snps:
			pos = int(snp[1]) // 3 - (int(snp[1])%3 == 0)
			num = int(snp[1]) - pos*3 - 1
			#print num, snp[1],pos
			refseq = str(fasta_dict[snp[0]][pos:pos+3].seq)
			snpseq = list(refseq)
			snpseq[num] = snp[3]
			snpseq = ''.join(snpseq)
			refp = str(Seq(refseq).translate())
			snpp = str(Seq(snpseq).translate())
			all_snps.append([snp[0],snp[1],refp,snpp,snp[2],snp[3]])
			if refp == snpp:
				syn_pol.append([snp[0],snp[1],refp,snpp])
			else:
				nonsyn_pol.append([snp[0],snp[1],refp,snpp])
		f.close()

		syn_f = open('syn'+json_file,'w')
		nonsyn_f = open('nonsyn'+json_file,'w')
		syn_f.write(json.dumps(syn_pol))
		nonsyn_f.write(json.dumps(nonsyn_pol))
		syn_f.close()
		nonsyn_f.close()


		syn_f_csv = open('syn' + json_file[:-5] + '.csv','w')
		nonsyn_f_csv = open('nonsyn' +json_file[:-5] + '.csv','w')
		for row in syn_pol:
			syn_f_csv.write(' '.join(map(str,row))+'\n')
		syn_f_csv.close()
		for row in nonsyn_pol:
			nonsyn_f_csv.write(' '.join(map(str,row))+'\n')
		nonsyn_f_csv.close()
		all_snps_f = open('all_snps_'+json_file[:-5]+'.csv','w')
		for row in all_snps:
			all_snps_f.write(' '.join(map(str,row))+'\n')
		all_snps_f.close()




if __name__ == '__main__':
	path = ''
	if (len(sys.argv) < 2):
		print 'usage:\tsnpsearch.py <fasta file> <vcf directory>'
		sys.exit(0)
	else:
		if (len(sys.argv) >= 3):
			path = sys.argv[2]
		main(sys.argv[1],path)
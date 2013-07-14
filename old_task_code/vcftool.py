import sys
import os
import re
import json

def main(path):
	os.chdir(path)
	vcf_list = os.listdir(os.getcwd())
	buff = vcf_list
	for file_ in vcf_list:
		if file_[-3:] != 'vcf':
			buff.remove(file_)
	vcf_list = buff
	print vcf_list
	print '______'

	for file_ in vcf_list:
		header =[]
		table = []
		f = open(file_,'r')
		data = f.readlines()
		for line in data:
			if line[0] == '#':
				header.append(line)
			else:
				m = re.match(r'(\w+)\t(\d+)\t.\t(\w+)\t(\w+)\t',line)
				if m!=None:
					table.append(m.groups())
		f.close()
		f_output = open(file_[:-4]+'.json','w')
		f_output.write(json.dumps(table))
		f_output.close()

if __name__ == '__main__':
	path = ''
	if (len(sys.argv) < 2):
		print 'usage:\tvcftool.py <vcf path>'
		sys.exit(0)
	else:
		main(sys.argv[1])
		
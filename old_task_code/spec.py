import sys
import os
import string


def main(filename):

	mf = open('masses.txt','r')
	mass_table = {}
	for line in mf:
		row = line.split()
		mass_table[round(float(row[1]),3)] = row[0]
	#four decimal precision
	f = open(filename,'r')
	data = []
	for line in f:
		data.append(float(line.strip('\n\r')))
	data = sorted(data,reverse=True)
	M = data[0]
	print M
	data = data[1:]
	pairs = zip(*[data,data[::-1]])[:len(data)/2]
	i = 0
	diffs = []
	c = 0
	L = len(pairs)
	result = []
	while len(pairs) > 1:
		c +=1
		diff = round(pairs[0][0]-pairs[1][0],3)
		if diff in mass_table:
			diffs.append(diff)
			del pairs[0]
		else:
			pairs[1] = pairs[1][::-1]
			pairs = sorted(pairs,reverse=True)
		if c>10000:
			break
	protein =  [mass_table[m] for m in diffs]
	print len(protein)
	print ''.join(protein)
	f = open('new'+filename,'w')
	f.write(''.join(protein))

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\ttranslate.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])
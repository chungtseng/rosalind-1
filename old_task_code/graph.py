import sys
import re
import math

def fastaread(handler):
	f = open(handler,'r')
	seq = ''
	data = {}
	for line in f:
		if line[0] == '>':
			name = line[1:].rstrip('\n\r')
			seq = ''
			data[name] = seq
		else:
			data[name] = data[name] + line.rstrip('\n\r')
	f.close()
	return data

def main(handler):
	data = fastaread(handler)
	starts = []
	ends = []
	overlaps = []
	for key in data.keys():
		starts.append((key,data[key][:3]))
		ends.append((key,data[key][-3:]))
	print ends
	f = open('new'+handler,'w')
	for end in ends:
		for start in starts:
			if end[1] == start[1] and end[0]!=start[0]:
				overlaps.append((end[0],start[0]))
				f.write(end[0] + ' ' + start[0] + '\n')
	f.close()

if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tgraph.py <fasta file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


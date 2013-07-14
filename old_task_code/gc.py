import sys
import re
import math


def main(handler):
	f = open(handler,'r')
	seq = ''
	data = {}
	for line in f:
		if line[0] == '>':
			name = line[1:-1]
			seq = ''
			data[name] = seq
		else:
			data[name] = data[name] + line.rstrip('\n\r')

	for key in data.keys():
		GC = float(len(re.findall('[GC]',data[key])))
		Len = float(len(data[key]))
		k = GC/Len*100
		data[key]=[k]
	M = max(data.values())
	print(data)
	for key in data.keys():
		if data[key] == M:
			print u'%s\n%4.2f%s' % (key, M[0],'%') 
	
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


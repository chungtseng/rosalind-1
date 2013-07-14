import os
import re
import sys



def basecounter(string,pattern,N):
	indexes = []
	for item in re.finditer(pattern,string):
		indexes.append(item.start())
	for i in indexes:
		counts[N][i] += 1


def main(filename):
	f = open(filename,'r')
	f_out = open('new'+filename,'w')
	string = f.readline().strip('\n\r')
	motif = f.readline().strip('\n\r')
	positions = []
	i = 0
	for num, letter in enumerate(string):
		if letter == motif[i]:
			positions.append(num+1)
			i += 1
		if i == len(motif):
			break
	f_out.write(' '.join(map(str,positions)))
	f.close()
	f_out.close()





if __name__ == '__main__':
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])

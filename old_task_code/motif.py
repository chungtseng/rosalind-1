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
	text = f.readlines()
	length = len(text[0].strip('\r\n'))
	global counts
	counts = [[0]*length for _ in range(4)]
	letters = ['A','C','G','T']
	for line in text:
		line = line.strip('\r\n')
		for letter in letters:
			basecounter(line,letter,letters.index(letter))
	
	tr = zip(*counts)
	consensus = ''
	counts_d = {}
	for i in range(length):
		letter_index = tr[i].index(max(tr[i]))
		consensus+=letters[letter_index]
	f_out.write(consensus+'\n')
	for i in range(4):
		#print '%s:' % letters[i],' '.join(map(str,counts[i][:]))
		s = letters[i]+ ': ' + ' '.join(map(str,counts[i][:]))
		f_out.write(s+'\n')





if __name__ == '__main__':
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])

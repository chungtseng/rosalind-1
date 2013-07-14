import sys
import re
import math




def distance(str1,str2):
	indicator = 0
	for i in range(min(len(str1),len(str2))):
		if (alphabet.index(str1[i]) > alphabet.index(str2[i])):
			indicator = 1
			break
		if (alphabet.index(str1[i]) < alphabet.index(str2[i])):
			indicator = -1
			break
	if indicator == 0:
		if len(str1)>len(str2):
			indicator = 1
		else:
			indicator = -1
	return indicator


def lexis(index,alphabet):
	newlist = []
	for letter in alphabet:
		if index > 1:
			for subs in lexis(index-1,alphabet):
				newlist.append(letter+subs)
		else:
			newlist.append(letter)
	return(newlist)

def main(handler):
	f = open(handler,'r')
	global alphabet
	alphabet = f.readline().strip('\n\r').split()
	num = int(f.readline().strip('\n\r'))
	kmers = []
	for i in range(1,num+1):
		kmers += lexis(i, alphabet)
	kmers = sorted(kmers, cmp = distance)
	print kmers
	f.close()
	f = open('new'+handler,'w')
	for kmer in kmers:
		f.write(kmer+'\n')

	#for in range(1,num+1):
	
	#print(data)
	#for key in data.keys():
	#	if data[key] == M:
	#		print u'%s\n%4.2f%s' % (key, M[0],'%') 
	
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


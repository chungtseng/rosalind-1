import sys
import re
import math
from itertools import groupby
from math import fabs

def union_(set1, set2):
	set3 = []
	for el in set1:
		if not(el in set2):
			set3.append(el)
	set3+= set2
	return sorted(set3)

def inter_(set1, set2):
	set3 = []
	for el in set1:
		if el in set2:
			set3.append(el)
	return sorted(set3)



def main(filename):
	#for in range(1,num+1):
	f = open(filename,'r')
	#num = int(f.readline().strip('\n\r'))
	#U = range(1,num+1)
	Set1 =map(float,f.readline().strip('{}\n\r').split())
	Set2 = map(float,f.readline().strip('{}\n\r').split())
	minkowski_diff = []
	for el in Set1:
		minkowski_diff += map(lambda x: fabs(round(x,4)), map(lambda x: x -el, Set2))
	minkowski_diff = sorted(minkowski_diff)
	#minkowski_dict = {key: len(list(group)) for (key,group) in groupby minkowski_diff}
	minkowski = [(key,len(list(group))) for key,group in groupby(minkowski_diff)]

	minkowski = sorted(minkowski,key = lambda x: x[1],reverse=True)
	print minkowski[0]
	#print set1
	#print set2


	# f = open('output.txt','w')
	# f.write('{'+', '.join(map(str,union_(Set1,Set2)))+'}\n')
	# f.write('{'+', '.join(map(str,inter_(Set1,Set2)))+'}\n')
	# f.write('{'+', '.join(map(str,subt_(Set1,Set2)))+'}\n')
	# f.write('{'+', '.join(map(str,subt_(Set2,Set1)))+'}\n')
	# f.write('{'+', '.join(map(str,subt_(U,Set1)))+'}\n')
	# f.write('{'+', '.join(map(str,subt_(U,Set2)))+'}\n')
	# #print(' '.join(map('{:.3f}'.format,cc)))
	#f.close() 
	
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


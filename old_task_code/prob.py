import sys
import re
import math


def permute(List, num):
	set_array = []
	for i, element in enumerate(List):
		if i != len(List):	
			short_List = List[i+1:]
		else:
			break	
		if num-1 != 0:
			part_List = permute(short_List,num-1)
			for subset in part_List:
				set_array.append([element] + subset)
		else:
			set_array.append([element])
	return set_array


def main(filename):
	#for in range(1,num+1):
	f = open(filename,'r')
	probabs = map(float,f.readline().strip('\n\r').split())
	cc = []
	for prob in probabs:
		p = 2*(prob/2)**2 + 2*(0.5 - prob/2)**2
		cc.append(round(p,3))
	f.close()
	f = open('output.txt','w')
	f.write(' '.join(map('{:.3f}'.format,cc)))
	print(' '.join(map('{:.3f}'.format,cc)))
	f.close() 
	
if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\treverse_complement.py <sequence file>'
		sys.exit(0)
	else:
		main(sys.argv[1])


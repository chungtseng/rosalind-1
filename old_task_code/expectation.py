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
	nums = map(int,f.readline().strip('\n\r').split())
	print nums
	probabs = map(float,f.readline().strip('\n\r').split())
	cc = []
	for prob in probabs:
		p = prob/2
		print p
		pw = nums[0]*2
		ev = (nums[1]-nums[0]+1)*(2*p**2+2*(0.5-p)**2)**nums[0]
		print ev
		cc.append(ev)
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


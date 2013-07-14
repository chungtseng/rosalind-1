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

def main(num):
	#for in range(1,num+1):
	L = range(1,int(num)+1)

	res = []
	for i in range(1,int(num)+1):
		res+= permute(L,i)
	f = open('output.txt','w')
	f.write(str(2^(int(num)+1))+'\n')
	f.write('{}\n')
	for el in res:
		f.write('{'+', '.join(map(str,el))+'}\n')
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


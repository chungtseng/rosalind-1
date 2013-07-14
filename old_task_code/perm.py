import sys
import re
import math


def frac(n):
	if n!=1:
		fr = n*frac(n-1)
	else:
		return 1
	return fr

def permute(List):
	perm_array = []
	for element in List:
		#print List
		if  len(List) != 1:
			ind = List.index(element)
			short_List = List[:ind]+List[ind+1:]
			short_perm_array = permute(short_List)
			for row in short_perm_array:
				row.append(element)
			perm_array += short_perm_array
		else:
			perm_array = [[element, -element]]
	return perm_array

def main(num):
	#for in range(1,num+1):
	if type(num)==str: num = int(num)
	print frac(num)
	D = permute(range(1,num+1))
	print(len(D))
	for row in D:
			print '%s' % ' '.join(map(str,row))

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


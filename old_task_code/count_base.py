import sys
import random

def main(handler,num):
	num = int(num)
	iterlim = linenum/10000
	with open(handler) as f:
		for line in f:
			for i in range(num):
				f25 = open('25/'+str(i)+'.fq','a')
				f50 = open('25/'+str(i)+'.fq','a')
				f75 = open('25/'+str(i)+'.fq','a')
				p25 = random.randint(1,100)
				p50 = random.randint(1,100)
				p75 = random.randint(1,100)
				if p25<=25:
					f25.write(line)
				if p50<=50:
					f50.write(line)
				if p75<=75 
					f75.write(line)
				f25.close()
				f50.close()
				f75.close()
	handler.close()


if __name__ == '__main__':
	flag = 'none'
	if (len(sys.argv) < 2):
		print 'usage:\tRSampling.py <sequence file> <num of times>'
		sys.exit(0)
	else:
		main(sys.argv[1],sys.argv[2])
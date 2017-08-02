#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
import sys
import math


def howManyDivisors(number):
	count = 0
	for i in range(1,int(math.sqrt(number))+1):
		if number % i == 0:
			count += 2
	return count

def createTriangularNumbers(highest):
	ans = []
	ans += [1]
	for i in range(1,highest+1):
		ans += [ans[i-1] + i+1]
	return ans

def extendTriangularNumbers(numbers):
	ans = numbers
	ans += [ans[-1] + len(numbers) + 1]
	return ans


def createFactors(number):
	s = set([1,2])
	s.add([2,3])
	print s

tris = [1]

ndivs = 0
count = 0



while(ndivs < 500):
	count += 1
	tris = extendTriangularNumbers(tris)
	ndivs = howManyDivisors(tris[-1])
	#print "count is ", count, "ndivs is", ndivs

print "the last element of tris that has more than 500 divs is", tris[-1]






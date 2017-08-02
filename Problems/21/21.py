# coding: utf-8 

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


import math

def findDivisors(n):
	divs = [1]
	for i in range (2,int(math.sqrt(n))):
		if (n % i == 0):
			divs += [i]
			divs += [n/i]
	return divs

def hasAmicable(A):
	B = sum(findDivisors(A))
	if (A == B):
		return None, None
	if (A == sum(findDivisors(B))):
		return A, B
	else:
		return None, None


a = []
b = []
for i in range(10000):
	A,B = hasAmicable(i)
	if (A != None):
		a += [A]
		b += [B]


print a
print sum(a)
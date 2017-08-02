#5.py
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import numpy as np

def smallest(number):
	a = []
	total = 1
	for i in range(2,number+1):
		print "\n\ni is", i
		temp = a[:]
		print "a is", a
		adding = factor(i)
		tempadding = factor(i)
		print "the factors of", i, "are", adding
		for add in tempadding:
			if add in temp:
				temp.remove(add)
				adding.remove(add)

		print "adding", adding
		print "temp", temp
		a+=adding
		print "a is now", a
	return a



def factor(n):
	PrimeFactors = []
	while (n > 1):
		token = False
		i = 2
		while (i < n+1):
			if (n%i == 0):
				n = n/i
				PrimeFactors += [i]
				i = 2
			else:
				i+=1
	return PrimeFactors

smal= smallest(20)
print smal

tot = 1
for i in smal:
	tot *= i

print tot



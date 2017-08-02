# Find the sum of all primes below 2 million.

#using 7_seive.py

import math
import sys

def seive(number):
	rootNumber = int(math.sqrt(number) + 1)
	# s = [True for x in range(number+1)] # initialize the array of numbers that we will cross off
	s = range(number + 1)
	s[0] = 0
	s[1] = 0 # 1 is not prime
	for val in xrange(2, rootNumber):
		if s[val] != 0:
				#Cross off values in table
				#Start at n*n, end at m, increment by size m.
				#set this "slice" equal to 0's.
				# eg [0,2,3,4,5,6,7,8,9,10] = > [0, 2, 3, 0, 5, 0, 7, 0, 9, 0] has 4 zeroes that have to be set
				# there are m/n total values between [0,10], but we start counting at the second occurrence of 2.
				# however, the slicing does not take into account the value at 2, so we need to add 1 more to make up for it.
			s[val*val:number + 1:val] = [0] * (number/val - val + 1) 
	return [x for x in s if x != 0]
	#return [x for x, t in enumerate(s) if s[x] == True]




def estN(numberOfPrimes):
	x = numberOfPrimes
	ans =  (x * (math.log(x) + 2))
	return ans

maxPrime = int(sys.argv[1])

primes = seive(maxPrime)


sumOfPrimes = 0

for i in primes:
	sumOfPrimes += i

print sumOfPrimes
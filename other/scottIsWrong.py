import sys
import numpy as np

def isAPrime(number):
	for i in range(2, int(np.sqrt(number))):
		if (number % i == 0):
			return False
	return True



numberOfPrimes = int(sys.argv[1])
primes = [2]

i = 2
while (len(primes) < numberOfPrimes+1):
	isPrime = True;
	thresh = primes[-1]
	for  j in primes:
		if (isPrime == False):
			break
		if (i % j == 0):
			isPrime = False
	if (isPrime == True):
		primes += [i]
		print len(primes) - 1, i
	i+=1

print primes

prim = primes[:]

for idx, p in enumerate(prim):
	if (idx > 0):
		prim[idx] = p*prim[idx - 1]

print prim


for idx, p in enumerate(prim):
	print primes[idx],(p+1), "is prime =", isAPrime(p + 1)

print isAPrime(6)




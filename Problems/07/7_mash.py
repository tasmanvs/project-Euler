#find the 10001st prime number
import sys

numberOfPrimes = int(sys.argv[1])
primes = []

i = 2
while (len(primes) < numberOfPrimes):
	isPrime = True;
	for  j in primes:
		if (isPrime == False):
			break;
		if (j**2 - 2< i):
			if (i % j == 0):
				isPrime = False
		else:
			break
	if (isPrime == True):
		primes += [i]
	i+=1

print primes[-1]




# real	0m10.000s for 10k





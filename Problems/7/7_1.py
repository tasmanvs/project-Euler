import sys

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

# real	0m13.913s

# real	2m11.293s for 30,000

# real	0m15.022s for 10k

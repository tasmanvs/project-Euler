#find the 10001st prime number
import sys

numberOfPrimes = int(sys.argv[1])
primes = [2]

i = 2
thresh = 10000
while (i < numberOfPrimes+1):
	isPrime = True;
	for  j in primes:
		if (isPrime == False):
			break;
		if (j < thresh):
			if (i % j == 0):
				thresh = i / j
				isPrime = False
		else:
			break
	if (isPrime == True):
		primes += [i]
		# print len(primes) - 1, i
		thresh = primes[-1];
	i+=1

print primes[-1]




# real	0m10.000s for 10k





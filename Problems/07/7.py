#find the 10001st prime number
import sys

numberOfPrimes = int(sys.argv[1])
primes = [2]

i = 2
while (len(primes) < numberOfPrimes+1):
	isPrime = True;
	thresh = primes[-1];
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
		print len(primes) - 1, i
	i+=1



# real	0m17.883s


# real	2m45.295s for 30k

# real	0m19.593s for 10k




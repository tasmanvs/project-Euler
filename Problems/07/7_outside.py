import math
import sys


# return a dict or a list of primes up to N
# create full prime sieve for N=10^6 in 1 sec

def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None

def estN(numberOfPrimes):
    x = numberOfPrimes
    ans =  (x * (math.log(x) + 2))
    return ans

target = int(sys.argv[1])
primes = prime_sieve(int(estN(float(target))), [])
print primes[target]

print "-The estimated value we are going up to is n = ", (estN(float(target)))
print "p has length", len(primes), "which should be more than", target
print "The value of the", str(target) + "th prime is", primes[target-1]

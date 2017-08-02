# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

import sys

def findNext(n):
	if (n%2 == 0):
		return (n/2)
	else:
		return (3*n+1)

def countTerms(n):
	count = 1
	while (n != 1):
		count += 1
		n = findNext(n)
	return count

maxTerms = 0
highestI = 0
for i in range(1,1000001):
	print i, "/", 1000000
	terms = countTerms(i)
	if (terms > maxTerms):
		maxTerms = terms
		highestI = i

print highestI, "had ", maxTerms, "terms."
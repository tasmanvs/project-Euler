import math

def findDivs(n):
	divs = [1]
	for i in range(2,int(math.sqrt(n) + 1)):
		if (n % i == 0):
			if (i != int(n/i)):
				divs += [i, int(n/i)]
			else:
				divs += [i]
	return divs

def isAbundant(n):
	sums = sum(findDivs(n))
	print sums
	print n
	return (sums > n)

def createAbundantsUpTo(n):
	abuns = []
	for i in range(1,n):
		if isAbundant(i):
			abuns += [i]
	return abuns

def sumExists(n, arry):
	sub = [n - a for a in arry]
	subsetty = set(sub)

	for a in arry:
		if a in subsetty and n - a in subsetty: # if a exists and n - a exist, then we can make a + n - a = n.
			return True
	return False


abuns = createAbundantsUpTo(28123)


total = 0
for i in range(28123 + 100):
	print str(i) + "/" + str(28123)
	if (sumExists(i, abuns) == False):
		total += i

print total



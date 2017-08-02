
def myFunc(b):
	b = float(b)
	numerator = 2000*b - 1000**2
	denominator = 2*b-2000
	return (numerator/denominator)

for i in range (1000):
	if (myFunc(i) % 1 == 0):
		if (i > 0 and myFunc(i) > 0 and 1000 - i - myFunc(i) > 0):
			print "The values are", i, myFunc(i), 1000 - i - myFunc(i)
			print "The product of these are", i * (myFunc(i)) *(1000 - i - myFunc(i))
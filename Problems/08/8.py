import sys

# The four adjacent digits in the 1000 digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000 digit number that have the greatest product. What is the value of this product?

# python 8.py 8_source.py 13



data = open(sys.argv[1], 'r').read()

intdata = []

for i in data:
	if i in str(range(10)):
		intdata += [int(i)]

adj = int(sys.argv[2])

maxProd = 0

for idx, i in enumerate(intdata):
	prod = 1
	if (idx + adj < len(intdata)):
		for j in range(adj):
			prod *= intdata[idx+j]
	if (prod > maxProd):
		maxProd = prod

print maxProd

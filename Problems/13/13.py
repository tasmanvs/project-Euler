# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# see 13_data.txt
import numpy as np

data = np.genfromtxt("13_data.txt")
print data

sum = 0

for item in data:
	sum += item

print sum
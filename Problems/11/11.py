import sys
import numpy as np

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

np.set_printoptions(linewidth = 125)

raw = np.genfromtxt("11_data.txt")

largestProd = 0
largest = []

for idx, row in enumerate(raw):
	prod = 1
	s = []
	# find the longest in the row:
	for j in range(4):
		if (idx + j < row.size):
			prod *= row[idx+j]
			s += [row[idx + j]]
	if (prod > largestProd):
		largestProd = prod
		largest = s
	# find the longest in the column
t = np.transpose(raw)
print t
for idx, row in enumerate(t):
	prod = 1
	s = []
	# find the longest in the row:
	for j in range(4):
		if (idx + j < row.size):
			prod *= row[idx+j]
			s += [row[idx + j]]
	if (prod > largestProd):
		largestProd = prod

rightDiags = []

for idxR, row in enumerate(raw):
	for idxE, ele, in enumerate(row):
		prod = 1
		s = []
		for i in range(4):
			if (idxR + 3 < raw.shape[0] and (idxE + 3 < raw.shape[1])):
				prod *= raw[idxR+i][idxE+i]
				s += [raw[idxR+i][idxE+i]]
		if (prod > largestProd):
			largestProd = prod
			largest = s

for idxR, row in enumerate(raw):
	for idxE, ele, in enumerate(row):
		prod = 1
		s = []
		for i in range(4):
			if (idxR + 3 < raw.shape[0] and (idxE - 3 < raw.shape[1])):
				prod *= raw[idxR+i][idxE-i]
				s += [raw[idxR+i][idxE-i]]
		if (prod > largestProd):
			largestProd = prod
			largest = s



print largestProd
print largest

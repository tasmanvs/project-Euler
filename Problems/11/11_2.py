import sys
import numpy as np

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

np.set_printoptions(linewidth = 125)

raw = np.genfromtxt("11_data.txt")

print "raw is\n", raw

rawList = raw.tolist()
rows_plus_cols = raw.shape[0] + raw.shape[1]
values = []

print "number of rows is", raw.shape[0]
print "number of cols is", raw.shape[1]




# values going down and right
for j in range(rows_plus_cols):
	diag = []
	row = 0
	col = j
	while (col >= 0):
		if (row < raw.shape[0] and col < raw.shape[1]):
			diag += [raw[row][col]]
			print row, col
		row += 1
		col -= 1
	if (diag):
		values += [diag]



#values going down and left
#everything above diag:
for j in range(rows_plus_cols):
	diag = []
	row = j
	col = 0
	while (row <= raw.shape[0]):
		if (row < raw.shape[0] and col < raw.shape[1]):
			diag += [raw[row][col]]
			print row, col
		row += 1
		col += 1
	if (diag):
		values += [diag]

#everything below diag
for j in range(rows_plus_cols):
	diag = []
	row = 0
	col = j
	while (row <= raw.shape[0]):
		if (row < raw.shape[0] and col < raw.shape[1]):
			diag += [raw[row][col]]
			print row, col
		row += 1
		col += 1
	if (diag):
		values += [diag]

for row in raw:
	values += [row.tolist()]
for row in np.transpose(raw):
	values += [row.tolist()]
print values

maxProd = 0
for val in values:
	for idx, number in enumerate(val):
		prod = 1
		for i in range(4):
			if (idx + i < len(val)):
				prod *= val[idx + i]
		if (prod > maxProd):
			maxProd = prod

print "maxprod is", maxProd
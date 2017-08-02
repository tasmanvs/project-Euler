import sys
import numpy as np

data = open("18_data.txt","r") 

# values = data.read()

data_table = [[0,0,0]]



for line in data:
	chars = [0]
	chars += line.strip('\n').split(' ')
	chars += [0]
	chars = [int(c) for c in chars]
	data_table += [chars]

for line in data_table:
	print line

dimension = len(data_table[-1])
print "dimension is", dimension

sum_table = list(data_table)


for i in range(dimension-1):
	for j in range(i+1):

		sum_table[i][j] = max(sum_table[i-1][j-1], sum_table[i-1][j]) + sum_table[i][j]

for s in sum_table:
	print s
	
print "THE MAX IS", max(sum_table[-1])


# coding: utf-8 

# Using names.txt (right click and 'Save Link/Target As...'), 
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working 
# out the alphabetical value for each name, multiply this 
# value by its alphabetical position in the list to obtain a
# name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

import random

#Read the files into a list of strings, return a list with the quotes removed.
def extractNames(filename):
	File = open(filename, "r")
	Data = [name.split(',') for name in File]
	Data = [name.strip('/"') for name in Data[0]]
	return Data

#Moves elements in Data to be in sorted order. In place.
def quickSortHelper(Data, start, end):

	if (end - start > 0): #if there exists some element in the array, try to sort it
		pivot = start + random.randrange(end - start) #set pivot to random value
		pivotVal = Data[pivot] #acquire pivot value that we will compare to later
		left = start # left cursor starts at the left
		right = end

		while (right != pivot or left != pivot):

			while(Data[left] <= pivotVal and left < pivot): #while the Data[left] in the correct place, move it
				left += 1

			while(Data[right] >= pivotVal and right > pivot):
				right -= 1

			if (pivot == left):
				pivot = right
			elif (pivot == right):
				pivot = left

			Data[left], Data[right] = Data[right], Data[left]
		quickSortHelper(Data, pivot + 1, end)
		quickSortHelper(Data, start, pivot - 1)

#Wrapper for quicksort. Starts and ends at the appropriate locations
def quickSort(Data):
	quickSortHelper(Data, 0, len(Data) - 1)






# numEle = 100
# dat = [random.randrange(-numEle, numEle) for i in range(numEle)]
# dat = extractNames("p022_names.txt")
# quickSort(dat)
# print dat



total = 0
# for idx, name in enumerate(dat):
# 	for char in name:



# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 
import numpy as np

highest = 0 

number = 600851475143

highest_prime = 0


Token = True

count = 0

while (Token == True):
	Token = False
	for i in range (int(np.sqrt(number)) + 10):
		count += 1
		if (number % (i+2) == 0):
			number = number/(i+2)
			Token = True
			print (i+2)
			print "number is", number
			break 








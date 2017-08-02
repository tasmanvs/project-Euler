#6.py
sumOfSquares = 0
squareOfSums = 0

number = 100

for i in range(1, number + 1):
	sumOfSquares += i*i
	squareOfSums += i
squareOfSums*=squareOfSums

print squareOfSums, sumOfSquares

print squareOfSums - sumOfSquares

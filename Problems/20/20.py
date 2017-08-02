def fact(n):
	if (n == 1 or n == 0):
		return 1
	else:
	 return (n * fact(n-1))

s = str(fact(100))

print s

total = 0

for char in s:
	total += int(char)

print total
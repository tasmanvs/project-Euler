# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
	end = len(number) - 1
	start = 0
	pal = True
	while(start < end):
		if (number[start] != number[end]):
			pal = False
		start += 1
		end -= 1
	return pal

print isPalindrome("")

maxPal = 0
number = 10

for i in range(number,0,-1):
	for k in range(i, 0, -1):
		if (isPalindrome(str(i*k)) and (i*k > maxPal)):
			maxPal = (i*k)

print  "Tasmans implement", maxPal
count = 0
for A in range(number,0,-1):
	if (isPalindrome(str(A**2))):
		print (A**2), A
		break
	count += 1
	for j in range(count):
		print "this is", (A**2 - (1+2*j))
		if isPalindrome(str(A**2 - (1+2j))):
			print (A**2 - (1+2j)), A, j

print (str(95**2 - (2*8)))

print "is pal", isPalindrome(str(99))



s = range(100)


#factor out all the twos

print s

n = 3
m = len(s)
i = 6
s[n*n:m:n] = [0] * (m/n - n + 1)

print s


# m = n/i - i
# sieve[i*i: n+1:i] = [0] * (m+1)
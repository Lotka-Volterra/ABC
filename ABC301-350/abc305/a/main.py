n = int(input())
nmod = n % 5
if nmod < 5 - nmod:
    print(n - nmod)
else:
    print(n + 5 - nmod)

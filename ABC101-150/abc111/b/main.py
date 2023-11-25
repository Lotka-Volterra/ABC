n = int(input())
nmod = n % 111
if nmod==0:
    print(n)
else:
    print(n + (111-nmod))

s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
sstr = ''.join(s)
tstr = ''.join(t)
if sstr < tstr:
    print('Yes')
else:
    print('No')

s = input()
smax = s
smin = s
for i in range(len(s)):
    s = s[1:] + s[0]
    smax = max(s, smax)
    smin = min(s, smin)
print(smin)
print(smax)

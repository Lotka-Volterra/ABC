n = int(input())
s = input()
for i in range(1, n):
    maxl = 0
    for l in range(n - i):
        if s[l] != s[l + i]:
            maxl = l + 1
        else:
            break
    print(maxl)

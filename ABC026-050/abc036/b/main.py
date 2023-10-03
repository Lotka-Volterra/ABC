n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)
for i in range(n):
    ans = ""
    for j in range(n):
        ans += s[n - 1 - j][i]
    print(ans)

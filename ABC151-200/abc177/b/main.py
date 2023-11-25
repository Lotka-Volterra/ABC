s = input()
t = input()
ans = float("inf")
for i in range(len(s) - len(t) + 1):
    sliceS = s[i : i + len(t)]
    count = 0
    for j in range(len(t)):
        if sliceS[j] != t[j]:
            count += 1
    ans = min(ans, count)
print(ans)

n = int(input())
s = input()
ans = 0
for i in range(1, n - 1):
    left = s[:i]
    right = s[i:]
    common = []
    for j in range(len(left)):
        if left[j] in right:
            common.append(left[j])
    ans = max(ans, len(list(set(common))))
print(ans)
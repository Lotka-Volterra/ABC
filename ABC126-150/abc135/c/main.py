n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    bi = b[i]
    if bi >= a[i]:
        ans += a[i]
        bi -= a[i]
        ans += min(a[i + 1], bi)
        a[i + 1] -= min(a[i + 1], bi)
    else:
        ans += bi
print(ans)

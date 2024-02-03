n, k = map(int, input().split())
a = list(map(int, input().split()))
dict = {}
for i in range(n):
    if a[i] in dict:
        dict[a[i]] += 1
    else:
        dict[a[i]] = 1
values = []
for i in dict.values():
    values.append(i)
values.sort()
ans = 0
for i in range(len(list(set(a))) - k):
    ans += values[i]
print(ans)

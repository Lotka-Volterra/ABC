n = int(input())
a = list(map(int, input().split()))
abs_a = []
negative_count = 0
for i in range(n):
    if a[i] < 0:
        negative_count += 1
    abs_a.append(abs(a[i]))
ans = sum(abs_a)
if negative_count % 2 == 1:
    ans -= min(abs_a) * 2
print(ans)

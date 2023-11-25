n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = -1
anstemp = 1000000
for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < anstemp:
        anstemp = abs(a - (t - h[i] * 0.006))
        ans = i+1
print(ans)

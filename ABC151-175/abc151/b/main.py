n, k, m = map(int, input().split())
a = list(map(int, input().split()))
sumA = sum(a)
goal = m * n
rest = goal - sumA
if rest > k:
    print(-1)
else:
    print(max(rest, 0))

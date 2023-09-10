n = int(input())
p = list(map(int, input().split()))
maxp = 0
# pが一人の場合を考慮
if len(p) > 1:
    maxp = max(p[1:])

if p[0] > maxp:
    print(0)
else:
    print(maxp - p[0] + 1)

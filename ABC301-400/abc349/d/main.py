import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
l, r = map(int, input().split())
ans = 0
ans_list = []
while True:
    ans += 1
    for i in range(61, -1, -1):
        if l % (2**i) == 0 and (2**i) * (l // (2**i) + 1) <= r:
            ans_list.append([l, (2**i) * (l // (2**i) + 1)])
            l = (2**i) * (l // (2**i) + 1)
            break
    if l == r:
        break
print(ans)
for i in ans_list:
    print(i[0], i[1])

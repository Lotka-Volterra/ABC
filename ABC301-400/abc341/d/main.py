import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n, m, k = map(int, input().split())
LCM = math.lcm(n, m)
shou_n = LCM // n
shou_m = LCM // m
# LCMまでの項数
kousuu = shou_m + shou_n - 2
K_shou = k // kousuu
K_amari = k % kousuu
# print(K_shou, K_amari)
if K_amari == 0:
    print(max(K_shou * LCM - n, K_shou * LCM - m))
else:
    ans = K_shou * LCM
    n_keisu = 1
    m_keisu = 1
    for i in range(K_amari):
        if n * n_keisu < m * m_keisu:
            if i == K_amari - 1:
                ans += n * n_keisu
            n_keisu += 1
        else:
            if i == K_amari - 1:
                ans += m * m_keisu
            m_keisu += 1
    print(ans)

import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
dict = defaultdict(int)
for i in s:
    dict[i] += 1
for i in range(len(s)):
    if dict[s[i]] == 1:
        print(i + 1)
        quit()

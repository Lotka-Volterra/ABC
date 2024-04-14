import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
len_s = len(s)
if s == "<" + "=" * (len_s - 2) + ">":
    print("Yes")
else:
    print("No")

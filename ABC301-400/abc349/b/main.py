import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
str_dict = defaultdict(int)
s = input()
for i in s:
    str_dict[i] += 1
for i in range(1, 101):
    count = 0
    for j in str_dict.values():
        if j == i:
            count += 1
    if count != 0 and count != 2:
        print("No")
        quit()
print("Yes")

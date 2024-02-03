import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
for i in range(len(s)):
    if i == 0:
        if s[i].islower():
            print("No")
            quit()
    else:
        if s[i].isupper():
            print("No")
            quit()
print("Yes")

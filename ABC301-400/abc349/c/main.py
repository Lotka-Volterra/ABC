import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()
s += "x"
t = input()
first = t[0].lower()
second = t[1].lower()
third = t[2].lower()
firstFlag = False
secondFlag = False
thirdFlag = False
for i in s:
    if not firstFlag:
        if i == first:
            firstFlag = True
    elif not secondFlag:
        if i == second:
            secondFlag = True
    else:
        if i == third:
            thirdFlag = True
            break
if thirdFlag:
    print("Yes")
else:
    print("No")

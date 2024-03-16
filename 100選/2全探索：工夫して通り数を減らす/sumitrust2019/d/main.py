import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n = int(input())
s = input()
count = 0
for i in range(1000):
    strI = (3 - len(str(i))) * "0" + str(i)
    firstFLag = False
    secondFlag = False
    for j in s:
        if not firstFLag and j == strI[0]:
            firstFLag = True
        elif firstFLag and not secondFlag and j == strI[1]:
            secondFlag = True
        elif secondFlag and j == strI[2]:
            count += 1
            break
print(count)

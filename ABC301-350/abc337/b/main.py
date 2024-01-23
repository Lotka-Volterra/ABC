import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
s = input()

lens = len(s)
for i in range(lens + 1):
    for j in range(lens - i + 1):
        k = lens - (i + j)
        string = "A" * i + "B" * j + "C" * k
        if s == string:
            print("Yes")
            quit()
print("No")

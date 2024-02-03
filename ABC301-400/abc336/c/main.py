import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)


def toNBase(integer, base):
    answerString = ""
    # integerが0より大きい間
    while integer:
        answerString = str(integer % base) + answerString
        integer //= base
    return answerString


n = int(input())
ansStr = toNBase(n - 1, 5)
ans = ""
# print(ansStr)
if n == 1:
    print(0)
    quit()
base = ["0", "2", "4", "6", "8"]
for i in range(len(ansStr)):
    if ansStr[i] == "0":
        ans += "0"
    else:
        ans += base[int(ansStr[i])]
print(ans)

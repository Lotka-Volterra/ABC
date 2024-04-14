import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
ans = []
while True:
    try:
        s = int(input())
    except EOFError:
        break
    ans.append(s)
ans.reverse()
for i in ans:
    print(i)

# 問題文ちゃんと読んでなかった
# 最後は0が来ることは確定しているので、エラーキャッチの実装までは不要

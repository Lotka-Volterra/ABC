from collections import defaultdict

n = int(input())
rdict = defaultdict(lambda: 10**9 + 1)
ldict = defaultdict(lambda: -1)
numset = set()
# 衝突が起きるのは、下記をすべて満たす場合
# y座標が同じで、LとRの組み合わせがある
# Lのx座標がRのx座標より大きい
xy = [list(map(int, input().split())) for i in range(n)]
s = input()
for i in range(n):
    if s[i] == "L":
        ldict[xy[i][1]] = max(ldict[xy[i][1]], xy[i][0])
    else:
        rdict[xy[i][1]] = min(rdict[xy[i][1]], xy[i][0])
    numset.add(xy[i][1])
# print(rdict)
# print(ldict)
for i in numset:
    if rdict[i] != 10**9 + 1 and ldict[i] != -1:
        if ldict[i] > rdict[i]:
            print("Yes")
            quit()
print("No")

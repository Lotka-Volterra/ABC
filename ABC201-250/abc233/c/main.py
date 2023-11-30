# from functools import lru_cache

# !!!!PyPyは再帰関数の実行速度が遅いことがあり、Python3でまず試してみる!!!!
# 再帰呼び出しの深さの上限を 10**6 に設定、設定を上げておかないと途中で再帰呼び出しを切り上げてREになる
import sys

sys.setrecursionlimit(10**6)

count = 0


# 深さ優先探索の再帰関数
# メモ化再帰　再帰関数の呼び出し時に、同じ引数の再帰関数が呼ばれる場合に備えて計算結果をメモしておく、Windowsでは落ちるので使わない
# @lru_cache(maxsize=None)
def depthFirstSearch(position, adjacencyList, seki):
    global count
    if position == n:
        if seki == x:
            return True
        return False
    for i in adjacencyList[position]:
        # 隣接した頂点が未踏の場合、その頂点へ行く（再帰）
        if depthFirstSearch(position + 1, adjacencyList, seki * i):
            count += 1
    # 一つ前の頂点に戻る
    return False


n, x = map(int, input().split())
A = []
L = []
for i in range(n):
    l, *a = map(int, input().split())
    A.append(a)
    L.append(l)

depthFirstSearch(0, A, 1)
print(count)

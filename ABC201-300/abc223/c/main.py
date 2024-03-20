def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    # return 条件式(arg)
    # pass
    return ans_time < time_list[arg]


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
time = 0
time_list = [0]
cm = 0
cm_list = [0]
for i in range(n):
    time += A[i] / B[i]
    time_list.append(time)
    cm += A[i]
    cm_list.append(cm)
ans_time = time / 2
ind = meguru_bisect(0, n)
# print(ans_time)
# print(ind)
# print(time_list)
# print(cm_list)
# print(A)
# print(B)
print(cm_list[ind - 1] + (B[ind - 1]) * (ans_time - time_list[ind - 1]))

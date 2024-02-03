def is_ok_left(arg, target_list, a_value):
    # 条件を満たすかどうか？問題ごとに定義
    return target_list[arg] >= a_value


def meguru_bisect_left(ng, ok, target_list, a_value):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok_left(mid, target_list, a_value):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok_right(arg, target_list, a_value):
    # 条件を満たすかどうか？問題ごとに定義
    return target_list[arg] > a_value


def meguru_bisect_right(ng, ok, target_list, a_value):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok_right(mid, target_list, a_value):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0
for b_i in range(n):
    if a[0] >= b[b_i] or c[-1] <= b[b_i]:
        continue
    a_i = meguru_bisect_left(-1, n, a, b[b_i])

    c_i = meguru_bisect_right(-1, n, c, b[b_i])
    # print(a_i, b_i, c_i)
    ans += (a_i) * (n - c_i)
print(ans)

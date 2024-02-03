def is_ok(arg, height):
    # 条件を満たすかどうか？問題ごとに定義
    # return 条件式(arg)
    return a[arg] >= height


def meguru_bisect(ng, ok, height):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, height):
            ok = mid
        else:
            ng = mid
    return ok


n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = [0] + a + [10**10]
for i in range(q):
    x = int(input())
    student = meguru_bisect(0, n + 1, x)
    print(n + 1 - student)

n, d, p = map(int, input().split())
f = list(map(int, input().split()))
# 使う費用が高い日の順にソート
f.sort(reverse=True)
ans = 0
# 日付のポインタ
i = 0
while True:
    # 日付がN日間を越えたら終了
    if i >= len(f):
        break
    # 当日からN日までD日以上あるとき
    if i + d - 1 <= len(f) - 1:
        # D日間の合計費用が周遊パスの値段より大きければ、周遊パスを買う
        if sum(f[i : i + d]) >= p:
            ans += p
        else:
            ans += sum(f[i : i + d])
        i += d
    # 当日からN日までD日未満のとき
    else:
        if sum(f[i:]) >= p:
            ans += p
        else:
            ans += sum(f[i:])
        break
print(ans)

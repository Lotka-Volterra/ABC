# 項数nの数列Anは、A1<A2<...<Anを満たす。
# xが何項目にあるかを二分探索で求める
n, x = map(int, input().split())
a = list(map(int, input().split()))
# startindexは探索範囲の始端、endindexは探索範囲の末端
start_index = 0
end_index = n - 1
# 探索範囲が存在する間、比較を続ける
while start_index <= end_index:
    # midindexは探索範囲の中央のインデックス、midAはその値
    mid_index = (end_index + start_index) // 2
    midA = a[mid_index]
    # 見つかったら何項目かを出力
    if x == midA:
        print(mid_index + 1)
        quit()
    # xがmidAより小さい場合は、探索範囲を末端側から狭める
    elif x < midA:
        end_index = mid_index - 1
    # xがmidAより大きい場合は、探索範囲を始端側から狭める
    else:
        start_index = mid_index + 1

# 項数nの数列Anは、A1<A2<...<Anを満たす。
# xが何項目にあるかを二分探索で求める
n, x = map(int, input().split())
a = list(map(int, input().split()))
# startindexは探索範囲の始端、endindexは探索範囲の末端
startindex = 0
endindex = n-1
# 探索範囲が存在する間、比較を続ける
while startindex <= endindex:
    # midindexは探索範囲の中央のインデックス、midAはその値
    midindex = (endindex+startindex)//2
    midA = a[midindex]
    # 見つかったら何項目かを出力
    if x == midA:
        print(midindex+1)
        quit()
    # xがmidAより小さい場合は、探索範囲を末端側から狭める
    elif x < midA:
        endindex = midindex-1
    # xがmidAより大きい場合は、探索範囲を始端側から狭める
    else:
        startindex = midindex+1

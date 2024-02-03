a, b = map(int, input().split())
# a==0 or b==0のときに備えて0を入れておく。
point = [0]
for i in [a, b]:
    if i == 1 or i == 2 or i == 4:
        point.append(i)
    elif i == 3:
        point += [1, 2]
    elif i == 5:
        point += [1, 4]
    elif i == 6:
        point += [2, 4]
    elif i==7:
        point += [1, 2, 4]
    # i==0のときは何もしない
point = set(point)
print(sum(point))

# 回答例
# 1,2,4は2の累乗。1,2,4は2進数で表せば各桁に対応し、その桁が1になる。
# 1から7までの数は1,2,4の和で表せる。
# aとbでORのbit演算をすれば、a,bについてどちらかに各桁に1があれば、1になる。
# 結果として1,2,4の得点があるかどうか網羅できる
a,b = map(int, input().split())
print(a|b) 

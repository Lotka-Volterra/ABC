n = int(input())
a = list(map(int, input().split()))
if len(list(set(a))) == len(a):
    print("YES")
else:
    print("NO")

# 別解：ソートを使う。
# ソートして、隣り合う要素のうちいずれか2つが同じ値ならNO、すべて異なるならYES
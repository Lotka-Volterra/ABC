a = list(map(int, input().split()))
a.sort()
print(a[0]+a[1])

# 別解。一番大きいものを求めて、a,b,cの和から引く
a = list(map(int, input().split()))
suma = sum(a)
maxa = max(a)
print(suma-maxa)

l = list(map(int, input().split()))
l.sort()
print(l[2]*10+l[1]+l[0])

#　別解、総当たり
a, b, c = map(int, input().split())
print(max(10*a, +b+c, 10*b+c+a, 10*c+a+b))

# 最大がどれかわからなくても解ける。たとえばaが最大なら10*a+b+c=9*a+a+b+cを利用
print(max(a, b, c)*9+a+b+c)

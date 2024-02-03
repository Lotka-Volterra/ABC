a = int(input())
l = []
for i in range(1, a):
    l.append(i*(a-i))
print(max(l))
#相加相乗平均より、(x+y)/2>=(x*y)^1/2より、xy<=((x+y)^2)/4
#等号成立はｘ=yのとき、つまりxy=x^2
#y=a-xより、x=a/2 今回aは偶数であることが保証されているので、x^2=(a/2)^2より、以下別解
x=a//2
print(x**2)
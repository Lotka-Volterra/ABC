a = list(map(int, input().split()))
a.sort()
print(a[1]+a[2])

# 別解
a = list(map(int, input().split()))
print(sum(a)-min(a))

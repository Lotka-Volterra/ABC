a = list(map(int, input().split()))
a.sort()
print(abs(a[0]-a[1])+abs(a[1]-a[2]))

# sortしてるので、大小は分かってる。abs使う必要ない。
# (a[1]-a[0])+(a[2]-a[1])=a[2]-a[0]=max(a)-min(a)

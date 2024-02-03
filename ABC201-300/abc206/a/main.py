n= int(input())
teika=int(n*1.08)
ans=''
if teika>206:
    ans=':( '
elif teika==206:
    ans='so-so'
else:
    ans='Yay!'
print(ans)

#精度問題を意識すると、整数の計算で完結させるのが良い。1.08=108/100
teika=n*108//100
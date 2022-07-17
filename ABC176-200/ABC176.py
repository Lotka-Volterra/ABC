n,x,t = list(map(int,input().split()))

shou = n//x
if n%x == 0:
    time = shou*t

else:
    time = (shou + 1)*t
print(time)
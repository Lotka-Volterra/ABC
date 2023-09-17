a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
st = s+t
total = a*s+b*t
if st >= k:
    print(total-c*st)
else:
    print(total)

#別解　s+t>=kは１か０の値を取る
a,b,c,k=map(int,input().split())
s,t=map(int,input().split())
print(s*a+b*t-c*(s+t)*(s+t>=k))
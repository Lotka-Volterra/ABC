s=input()
t=input()
sl=len(s)
tl=len(t)
if tl==sl+1 and t[:sl]==s:
    print("Yes")
else:
    print("No")
#問題文の条件からtl==sl+1は保証されているので、t[:sl]==sだけ調べればいい
#別解。末尾の一つ前までは:−1
if s==t[:-1]:
    print("Yes")
else:
    print("No")
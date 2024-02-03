n,x = map(int,input().split())
print(min(abs(n-x),x-1))
# n>=xなので、absは必要ない
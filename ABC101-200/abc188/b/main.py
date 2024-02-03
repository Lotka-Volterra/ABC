n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
naiseki = 0
for i in range(n):
    naiseki += a[i] * b[i]
print("Yes" if naiseki == 0 else "No")

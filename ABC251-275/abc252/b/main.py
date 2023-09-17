n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
om = max(a)
for i in range(k):
    if a[b[i]-1] == om:
        print("Yes")
        quit()
print("No")

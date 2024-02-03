n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = "No"
for i in range(n):
    for j in range(n):
        if a[i] - a[j] == x:
            print("Yes")
            quit()
print("No")

n, k = map(int, input().split())
snuke = [0] * n
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        snuke[a[j] - 1] = 1
ans = 0
for i in range(n):
    if snuke[i] == 0:
        ans += 1
print(ans)

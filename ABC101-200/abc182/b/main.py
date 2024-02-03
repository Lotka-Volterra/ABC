n = int(input())
a = list(map(int, input().split()))
gcdd = 0
ans = 0
for i in range(2, max(a) + 1):
    gcddi = 0
    for j in range(n):
        if a[j] % i == 0:
            gcddi += 1
    if gcddi > gcdd:
        gcdd = gcddi
        ans = i
print(ans)

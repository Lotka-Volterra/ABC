n, k = map(int, input().split())
for i in range(1, 10000):
    if n <= k**i-1:
        print(i)
        quit()

# 別解。nを何回kで割れるか
n, k = map(int, input().split())
ans = 0
while n > 0:
    n //= k
    ans += 1
print(ans)

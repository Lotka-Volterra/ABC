n, l = map(int, input().split())
originaltaste = n * (2 * l + n - 1) // 2
diff = float("inf")
ans = 0
for i in range(1, n + 1):
    if diff > abs(l + i - 1):
        diff = abs(l + i - 1)
        ans = originaltaste - (l + i - 1)
print(ans)

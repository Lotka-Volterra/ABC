n = int(input())
a = list(map(int, input().split()))
square = a[0] ** 2
prefix_sum = [a[0]]
for i in range(1, n):
    square += a[i] ** 2
    prefix_sum.append(prefix_sum[i - 1] + a[i])
ans = 0
for i in range(1, n):
    ans += -2 * a[i] * prefix_sum[i - 1]
print(ans + square * (n - 1))
# print(square)
# print(prefix_sum)

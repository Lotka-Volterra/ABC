n = int(input())
p = list(map(int, input().split()))
q = [0] * n
for i in range(n):
    q[p[i] - 1] = i + 1
print(*q)
# 模範解答
N = int(input())
P = [0] + list(map(int, input().split()))
Q = [-1] * (N + 1)
for i in range(1, N + 1):
    Q[P[i]] = i
print(" ".join(map(str, Q[1:])))

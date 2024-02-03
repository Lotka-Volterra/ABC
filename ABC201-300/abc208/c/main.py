# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# numA = []
# for i in range(n):
#     numA.append([a[i], i])
# numA.sort()
# common = k // n
# amari = k % n
# candy = [0] * n
# for i in range(n):
#     candy[numA[i][1]] = common
#     if i < amari:
#         candy[numA[i][1]] += 1
# for i in candy:
#     print(i)
# 定数倍の良い実装
N, K = map(int, input().split())
a = list(map(int, input().split()))

order = [(a[i] << 32) + i for i in range(N)]
order.sort()
for i in range(N):
    print(format(order[i], "b"))
answer = [K // N for i in range(N)]
for i in range(K % N):
    print(format(order[i], "b"))
    print(format((1 << 32) - 1, "b"))
    answer[order[i] & ((1 << 32) - 1)] += 1
for x in answer:
    print(x)

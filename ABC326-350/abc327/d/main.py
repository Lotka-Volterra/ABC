# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# x = [2] * (n + 1)
# for i in range(m):
#     print(x)
#     if a[i] == b[i]:
#         print("No")
#         quit()
#     if x[a[i]] != 2 and x[b[i]] != 2:
#         if x[a[i]] == x[b[i]]:
#             print("No")
#             quit()
#     elif x[a[i]] != 2:
#         if x[a[i]] == 1:
#             x[b[i]] = 0
#         else:
#             x[b[i]] = 1
#     elif x[b[i]] != 2:
#         if x[b[i]] == 1:
#             x[a[i]] = 0
#         else:
#             x[a[i]] = 1
#     else:
#         x[a[i]] = 1
#         x[b[i]] = 0
# print("Yes")
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rinsetsu = [[0] * n for i in range(n)]
for i in range(m):
    if a[i] == b[i]:
        print("No")
        quit()
    rinsetsu[a[i] - 1][b[i] - 1] = 1
    rinsetsu[b[i] - 1][a[i] - 1] = 1
x = [2] * (n + 1)
ab = list(set(a + b))
# for i in ab:

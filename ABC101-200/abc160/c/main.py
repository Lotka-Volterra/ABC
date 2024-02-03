# k, n = map(int, input().split())
# house = []
# a = list(map(int, input().split()))
# for i in range(n):
#     house.append(a[i])
#     house.append(-(k - a[i]))
# house.sort()
# ans = k
# for i in range(n):
#     ans = min(ans, house[n + i - 1] - house[i])
# print(ans)
# 模範解答
# n件の家で、湖をn個の区間に分ける。
# n個の区間のうち、最大幅の区間を通らず、それ以外の区間をすべて通ればすべての家を訪れることになる
k, n = map(int, input().split())
a = list(map(int, input().split()))
kukan = []
for i in range(n - 1):
    kukan.append(a[i + 1] - a[i])
kukan.append(k - a[-1] + a[0])
print(k - max(kukan))

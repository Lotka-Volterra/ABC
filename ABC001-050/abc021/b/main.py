# 同じ街を訪問する、あるいはaあるいはbを一度以上訪れると最短ではない
n = int(input())
town = [0] * n
a, b = map(int, input().split())
town[a - 1] = 1
town[b - 1] = 1
k = int(input())
p = list(map(int, input().split()))
for i in range(k):
    town[p[i] - 1] += 1
for i in range(n):
    if town[i] > 1:
        print("NO")
        quit()
print("YES")

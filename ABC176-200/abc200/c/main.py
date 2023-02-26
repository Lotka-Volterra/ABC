n = int(input())
a = list(map(int, input().split()))
alist = [0]*200
# mod200の値のインデックスに格納。差が200の倍数＝mod200が等しい
for i in range(n):
    x = a[i] % 200
    alist[x] += 1
count = 0
for i in range(200):
    ai = alist[i]
    count += (ai * (ai - 1) )// 2
# print(alist)
print(count)

N, S, T = map(int, input().split())
W = int(input())
count = 0
WL = [W]
for i in range(1, N):
    a = int(input())
    WL.append(WL[i-1] + a)
for i in range(N):
    if WL[i] >= S and WL[i] <= T:
        count += 1
print(count)

# 書き直すなら、リストを作る必要はないので、一つの変数に体重をまとめて、入力受付と体重の判定を一つにする
N, S, T = map(int, input().split())
W = int(input())
count = 0

for i in range(N):
    if i != 0:
        a = int(input())
        W += a
    if W >= S and W <= T:
        count += 1
print(count)

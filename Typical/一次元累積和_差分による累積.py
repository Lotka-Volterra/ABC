# いもす法
# D日感続くイベントに、N人がそれぞれL日目からR日目まで参加する。各日の参加者数を出力する問題
d = int(input())
n = int(input())
# 前日比を格納するdif
# 0日目からD+1日目まで(0日目の前日比は0、D+1日目は誰も参加しない)
dif = [0]*(d+2)
# その日の客の数を前日比から計算して格納するvisitor
# 0日目からD日目まで
visitor = [0]*(d+1)

# 前日比の計算
for i in range(n):
    li, ri = map(int, input().split())
    # L日目から参加する場合、L日目の前日比に＋１。R日目まで参加する場合、R+1日目の前日比に-1
    dif[li] += 1
    dif[ri+1] -= 1
# 各日の参加者の計算
for j in range(1, d+1):
    # j日目の参加者は、前日の参加者＋j日目の前日比
    visitor[j] = visitor[j-1]+dif[j]
    print(visitor[j])

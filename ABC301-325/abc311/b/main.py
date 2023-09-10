# いもす法
n, d = map(int, input().split())

# 前日比を格納するdif
# 0日目からD+1日目まで(0日目の前日比は0、D+1日目は誰も参加しない)
dif = [0] * (d + 2)
# その日の客の数を前日比から計算して格納するvisitor
# 0日目からD日目まで
visitor = [0] * (d + 1)

# 前日比の計算
# print("difここから")
for i in range(n):
    s = input()
    s = "x" + s + "x"
    for j in range(d):
        if 0 < j < d + 1 and s[j - 1] == "x" and s[j] == "o":
            dif[j] += 1
        elif 0 < j < d + 1 and s[j - 1] == "o" and s[j] == "x":
            dif[j] -= 1
#         print(j)
#         print(dif)
# print("difここまで")
# 各日の参加者の計算
for j in range(1, d + 1):
    # j日目の参加者は、前日の参加者＋j日目の前日比
    visitor[j] = visitor[j - 1] + dif[j]
# print(visitor)
days = [0] * (d + 1)
for k in range(1, d + 1):
    if days[k - 1] == 0 and visitor[k] == n:
        days[k] = 1
    elif days[k - 1] != 0 and visitor[k] == n:
        days[k] = days[k - 1] + 1
# print(days)
print(max(days))
# TODO:途中 添え字をどうやって整合性とるか考え中

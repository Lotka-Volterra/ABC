x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
team = []
for i in [x, y]:
    if i in a:
        team.append("a")
    elif i in b:
        team.append("b")
    else:
        team.append("c")
if team[0] == team[1]:
    print("Yes")
else:
    print("No")

# 公式解答。グループに1,2,3と番号を振り、1から12についてそれが属するグループの番号をリストに格納
# インデックスで値を参照し、値が等しいかどうかを調べる
# 配列の添字は0から始まるので、その調整でlist[0]に1−3以外の数字を入れている
list = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
if list[x] == list[y]:
    print("Yes")
else:
    print("No")

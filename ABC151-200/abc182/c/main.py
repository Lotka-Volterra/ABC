n = input()
amari1 = 0
amari2 = 0
for i in n:
    if int(i) % 3 == 1:
        amari1 += 1
    elif int(i) % 3 == 2:
        amari2 += 1
totalAmari = (amari1 + amari2 * 2) % 3
ans = 0
if totalAmari == 1:
    if amari1 >= 1:
        ans = 1
    elif amari2 >= 2:
        ans = 2
    else:
        ans = -1
elif totalAmari == 2:
    # 最小から評価する。つまり、1つ除く方法と2つ除く方法がどちらも取れる場合は1つ除く方法が採用されるようにする
    if amari2 >= 1:
        ans = 1
    elif amari1 >= 2:
        ans = 2
    else:
        ans = -1
if ans == len(n):
    ans = -1
print(ans)

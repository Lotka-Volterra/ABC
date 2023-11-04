s = input()
line = [0] * 7
if s[6] == "1":
    line[0] = 1
if s[3] == "1":
    line[1] = 1
if s[1] == "1" or s[7] == "1":
    line[2] = 1
if s[4] == "1":
    line[3] = 1
if s[2] == "1" or s[8] == "1":
    line[4] = 1
if s[5] == "1":
    line[5] = 1
if s[9] == "1":
    line[6] = 1
if s[0] == "1":
    print("No")
    quit()
stand = []
lie = []
for i in range(7):
    stand.append(i) if line[i] == 1 else lie.append(i)
for i in range(len(lie)):
    if len(stand) > 0 and min(stand) < lie[i] < max(stand):
        print("Yes")
        quit()
print("No")

# ちょっとした高速化
# s[0]=="1"かどうかの判定をまず行うようにする。
# 立っている列の間に倒れている列があるかは、max(stand)-min(stand)+1 != len(stand)と同値(下記参照)
# https://atcoder.jp/contests/abc267/editorial/4740
# max(stand)-min(stand)+1 != len(stand)だと、min(stand)とmax(stand)の間の列がすべて立っている列になる

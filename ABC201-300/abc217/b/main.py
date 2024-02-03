s = ""
for i in range(3):
    s1 = input()
    s += s1
contest = ["ABC", "ARC", "AGC", "AHC"]
for i in contest:
    if not(i in s):
        print(i)
        break
# 別解　リストから入力値を除いていき、残ったものを表示
l = ["ABC", "ARC", "AGC", "AHC"]
for i in range(3):
    S = input()
    l.remove(S)
print(l[0])

# 別解（公式解答　二重For文）
cand = ["ABC", "ARC", "AGC", "AHC"]
used = [True for i in range(4)]
for i in range(3):
    str = input()
    for j in range(4):
        if(str == cand[j]):
            used[j] = False
for i in range(4):
    if(used[i]):
        print(cand[i])

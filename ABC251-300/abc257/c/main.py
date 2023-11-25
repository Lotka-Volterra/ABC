n = int(input())
s = input()
w = list(map(int, input().split()))
strs = list(s)
child = strs.count("0")
adult = strs.count("1")
ws = []
for i in range(n):
    ws.append([w[i], s[i]])
ws.sort()
# 誰よりも軽い・重い非実在人間の体重を追加しておく
w.append(0)
w.append(10**9 + 1)
setw = list(set(w))
setw.sort()
correctnum = []
childcount = 0
adultcount = 0
wsInd = 0
lenSetW = len(setw)
for i in range(lenSetW):
    # while ws[wsInd][0] < setw[i]:
    while wsInd < n and ws[wsInd][0] < setw[i]:
        if ws[wsInd][1] == "0":
            childcount += 1
        else:
            adultcount += 1
        wsInd += 1
    correctadult = adult - adultcount
    correctnum.append(childcount + correctadult)
print(max(correctnum))

s = input()
maru = []
maruOrHatena = []
for i in range(10):
    if s[i] == "o":
        maru.append(i)
        maruOrHatena.append(i)
    elif s[i] == "?":
        maruOrHatena.append(i)
ans = 0
# マルかハテナの数で4重ループして4桁の暗証番号を作る。暗証番号に、マルの数が全て入っていたらありうる暗証番号とする
for i in maruOrHatena:
    for j in maruOrHatena:
        for k in maruOrHatena:
            for l in maruOrHatena:
                number = str(i) + str(j) + str(k) + str(l)
                allInclude = True
                for m in maru:
                    if str(m) not in number:
                        allInclude = False
                if allInclude:
                    ans += 1
print(ans)

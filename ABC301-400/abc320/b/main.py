# 文字列の全探索　回文　逆順にするreversed()を使わなくてもS[(N-1)-i]でいい
# データを受け取る
S = input()
n = len(S)
ans = 1

for i in range(n - 1):
    for j in range(i + 1, n):
        if j != n - 1:
            kaibun = S[i : j + 1]
        else:
            kaibun = S[i:]
        lenkaibun = len(kaibun)

        flag=True
        # 線形探索
        for k in range(lenkaibun):
            if kaibun[k] != kaibun[(lenkaibun - 1) - k]:
                flag=False
                break
        if(flag):
            ans = max(ans, lenkaibun)
print(ans)

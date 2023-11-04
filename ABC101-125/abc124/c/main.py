# 0番目が黒の場合と、白の場合の2通りで、塗り替える必要のあるタイル数をカウントする
s = input()
blackCount = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] != "0":
        blackCount += 1
    elif i % 2 == 1 and s[i] != "1":
        blackCount += 1
print(min(blackCount, len(s) - blackCount))

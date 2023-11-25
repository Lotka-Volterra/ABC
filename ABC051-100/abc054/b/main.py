n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]
# Aの左端からBを重ねて平行移動させて、一致する部分があるかどうかを確認する。
for i in range(n - m + 1):
    for j in range(n - m + 1):
        isSame = True
        for k in range(m):
            for l in range(m):
                if a[i + k][j + l] != b[k][l]:
                    isSame = False
                    break
            if not isSame:
                break
        if isSame:
            print("Yes")
            quit()
print("No")

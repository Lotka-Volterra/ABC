a, b, c, d = map(int, input().split())
for i in range(101):
    c -= b
    if c <= 0:
        print('Yes')
        quit()
    a -= d
    if a <= 0:
        print('No')
        quit()

# 青木くんのモンスターは(c+b-1)//b回目に体力が切れる。（つまり、切り上げ）
# 高橋くんのモンスターは(a+d-1)//d回目に体力が切れる。（つまり、切り上げ）
# (c+b-1)//b =< (a+d-1)//d なら高橋くんの勝ち。

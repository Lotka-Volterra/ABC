a, b = map(int, input().split())
if max(a, b) >= 9:
    print(":(")
else:
    print("Yay!")
# 最適に取る方法は交互に取ること。
# 最適に取るとふたりとも最高8個取れる。
# なので、どちらも8個以下の場合はYay!
# そうでないなら:(である。

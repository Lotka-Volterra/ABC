n = int(input())
# 1の位
n % 10
# 10の位
(n // 10) % 10
# https://atcoder.jp/contests/abc326/editorial/7500
# floor(n/10)mod10らしい
# 100の位
(n // 100) % 10


# n進法、n進数表記
# integerをbase進数表記の文字列にして返す関数
# https://atcoder.jp/contests/abc186/editorial/403
def toNBase(integer, base):
    answerString = ""
    # integerが0より大きい間
    while integer:
        answerString = str(integer % n) + answerString
        integer //= base
    return integer

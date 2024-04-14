import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
n = int(input())
s = input()
c = list(map(int, input().split()))
# 0始まりにするとき、修正のためのコストの累積和
zero_start = []
# 0終わりにするとき、修正のためのコストの累積和
zero_end = []
# 1始まりにするとき、修正のためのコストの累積和
one_start = []
# 1終わりにするとき、修正のためのコストの累積和
one_end = []
for i in range(n):
    # 0始まりにするときの累積和計算用変数
    zero_plus = 0
    # 1始まりにするときの累積和計算用変数
    one_plus = 0
    # iの奇偶とs[i]が0か1かでコストが発生するかどうか変わる
    if i % 2 == 0:
        if s[i] == "1":
            zero_plus += c[i]
        else:
            one_plus += c[i]
    else:
        if s[i] == "1":
            one_plus += c[i]
        else:
            zero_plus += c[i]
    # 累積和。i==0のときは別枠にしている
    if i == 0:
        zero_start.append(zero_plus)
        one_start.append(one_plus)
    else:
        zero_start.append(zero_start[i - 1] + zero_plus)
        one_start.append(one_start[i - 1] + one_plus)

# sとcを逆順にして、0終わり、1終わりのそれぞれの場合の累積和を考える
reversed_s = "".join(list(reversed(s)))
c.reverse()
for i in range(n):
    zero_plus = 0
    one_plus = 0
    if i % 2 == 0:
        if reversed_s[i] == "1":
            zero_plus += c[i]
        else:
            one_plus += c[i]
    else:
        if reversed_s[i] == "1":
            one_plus += c[i]
        else:
            zero_plus += c[i]
    if i == 0:
        zero_end.append(zero_plus)
        one_end.append(one_plus)
    else:
        zero_end.append(zero_end[i - 1] + zero_plus)
        one_end.append(one_end[i - 1] + one_plus)

zero_end.reverse()
one_end.reverse()
ans = float("inf")
for i in range(n - 1):
    # i,i+1を00にする場合
    ans_zero = 0
    # i,i+1を11にする場合
    ans_one = 0
    # 例えばi,i+1を00にする場合、答えはiを前から0にするコストの総和とi+1を後ろから0にするコストの総和
    if i % 2 == 0:
        ans_zero += zero_start[i]
        if n % 2 == 0:
            ans_zero += zero_end[i + 1]
        else:
            ans_zero += one_end[i + 1]
    else:
        ans_zero += one_start[i]
        if n % 2 == 0:
            ans_zero += one_end[i + 1]
        else:
            ans_zero += zero_end[i + 1]
    if i % 2 == 0:
        ans_one += one_start[i]
        if n % 2 == 0:
            ans_one += one_end[i + 1]
        else:
            ans_one += zero_end[i + 1]
    else:
        ans_one += zero_start[i]
        if n % 2 == 0:
            ans_one += zero_end[i + 1]
        else:
            ans_one += one_end[i + 1]
    ans = min(ans, ans_one, ans_zero)
print(ans)

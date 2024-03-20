# import math
# import sys
# from collections import defaultdict, deque

# sys.setrecursionlimit(100000000)
# x = input()
# new_x = ""
# if len(str(abs(int(x)))) != 1:
#     new_x = x[:-1] + "." + x[-1]
# else:
#     if int(x) < 0:
#         new_x = "-0." + x
#     else:
#         new_x = "0." + x
# print(new_x)
# new_x = float(new_x)
# print(math.ceil(new_x))
x = int(input())
# xを10で割った時の商と余りを求める
quotient, remainder = divmod(x, 10)

# 余りが0ならそのまま商、それ以外なら商に1を加えたものが答え
result = quotient if remainder == 0 else quotient + 1

print(result)

from locale import YESEXPR
from tkinter.messagebox import YES, YESNO, YESNOCANCEL

from pkg_resources import yield_lines
from yaml import YAMLObjectMetaclass


n = int(input())
for i in range(26):
    for j in range(15):
        if 4*i+7*j == n:
            print('Yes')
            quit()
print('No')
""" 答えがNoになるのは、N = 1, 2, 3, 5, 6, 9, 10, 13, 17 の場合のみ
n>=21では、答えが必ずYesになる。
(証明)n mod 4 = 0のとき、YES
n mod 4 = 1のとき、n-21 mod 4 <=> -21+1 mod 4 =0より、YES
n mod 4 = 2のとき、n-14 mod 4 <=> -14+2 mod 4 =0より、YES
n mod 4 = 3のとき、n-7 mod 4 <=> -7+3 mod 4 =0より、YES
以上から、n>=21では、ドーナツを適切に購入すれば必ずYesになる。 """
# 別解
n = int(input())
if n in [1, 2, 3, 5, 6, 9, 10, 13, 17]:
    print('No')
else:
    print('Yes')

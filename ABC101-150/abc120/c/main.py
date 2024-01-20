#!/bin/python3

import math
import os
import random
import re
import sys

#
stack = []
s = input()
ans = 0
# スタックは後入れ先出し（LIFO）のため、適する
for char in s:
    # スタックが空の場合、追加
    if not stack:
        stack.append(char)
    # スタックが空でない場合
    else:
        # スタックの最新要素とcharが異なるなら、最新要素をスタックから取り除く
        if stack[-1] != char:
            stack.pop()
            ans += 2
        else:
            stack.append(char)
print(ans)

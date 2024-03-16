import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)

n, q = map(int, input().split())
s = input()
int_s = int(s, 2)
# print(int_s)
que = deque()
for i in range(q):
    query, l, r = map(int, input().split())
    if query == 1:
        reverse_int = 2 ** (r - l + 1) - 1
        reverse_int = reverse_int << (n - r)
        int_s = int_s ^ reverse_int
        # print(int_s)
    else:
        # print(n - r)
        # print(int_s)
        lr_int = int_s >> (n - r)
        # print(1, lr_int)
        lr_and_int = 2 ** (r - l + 1) - 1
        lr_int = lr_int & lr_and_int
        # print(lr_int)
        amari = lr_int % 2
        and_int = lr_int << 1
        if amari == 0:
            and_int += 1
        print(and_int)
        if lr_int & and_int == 0:
            print("Yes")
        else:
            print("No")

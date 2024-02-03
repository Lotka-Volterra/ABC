import math
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000000)
h, w, k = map(int, input().split())
HW = []
yoko = w + 1
for i in range(h):
    s = input()
    HW.append(s)
    split_s = s.split("x")
    for segment in split_s:
        if len(segment) >= k:
            dot_count = segment[:k].count(".")
            for l in range(len(segment) - k + 1):
                yoko = min(yoko, dot_count)
                if l + k < len(segment):
                    # 次のスライスへ移動する際に、カウントを更新
                    if segment[l] == ".":
                        dot_count -= 1
                    if segment[l + k] == ".":
                        dot_count += 1
tate = h + 1
for i in range(w):
    tate_s_list = []
    for j in range(h):
        tate_s_list.append(HW[j][i])
    tate_s = "".join(tate_s_list)
    split_s = tate_s.split("x")
    # print(split_s)
    for segment in split_s:
        if len(segment) >= k:
            dot_count = segment[:k].count(".")
            for l in range(len(segment) - k + 1):
                tate = min(tate, dot_count)
                if l + k < len(segment):
                    # 次のスライスへ移動する際に、カウントを更新
                    if segment[l] == ".":
                        dot_count -= 1
                    if segment[l + k] == ".":
                        dot_count += 1
ans = 3 * (10**5)
if yoko != w + 1:
    ans = yoko
if tate != h + 1:
    ans = min(ans, tate)
if ans == 3 * (10**5):
    print(-1)
else:
    print(ans)

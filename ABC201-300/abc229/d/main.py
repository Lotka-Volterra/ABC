import sys

sys.setrecursionlimit(100000000)
s = input()
k = int(input())
ruiseki = [0]
count = 0
for i in s:
    if i == ".":
        count += 1
    ruiseki.append(count)
ans = 0
r = 1
for l in range(1, len(s) + 1):
    # r = l + 1
    while r <= len(s) and ruiseki[r] - ruiseki[l - 1] <= k:
        r += 1
        # if r == len(s) + 1:
        #     break
    ans = max(r - l, ans)
    # if r == len(s) + 1:
    # break
print(ans)

from collections import deque

n = int(input())
s = input()
new_s = []
for i in range(n):
    if s[i] == "L":
        new_s.append("R")
    else:
        new_s.append("L")
d = deque()
d.append(n)
for i in range(n - 1, -1, -1):
    if new_s[i] == "R":
        d.append(i)
    else:
        d.appendleft(i)
print(*d)

zahyo = []
import copy
n = int(input())
s = input()
zahyo.append((0, 0))
for i in range(n):
    newzahyo = list(copy.copy(zahyo[i]))
    if s[i] == "R":
        newzahyo[0] += 1
    elif s[i] == "L":
        newzahyo[0] -= 1
    elif s[i] == "U":
        newzahyo[1] += 1
    else:
        newzahyo[1] -= 1
    zahyo.append(tuple(newzahyo))
# print(zahyo)
lenzahyo = len(set(zahyo))
# lenzahyo = set(zahyo)

if lenzahyo < n + 1:
    print("Yes")
else:
    print("No")

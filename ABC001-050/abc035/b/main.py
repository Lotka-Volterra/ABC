s = input()
t = int(input())
L, R, U, D, Q = 0, 0, 0, 0, 0
for i in s:
    if i == "L":
        L += 1
    elif i == "R":
        R += 1
    elif i == "U":
        U += 1
    elif i == "D":
        D += 1
    else:
        Q += 1
if t == 1:
    if L >= R:
        L += Q
    else:
        R += Q
else:
    for i in range(Q):
        if L > R:
            R += 1
        elif L < R:
            L += 1
        elif U > D:
            D += 1
        elif U < D:
            U += 1
        else:
            L += 1
print(abs(L - R) + abs(U - D))

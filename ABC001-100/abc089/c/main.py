n = int(input())
m, a, r, c, h = 0, 0, 0, 0, 0
for i in range(n):
    s = input()
    if s[0] == "M":
        m += 1
    elif s[0] == "A":
        a += 1
    elif s[0] == "R":
        r += 1
    elif s[0] == "C":
        c += 1
    elif s[0] == "H":
        h += 1
ans = (
    m * a * r
    + m * a * c
    + m * a * h
    + m * r * c
    + m * r * h
    + m * c * h
    + a * r * c
    + a * r * h
    + a * c * h
    + r * c * h
)
print(ans)

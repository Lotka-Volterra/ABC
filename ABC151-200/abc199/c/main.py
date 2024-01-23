n = int(input())
s = [""] + list(input())
q = int(input())

rev = False
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if rev:
            if a <= n:
                a += n
            else:
                a -= n
            if b <= n:
                b += n
            else:
                b -= n
        s[a], s[b] = s[b], s[a]
    else:
        rev = not rev
if rev:
    s = s[n + 1 :] + s[: n + 1]
print("".join(s))

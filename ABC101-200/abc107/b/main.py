h, w = map(int, input().split())
a = []
white = ['.' for i in range(w)]
for i in range(h):
    s = list(input())
    if s != white:
        a.append(s)
whitelist = []
for i in range(w):
    whiteflag = True
    for j in range(len(a)):
        if a[j][i] != '.':
            whiteflag = False
            break
    if whiteflag:
        whitelist.append(i)

for i in range(len(a)):
    new_s = []
    for j in range(w):
        if j not in whitelist:
            new_s.append(a[i][j])
    print("".join(new_s))

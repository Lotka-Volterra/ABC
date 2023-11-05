h, w = map(int, input().split())
ans = 0
for i in range(h):
    s = input()
    for j in range(w - 1):
        if s[j] == "T" and s[j + 1] == "T":
            s = s[:j] + "PC" + s[j + 2 :]
    print(s)

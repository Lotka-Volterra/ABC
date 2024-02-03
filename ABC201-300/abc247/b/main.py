n = int(input())
s = []
t = []
for i in range(n):
    s1, t1 = input().split()
    s.append(s1)
    t.append(t1)
for i in range(n):
    srest = []
    trest = []
    if i != n - 1:
        srest = s[:i] + s[i + 1 :]
        trest = t[:i] + t[i + 1 :]
    else:
        srest = s[:i]
        trest = t[:i]
    allrest = list(set(srest + trest))
    # 名氏も名前も他の誰かと被っていたらニックネームがつけられな
    if s[i] in allrest and t[i] in allrest:
        print("No")
        quit()
print("Yes")

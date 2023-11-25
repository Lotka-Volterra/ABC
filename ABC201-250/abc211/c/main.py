s = input()
c = []
h = []
o = []
k = []
u = []
d = []
a = []
ii = []
for i in range(len(s)):
    if s[i] == "c":
        c.append(i)
    elif s[i] == "h":
        h.append(i)
    elif s[i] == "o":
        o.append(i)
    elif s[i] == "k":
        k.append(i)
    elif s[i] == "u":
        u.append(i)
    elif s[i] == "d":
        d.append(i)
    elif s[i] == "a":
        a.append(i)
    elif s[i] == "i":
        ii.append(i)
count = 0
for ci in c:
    for hi in h:
        for oi in o:
            for ki in k:
                for ui in u:
                    for di in d:
                        for ai in a:
                            for iii in ii:
                                if ci < hi < oi < ki < ui < di < ai < iii:
                                    count += 1
print(count % (10**9 + 7))

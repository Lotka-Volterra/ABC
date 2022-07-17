n = int(input())
s = []
for i in range(n):
    s.append(input())
ss = [[] for i in range(10)]

for h in range(n):
    for i in range(10):
        ss[i].append(s[h].index(str(i)))
ss.sort()

t = []
for i in ss:
    sum = 0
    for j in range(n):
        if j != 0 and j<n-1:
            if i[j-1] == i[j]:
                sum += 10
                continue
        if j == n-1:
            if i[j-1]==i[j]:
                sum+=10
            else:
                sum+=i[j]
    t.append(sum)
print(min(t))

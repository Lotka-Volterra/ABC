import collections

n = int(input())
s = [input() for i in range(n)]
cs = collections.Counter(s).most_common()
ans = []
for i in cs:
    if i[1] == cs[0][1]:
        ans.append(i[0])
ans.sort()
for i in ans:
    print(i)

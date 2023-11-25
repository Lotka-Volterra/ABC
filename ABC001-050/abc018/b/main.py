s = input()
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    part = s[l - 1 : r]
    partReverse = ""
    for i in range(len(part) - 1, -1, -1):
        partReverse += part[i]
    s = s[: l - 1] + partReverse + s[r:]
print(s)

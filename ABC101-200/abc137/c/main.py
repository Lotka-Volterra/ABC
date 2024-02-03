from collections import defaultdict

n = int(input())
dict = defaultdict(int)
for i in range(n):
    s = input()
    s = "".join(sorted(s))
    dict[s] += 1
ans = 0
for value in dict.values():
    ans += value * (value - 1) // 2
print(ans)

from collections import defaultdict

n = int(input())
s = [input() for i in range(n)]
alph = [[] for i in range(26)]
for i in range(n):
    num = defaultdict(int)
    for j in s[i]:
        num[j] += 1
    for i in num:
        alph[ord(i) - ord("a")].append(num[i])
ans = ""
for i in range(26):
    # 全ての文書に出現する場合
    if len(alph[i]) == n:
        ans += chr(ord("a") + i) * min(alph[i])
print(ans)

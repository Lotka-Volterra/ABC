s = input()
ans = ""
boin = "aiueo"
for i in range(len(s)):
    if s[i] not in boin:
        ans += s[i]
print(ans)

s = input()
ans = ""
for i in range(len(s)):
    if s[i] == ".":
        break
    ans += s[i]
print(ans)

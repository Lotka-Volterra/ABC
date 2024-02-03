s = input()
alph = [0] * 26
for i in range(len(s)):
    alph[ord(s[i]) - ord("a")] += 1
ans = ""
for i in range(26):
    ans += chr(ord("a") + i) * alph[i]
print(ans)

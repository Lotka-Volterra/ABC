n = int(input())
s = input()
ans = ""
for i in range(len(s)):
    okikae = (ord(s[i]) - ord("A") + n) % 26
    ans += chr(ord("A") + okikae)
print(ans)

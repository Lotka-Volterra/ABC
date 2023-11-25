s = input()
t = input()
k = ord(t[0]) - ord(s[0])
for i in range(len(s)):
    dif = (ord(s[i]) - ord("a") + k) % 26
    if chr(ord("a") + dif) != t[i]:
        print("No")
        quit()
print("Yes")

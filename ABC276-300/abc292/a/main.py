s = input()
upperS = ""
for i in range(len(s)):
    ordS = ord(s[i]) - ord("a")
    upperS += chr(ord("A") + ordS)
print(upperS)

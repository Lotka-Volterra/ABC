s = input()
slen = len(s)
for i in range(slen // 2):
    print(s[2 * i + 1], end="")
    print(s[2 * i], end="")
print()
s = input()
reversed_s = s[::-1]

count = 0
i = 0
while i < len(s):
    if s[i] == "0" and i + 1 < len(s) and s[i + 1] == "0":
        i += 1
    count += 1
    i += 1
print(count)

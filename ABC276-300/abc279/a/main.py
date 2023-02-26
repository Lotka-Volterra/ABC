s = input()
count = 0
for i in range(len(s)):
    if s[i] == "v":
        count += 1
    else:
        count += 2
print(count)

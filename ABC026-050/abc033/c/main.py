s = input().split("+")
count = 0
for i in range(len(s)):
    if "0" not in s[i]:
        count += 1
print(count)

s = input()
mae = s[0]
count = 1
ans = ""
for i in range(1, len(s)):
    if s[i] == mae:
        count += 1
    else:
        ans += mae + str(count)
        count = 1
        mae = s[i]
    if i == len(s) - 1:
        ans += mae + str(count)
print(ans)

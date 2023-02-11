s = input()

for i in range(len(s)):
    count = 0
    if s[i] == s[0]:
        count += 1
    if s[i] == s[1]:
        count += 1
    if s[i] == s[2]:
        count += 1
    if count == 1:
        print(s[i])
        quit()
print(-1)

#愚直に
if s[0]!=s[1] and s[0]!=s[2]:
    print(s[0])
elif s[1]!=s[0] and s[1]!=s[2]:
    print(s[1])
elif s[2]!=s[0] and s[2]!=s[1]:
    print(s[2])
else:
    print(-1)




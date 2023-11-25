s = input()
t = input()
if s == t:
    print("Yes")
    quit()
count = 0
diff = 0
for i in range(len(s) - 1):
    if s[i] == t[i]:
        continue
    elif s[i] == t[i + 1] and s[i + 1] == t[i]:
        count += 1
    else:
        diff += 1
if count == 1 and diff <= 1:
    print("Yes")
else:
    print("No")

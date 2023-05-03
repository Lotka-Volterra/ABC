s = input()
t = input()
lens = len(s)
lent = len(t)
for i in range(lens - lent + 1):
    if t == s[i : i + lent]:
        print("Yes")
        quit()
print("No")

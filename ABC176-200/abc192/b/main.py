s = input()
for i in range(len(s)):
    if i % 2 == 0 and s[i].isupper():
        print("No")
        quit()
    elif i % 2 == 1 and s[i].islower():
        print("No")
        quit()
print("Yes")

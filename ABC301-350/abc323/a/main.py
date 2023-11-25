s = input()
for i in range(16):
    if i % 2 == 1 and s[i] != "0":
        print("No")
        quit()
print("Yes")

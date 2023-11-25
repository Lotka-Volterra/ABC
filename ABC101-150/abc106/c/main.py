s = input()
k = int(input())

for i in range(min(len(s), k)):
    if s[i] != "1":
        print(int(s[i]))
        quit()
print(1)

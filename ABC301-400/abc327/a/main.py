n = int(input())
s = input()
for i in range(n - 1):
    if s[i : i + 2] == "ab" or s[i : i + 2] == "ba":
        print("Yes")
        quit()
print("No")

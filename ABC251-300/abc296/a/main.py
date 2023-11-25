n = int(input())
s = input()
mae = s[0]
for i in range(1, n):
    if s[i] == mae:
        print("No")
        quit()
    else:
        mae = s[i]
print("Yes")

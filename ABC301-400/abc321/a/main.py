n = input()
for i in range(len(n) - 1):
    if n[i] <= n[i + 1]:
        print("No")
        quit()
print("Yes")

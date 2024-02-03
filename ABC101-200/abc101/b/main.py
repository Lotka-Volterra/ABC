n = input()
sn = 0
for i in n:
    sn += int(i)
print("Yes") if int(n) % sn == 0 else print("No")

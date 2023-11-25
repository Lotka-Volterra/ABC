n = input()
count = 0
for i in range(len(n)):
    count += int(n[i])
if count % 9 == 0:
    print("Yes")
else:
    print("No")

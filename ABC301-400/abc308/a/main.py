s = list(map(int, input().split()))
flag = True
for i in range(7):
    if s[i] > s[i + 1]:
        flag = False
    if s[i] < 100 or s[i] > 675:
        flag = False
    if s[i] % 25 != 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")

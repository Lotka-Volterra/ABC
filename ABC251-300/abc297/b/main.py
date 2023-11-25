s = input()
b = []
r = []
k = -1
for i in range(8):
    if s[i] == "B":
        b.append(i)
    elif s[i] == "R":
        r.append(i)
    elif s[i] == "K":
        k = i
oeflag = b[0] % 2 != b[1] % 2
if oeflag and (r[0] < k < r[1]):
    print("Yes")
else:
    print("No")

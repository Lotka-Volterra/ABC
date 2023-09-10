n = int(input())
s = input()
isGood = False
isBad = False
for i in range(n):
    if s[i] == "o":
        isGood = True
    elif s[i] == "x":
        isBad = True
if isGood and not isBad:
    print("Yes")
else:
    print("No")

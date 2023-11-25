n = int(input())
s = input()
twin = 0
awin = 0
for i in range(n):
    if s[i] == "T":
        twin += 1
    else:
        awin += 1
    if twin == (n + 1) // 2:
        print("T")
        quit()
    elif awin == (n + 1) // 2:
        print("A")
        quit()

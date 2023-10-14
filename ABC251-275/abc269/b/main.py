a, b = 0, 0
firstString = False
cd = []
for i in range(10):
    si = input()
    if "#" in si and not firstString:
        firstString = True
        a = i + 1
    if "#" not in si and firstString:
        firstString = False
        b = i
    for j in range(10):
        if si[j] == "#":
            cd.append(j + 1)
if b == 0:
    b = 10
print(a, b)
print(cd[0], cd[-1])


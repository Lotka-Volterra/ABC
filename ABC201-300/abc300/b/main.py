h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(input())
b = []
for i in range(h):
    b.append(input())
if a == b:
    print("Yes")
    quit()
for i in range(1, h):
    a = a[1:] + [a[0]]
    aa = a
    if a == b:
        print("Yes")
        quit()
    for j in range(1, w):
        for k in range(h):
            aa[k] = aa[k][1:] + aa[k][0]
        if a == b:
            print("Yes")
            quit()
print("No")

n = int(input())
a = []
for i in range(n):
    ai = list(map(int, input().split()))
    for j in range(n):
        if ai[j] == 1:
            a.append([i + 1, j + 1])
b = []
for i in range(n):
    bi = list(map(int, input().split()))
    for j in range(n):
        if bi[j] == 1:
            b.append([i + 1, j + 1])

for k in range(4):
    rolledA = []
    for i in range(len(a)):
        rolledA.append([a[i][1], n + 1 - a[i][0]])
    rolledA.sort()
    allInB = True
    for j in rolledA:
        if j not in b:
            allInB = False
    if allInB:
        print("Yes")
        quit()
    a = rolledA
print("No")

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
passed = [False] * n
math = []
for i in range(n):
    math.append([a[i], n - i, i])
math.sort(reverse=True)
for i in range(x):
    passed[math[i][2]] = True
eng = []
for i in range(n):
    eng.append([b[i], n - i, i])
eng.sort(reverse=True)
count = 0
for i in range(n):
    if count >= y:
        break
    if passed[eng[i][2]] == False:
        passed[eng[i][2]] = True
        count += 1
total = []
for i in range(n):
    total.append([a[i] + b[i], n - 1, i])
total.sort(reverse=True)
count = 0
for i in range(n):
    if count >= z:
        break
    if passed[total[i][2]] == False:
        passed[total[i][2]] = True
        count += 1
for i in range(n):
    if passed[i] == True:
        print(i + 1)

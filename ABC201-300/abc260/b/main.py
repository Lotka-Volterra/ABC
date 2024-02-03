n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ai = []
for i in range(n):
    ai.append([a[i], n + 1 - i, i])
ai.sort(reverse=True)
passed = []
for i in range(x):
    passed.append(ai[i][2] + 1)
bi = []
for i in range(x, n):
    bi.append([b[ai[i][2]], ai[i][1], ai[i][2]])
bi.sort(reverse=True)
for i in range(y):
    passed.append(bi[i][2] + 1)
abi = []
for i in range(y, n - x):
    abi.append([a[bi[i][2]] + bi[i][0], bi[i][1], bi[i][2]])
abi.sort(reverse=True)
for i in range(z):
    passed.append(abi[i][2] + 1)
passed.sort()
for i in passed:
    print(i)

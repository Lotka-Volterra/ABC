n = int(input())
p = list(map(int, input().split()))
a = [[] for i in range(n)]
a[0].append(1)
for i in range(n - 1):
    for j in range(n):
        if p[i] in a[j]:
            a[j + 1].append(i + 2)
            break
gen = 0
for i in range(n):
    if n in a[i]:
        break
    gen += 1
print(gen)

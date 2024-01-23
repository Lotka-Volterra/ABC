import itertools

n, k = map(int, input().split())
T = []
for i in range(n):
    T.append(list(map(int, input().split())))
seq = range(1, n)
ans = 0
for i in list(itertools.permutations(seq)):
    time = 0
    i = [0] + list(i) + [0]
    for j in range(n):
        time += T[i[j]][i[j + 1]]
    if time == k:
        ans += 1
print(ans)

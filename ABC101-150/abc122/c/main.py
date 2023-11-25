n, q = map(int, input().split())
s = input()
ruiseki = [0, 0]
count = 0
for i in range(1, n):
    if s[i - 1 : i + 1] == "AC":
        count += 1
    ruiseki.append(count)
for i in range(q):
    l, r = map(int, input().split())
    print(ruiseki[r] - ruiseki[l])

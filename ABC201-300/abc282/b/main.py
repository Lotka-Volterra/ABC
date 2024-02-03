n, m = map(int, input().split())
s = []
for i in range(n):
    str = input()
    str = str.replace("o", "1")
    str = str.replace("x", "0")
    str = "0b" + str
    s.append(int(str, 2))
andans = "0b" + ("1" * m)
andans = int(andans, 2)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if s[i] | s[j] == andans:
            count += 1
print(count)

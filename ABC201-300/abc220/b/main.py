k = int(input())
a, b = map(int, input().split())
a10 = 0
for i in range(len(str(a))):
    a10 += int(str(a)[-i - 1]) * (k**i)
b10 = 0
for i in range(len(str(b))):
    b10 += int(str(b)[-i - 1]) * (k**i)
print(a10 * b10)

n = int(input())
d, x = map(int, input().split())
a = []
count = 0
for i in range(n):
    a = int(input())
    count += (d - 1) // a + 1
print(count + x)

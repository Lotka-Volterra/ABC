h, w = map(int, input().split())
s = []
count = 0
for i in range(h):
    s = input()
    count += s.count("#")
print(count)

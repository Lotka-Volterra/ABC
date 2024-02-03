h, w = map(int, input().split())
c = [0] * w
for i in range(h):
    ci = input()
    for i in range(w):
        if ci[i] == "#":
            c[i] += 1
print(*c)

h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
current_h, current_w = 0, 0
ans = [[0] * w for i in range(h)]
for i in range(n):
    count = 0
    while count < a[i]:
        ans[current_h][current_w] = i + 1
        count += 1
        if current_h == h - 1 and current_w % 2 == 0:
            current_w += 1
        elif current_h == 0 and current_w % 2 == 1:
            current_w += 1
        elif current_w % 2 == 0:
            current_h += 1
        else:
            current_h -= 1
for i in range(h):
    print(*ans[i])

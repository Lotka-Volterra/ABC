color = [0] * 8
n = int(input())
a = list(map(int, input().split()))
rainbow = 0
for i in range(n):
    ai = a[i] // 400
    if ai < 8:
        color[ai] = 1
    else:
        rainbow += 1
colors = sum(color)
# 最小値は全員レート3200以上の場合を考慮
print(max(1, colors), colors + rainbow)

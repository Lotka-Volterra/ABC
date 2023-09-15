n, m = map(int, input().split())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
ab.sort()
count = 0
price = 0
for i in range(n):
    if m - count > ab[i][1]:
        count += ab[i][1]
        price += ab[i][0] * ab[i][1]
    else:
        price += ab[i][0] * (m - count)
        print(price)
        quit()

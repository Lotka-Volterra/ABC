n, x = map(int, input().split())
a = list(map(int, input().split()))
price = 0
for i in range(n):
    price += a[i]
    if i % 2 == 1:
        price -= 1
print("Yes") if price <= x else print("No")

n = int(input())
mint = float("inf")
for i in range(n):
    t = int(input())
    mint = min(mint, t)
print(mint)

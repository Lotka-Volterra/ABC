n = int(input())
ans = n
for tate in range(1, n + 1):
    yoko = n // tate
    sa = abs(tate - yoko)
    amari = n - tate * yoko
    ans = min(ans, sa + amari)
print(ans)

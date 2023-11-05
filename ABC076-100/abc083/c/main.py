x, y = map(int, input().split())
ans = 1
while x <= y:
    x *= 2
    ans += 1
print(ans - 1)

n = int(input())
ans = 0
for i in range(10**5):
    if i**2 <= n:
        ans = max(ans, i**2)
    else:
        print(ans)
        quit()

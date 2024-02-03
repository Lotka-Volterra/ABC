h, w = map(int, input().split())
for i in range(h):
    a = list(map(int, input().split()))
    ans = ""
    for i in range(w):
        if a[i] == 0:
            ans += "."
        else:
            ans += chr(ord("A") + a[i] - 1)
    print(ans)

l, r = map(int, input().split())
s = input()
ans = s[: l - 1]
for i in range(r - 1, l - 2, -1):
    ans += s[i]
ans += s[r:]
print(ans)

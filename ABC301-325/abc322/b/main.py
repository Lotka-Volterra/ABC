n, m = map(int, input().split())
s = input()
t = input()
ans = 3
if t[:n] == s:
    ans -= 2
if t[-n:] == s:
    ans -= 1
print(ans)

n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
s.sort()

ans = ""
for i in s:
    ans += i
print(ans)

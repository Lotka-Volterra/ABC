n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ruisekiwa = [0]
for i in range(n):
    ruisekiwa.append((ruisekiwa[i] + a[-i - 1]) % mod)
ans = 0
for i in range(n):
    ans = (ans + a[i] * ruisekiwa[-i - 2]) % mod
print(ans)

n = int(input())
a_b = []
aoki = 0
for i in range(n):
    a, b = map(int, input().split())
    # [高橋派の実質的な増加人数（純増＋青木派に与えるダメージ）、青木派の減少人数]でソート
    a_b.append([a + b + a, a])
    aoki += a
a_b.sort(reverse=True)
takahashi = 0
ans = 0
for i in range(n):
    ans += 1
    takahashi += a_b[i][0] - a_b[i][1]
    aoki -= a_b[i][1]
    if takahashi > aoki:
        break
print(ans)

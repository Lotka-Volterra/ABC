n, h = map(int, input().split())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
wield_katana = max(A)
B.sort(reverse=True)
throwing_katana_damage = [B[0]]
for i in range(1, n):
    throwing_katana_damage.append(throwing_katana_damage[-1] + B[i])
ans = float("inf")
for i in range(n):
    count = i + 1
    remaining_hp = max(h - throwing_katana_damage[i], 0)
    count += int((remaining_hp + wield_katana - 1) / wield_katana)
    ans = min(ans, count)
print(ans)

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dict = defaultdict(int)
for i in range(n):
    dict[a[i]] += 1
odd, even = 0, 0
for i in dict.values():
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
ans = 0
# 出現回数が奇数階のものは、それ単体で1個残せる
# 出現回数が偶数回のものは、ペアで打ち消し合うことで1個ずつ残せる
# 出現回数が偶数回のものが奇数種類ある場合、1個余り、それは出現回数が奇数回のもの一つと打ち消し合う
if even % 2 == 1:
    even -= 1
    odd -= 1
    ans += 1
print(even + odd + ans)

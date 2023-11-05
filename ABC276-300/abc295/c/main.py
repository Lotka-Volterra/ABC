n = int(input())
a = list(map(int, input().split()))
dict = {}
for i in range(n):
    if a[i] not in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]] += 1
ans = 0
for i in set(a):
    ans += dict[i] // 2
print(ans)

# 楽な実装
# 指定した文字列（または正規表現）にマッチするすべての部分文字列を置換する標準ライブラリを使う
# H, W = map(int, input().split())
# for _ in range(H):
#     print(input().replace('TT', 'PC'))

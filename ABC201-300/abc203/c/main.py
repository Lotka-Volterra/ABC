# n, k = map(int, input().split())
# a_b = []
# for i in range(n):
#     a, b = map(int, input().split())
#     a_b.append([a, b])
# # 町の番号の昇順に並べる
# a_b.sort()
# town = 0
# for i in range(n):
#     # これまでに進んだ町＋残金＞次の友達がいる町なら、次の町にたどり着ける
#     if town + k >= a_b[i][0]:
#         # それまでに進んできた町までの移動分townを引く。
#         # 同じ町に複数の友達がいる場合を考慮して、maxで0と比較する。
#         k -= max(a_b[i][0] - town, 0)
#         town += max(a_b[i][0] - town, 0)

#         k += a_b[i][1]
#     else:
#         break
# print(k + town)
# 模範解答
n, k = map(int, input().split())
a_b = []
for i in range(n):
    a, b = map(int, input().split())
    a_b.append([a, b])
# 町の番号の昇順に並べる
a_b.sort()
# 町に到達できる限り、友達からお金をもらう
# 最初の所持金＋友達からもらったお金＝答え（到達できる町）
for i in range(n):
    if a_b[i][0] > k:
        break
    k += a_b[i][1]
print(k)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# hen = []
# chohen = False
# count = 1
# chohenLength = 0
# for i in range(1, n):
#     if a[i] == a[i - 1]:
#         count += 1
#     else:
#         count = 1
#     if not chohen and count == 2:
#         # 正方形がつくれるので面積を出力
#         if i + 2 < n and a[i] == a[i + 1] and a[i] == a[i + 2]:
#             print(a[i] ** 2)
#             quit()
#         # 正方形は作れないが、長方形の長辺として記憶しておく
#         chohenLength = a[i]
#         chohen = True
#     elif chohen and count == 2:
#         # 短辺が見つかったので長方形の面積を出力
#         print(a[i] * chohenLength)
#         quit()
# print(0)

# ユーザー解説の解法。辞書を使う、棒は２本セットで辺のリストに追加する。
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
hen = []
count = {}
for i in range(n):
    if a[i] not in count:
        count[a[i]] = 1
    else:
        count[a[i]] += 1
        if count[a[i]] == 2:
            hen.append(a[i])
            count[a[i]] = 0
if len(hen) < 2:
    print(0)
else:
    print(hen[0] * hen[1])

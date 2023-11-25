# 自分が書いたコード。TLEになる。
# 15行目と17行目がおそらくTLEの原因
# n = int(input())
# a = list(map(int, input().split()))
# setA = sorted(list(set(a)), reverse=True)
# wa = {}

# total = 1
# wa[setA[0]] = 0

# for i in range(1, len(setA)):
#     wa[setA[i]] = total
#     total += 1

# for i in range(n):
#     count = 0
#     for j in a:
#         if wa[j] == i:
#             count += 1
#     print(count)
# 解答例のC++コードをChatGPTに翻訳させて、修正したもの
n = int(input())
mp = {}

a= list(map(int,input().split()))

for i in a:
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1

# ヒント
# 辞書（連想配列）を使うこと
# 以下に気づくこと
# ・0種類=一番大きい数、1種類=二番目に大きい数、と対応していること（len(mp)個の対応がある）
# ・n-len(mp)個以降は0を出力すればいいこと
sorted_mp = sorted(mp.items(), reverse=True)
for item in sorted_mp:
    print(item[1])

for i in range(1, n - len(mp) + 1):
    print(0)

# 模範解答解法1 鶴亀算
# n, m = map(int, input().split())
# if m > 4 * n:
#     print(-1, -1, -1)
#     quit()
# for baby in range(n + 1):
#     if baby * 4 > m:
#         break
#     # 残りを全部大人だと考える
#     adult = n - baby
#     # 足の数の差
#     old = (m - 4 * baby) - 2 * adult
#     adult -= old
#     if adult < 0 or old < 0:
#         continue
#     print(adult, old, baby)
#     quit()
# print(-1, -1, -1)
# 模範解答解法2 老人を大人と子供に換算
# n, m = map(int, input().split())
# if m > 4 * n:
#     print(-1, -1, -1)
#     quit()
# for old in range(2):
#     for baby in range(n + 1 - old):
#         adult = n - (old + baby)
#         if adult * 2 + old * 3 + baby * 4 == m:
#             print(adult, old, baby)
#             quit()
# print(-1, -1, -1)
# 解法3 解法1と2の組み合わせ(O(1))
n, m = map(int, input().split())
if m % 2 == 0:
    old = 0
else:
    old = 1
# 残りを全部大人だと考える
adult = n - old
# 足の数の差を2で割った数を赤ちゃんに変換
baby = ((m - 3 * old) - 2 * adult) // 2
adult -= baby
if adult < 0 or baby < 0:
    print(-1, -1, -1)
else:
    print(adult, old, baby)

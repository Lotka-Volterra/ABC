n = int(input())
draw = [1]
for i in range(1, 7):
    draw.append(6**i)
for j in range(1, 6):
    draw.append(9**j)

# -1で初期化。0で初期化すると、引き落としする必要がない=０回（dp[0]）と混同してしまう
dp = [-1]*(n+1)
# 0円の引き落とし回数は０回
dp[0] = 0

for i in range(1, n+1):
    # 最小手数の初期化。全部１円で引き出す場合よりも多いn+1回
    mindrawcount = n+1
    # mindrawcontの引き落とし額を保存する
    tempdraw = n+1
    for j in draw:
        # iの位置までの払い方がある（i-j>=0,dp[i-j]>0)、かつiの一歩手前までに到達する最小引き落とし回数（暫定）であるとき
        if i-j >= 0 and 0 <= dp[i-j] < mindrawcount:
            mindrawcount = dp[i-j]
            tempdraw = j
    # dp[i](最小引き落とし回数)は、最小手数＋iに到達するまでの１回
    dp[i] = dp[i-tempdraw]+1
print(dp[n])

import math

n, k = map(int, input().split())
ans = 0
# 最初の目=1-NのN通り（1/N）
# 最初の目がiの場合、何回2倍にすればKを超すかは、
# log2(K/i)に対して、切り上げを行った整数（count）で表される。
# 目iが出る確率（1/N）*表がcount回出る確率を足し合わせれば、最終的な答えになる。
# 目iがすでにKを超える場合は、count=0にする
for i in range(1, n + 1):
    count = max(math.ceil(math.log2(k / i)), 0)
    ans += (1 / n) * (1 / (2**count))
print(ans)
# 模範解答のシミュレーション的解き方のほうがわかりやすい

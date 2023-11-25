import math

n = int(input())
a = list(map(int, input().split()))
LCM = math.lcm(*a)

fmax = 0
for i in a:
    fmax += (LCM - 1) % i
print(fmax)

# 別解
# LCM（最大公約数）求める必要ない。
# 最大公約数-1のmod AiはAi-1になるため、Ai-1の和を求めれば答えになる。
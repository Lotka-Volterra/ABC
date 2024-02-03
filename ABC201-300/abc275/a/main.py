n = int(input())
h = list(map(int, input().split()))
maxInd = 0
maxH = 0
for i in range(n):
    if h[i] > maxH:
        maxH = h[i]
        maxInd = i + 1
print(maxInd)

# 別解　最大の値があるインデックスを返すargmaxを使う
import numpy as np

N = int(input())
H = list(map(int, input().split()))
print(np.argmax(H) + 1)

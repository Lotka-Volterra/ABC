n = int(input())
ans = 0
for i in range(1, n+1, 2):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 8:
        ans += 1
print(ans)

# 約数の個数は、sqrt(n)まで調べれば十分。計算量O(n)をO(sqrt(n))にする
n = int(input())
ans = 0
for i in range(1, n+1, 2):
    count = 0
    for j in range(1, i+1):
        if j**2 > i:
            break
        if i % j == 0:
            k = i//j
            if j != k:
                count += 2
            else:
                count += 1
    print(i, count)
    if count == 8:
        ans += 1
print(ans)

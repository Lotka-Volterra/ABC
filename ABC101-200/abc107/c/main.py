n, k = map(int, input().split())
x = list(map(int, input().split()))
negative = [0]
non_negative = [0]
for i in range(n):
    if x[i] < 0:
        negative.append(abs(x[i]))
    else:
        non_negative.append(x[i])
negative.sort()
ans = float("inf")
for i in range(min(len(negative), k + 1)):
    if k - i >= len(non_negative):
        continue
    ans = min(
        negative[i] * 2 + non_negative[k - i],
        negative[i] + non_negative[k - i] * 2,
        ans,
    )
print(ans)

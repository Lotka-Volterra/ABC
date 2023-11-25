def makeArray(currentNum, maxNum, arrayLength, tempArray):
    if len(tempArray) == arrayLength:
        ans.append(tempArray.copy())
        return
    for i in range(currentNum, maxNum + 1):
        tempArray.append(i)
        makeArray(i, maxNum, arrayLength, tempArray)
        tempArray.pop()


ans = []
n, m, q = map(int, input().split())
makeArray(1, m, n, [])
score = [0] * len(ans)
for i in range(q):
    a, b, c, d = map(int, input().split())
    for j in range(len(ans)):
        if ans[j][b - 1] - ans[j][a - 1] == c:
            score[j] += d
print(max(score))

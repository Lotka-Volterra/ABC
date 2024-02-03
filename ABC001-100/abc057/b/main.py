n, m = map(int, input().split())
student = []
for i in range(n):
    a, b = map(int, input().split())
    student.append([a, b])
checkpoint = []
for i in range(m):
    c, d = map(int, input().split())
    checkpoint.append([c, d])
ans = []
for i in range(n):
    mindist = 10**9
    minInd = -1
    for j in range(m):
        dist = abs(student[i][0] - checkpoint[j][0]) + abs(
            student[i][1] - checkpoint[j][1]
        )
        if dist < mindist:
            mindist = dist
            minInd = j + 1
    ans.append(minInd)
for i in range(n):
    print(ans[i])

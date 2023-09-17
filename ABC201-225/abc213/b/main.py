n = int(input())
a = list(map(int, input().split()))
score = []
for i in range(n):
    score.append([a[i], i + 1])
score.sort(reverse=True)
print(score[1][1])

from collections import defaultdict

n, m = map(int, input().split())
A = []
for i in range(2 * n):
    a = input()
    A.append(a)
wins = defaultdict(int)
for i in range(2 * n):
    wins[i] = 0
for i in range(m):
    rank = []
    for k, v in wins.items():
        rank.append([m - v, k])
    rank.sort()
    for j in range(n):
        if A[rank[j * 2][1]][i] == "G" and A[rank[j * 2 + 1][1]][i] == "C":
            wins[rank[j * 2][1]] += 1
        elif A[rank[j * 2][1]][i] == "C" and A[rank[j * 2 + 1][1]][i] == "G":
            wins[rank[j * 2 + 1][1]] += 1
        elif A[rank[j * 2][1]][i] == "C" and A[rank[j * 2 + 1][1]][i] == "P":
            wins[rank[j * 2][1]] += 1
        elif A[rank[j * 2][1]][i] == "P" and A[rank[j * 2 + 1][1]][i] == "C":
            wins[rank[j * 2 + 1][1]] += 1
        elif A[rank[j * 2][1]][i] == "P" and A[rank[j * 2 + 1][1]][i] == "G":
            wins[rank[j * 2][1]] += 1
        elif A[rank[j * 2][1]][i] == "G" and A[rank[j * 2 + 1][1]][i] == "P":
            wins[rank[j * 2 + 1][1]] += 1
result = []
for k, v in wins.items():
    result.append([m - v, k])
result.sort()
for i in range(2 * n):
    print(result[i][1] + 1)

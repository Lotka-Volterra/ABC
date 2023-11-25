# 各人が参加した舞踏会の回を記録し、すべての二人の組み合わせについて、参加回の重複があるか確認
n, m = map(int, input().split())
nlist = [[] for i in range(n)]
for i in range(m):
    k = list(map(int, input().split()))
    for j in range(1,len(k)):
        nlist[k[j] - 1].append(i)
for i in range(n - 1):
    for j in range(i, n):
        if len(nlist[i] + nlist[j]) == len(list(set(nlist[i] + nlist[j]))):
            print("No")
            quit()
print("Yes")
n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
vote_line = sum(a)/(4*m)
for i in range(n):
    if a[i] >= vote_line:
        count += 1
if count >= m:
    print('Yes')
else:
    print('No')

# 別解　ソートして境界（M個目）だけ調べる
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)
if a[m-1] >= s/(4*m):
    print('Yes')
else:
    print('No')

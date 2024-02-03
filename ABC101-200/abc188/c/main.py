n = int(input())
a = list(map(int, input().split()))
a1 = a[:2**(n-1)]
a2 = a[2**(n-1):]
a1max = max(a1)
a2max = max(a2)
jun = min(a1max, a2max)
print(a.index(jun)+1)

#実装
#https://atcoder.jp/contests/abc188/submissions/19310202
N = int(input())
A = list(map(int, input().split()))
p = [(A[i], i + 1) for i in range(len(A))]
while len(p) > 2:
    p = [max(p[i * 2], p[i * 2 + 1]) for i in range(len(p) // 2)]
print(min(p)[1])

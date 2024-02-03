n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
aswap = a[1:p] + a[r : s + 1] + a[q + 1 : r] + a[p : q + 1] + a[s + 1 :]
print(*aswap)

# スライスして結合ではなく、区間を入れ替えでいい
N, P, Q, R, S = map(int, input().split())

A = list(map(int, input().split()))
A[P - 1 : Q], A[R - 1 : S] = A[R - 1 : S], A[P - 1 : Q]

print(*A)

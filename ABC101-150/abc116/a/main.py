abc = list(map(int, input().split()))
abc.sort()
print((abc[0]*abc[1])//2)

# ∠ABC=90°と条件があるので、ACが斜辺であることが確定している。
# そのためソートする必要はなく、AB,BCを掛けて2で割ればいい。
# ACは使わないが受け取っておこう

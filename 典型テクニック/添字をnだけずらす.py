# https://atcoder.jp/contests/abc314/editorial/6950
# 添字をkずらすときは、リストの要素数がnだとすると、
# (添字+k)%n とすればよい。
# (簡単のためにk<nとすると)たとえば0はkに、1はk+1になり、
# n-1（もともとのリストの末尾）は(n-1+k)%n=k-1と、前からk番目に移動する
n = 3
k = 1
a = [1, 2, 3]
for i in range(n):
    print(a[(i + k) % n])

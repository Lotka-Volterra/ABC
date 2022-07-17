n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]
print(alice-bob)

#aliceとbobを別々に考えるのではなく、aliceのときは足す、bobのときは引くと考えても良い
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
sa=0
for i in range(n):
    if i % 2 == 0:
        sa += a[i]
    else:
        sa -= a[i]
print(sa)

#c++ではもっと簡潔に書ける
#https://atcoder.jp/contests/abc088/submissions/2105068
n, k = map(int, input().split())
a = list(map(int, input().split()))
# k>=nの場合、要素数n、全ての要素が0の配列になる。
# k>=nでも、a[k:]のスライスはエラーにならない
a = a[k:] + [0] * min(n,k)
print(*a)

# for文で書く
N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(K):
  A = A[1:] + [0]
print(*A)


# popやappendを使う
N,K=map(int,input().split())
A=list(map(int,input().split()))

for _ in range(K):
  A.pop(0)     # Aの先頭(0番目)の要素を削除
  A.append(0)  # Aの末尾に0を追加

# 出力する
print(*A)

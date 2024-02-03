a = int(input())
b = int(input())
c = a % b
if c != 0:
    print(b-c)
else:
    print(c)

#別解 bが小さいのでaがbの倍数になるまでインクリメント
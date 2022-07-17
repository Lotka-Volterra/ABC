from socket import SOCK_NONBLOCK


X = int(input())
kyuryo = 0
for i in range(1, X+1):
    kyuryo += i
kyuryo = int(kyuryo*10000/X)
print(kyuryo)

# 別解　総和の書き方
N = int(input())
s = ((1 + N) * N / 2) * 10000 / N
# 別の総和の書き方
z = sum(range(N+1))

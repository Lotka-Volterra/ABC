b = int(input())
for i in range(1, 100):
    if i**i == b:
        print(i)
        quit()
print(-1)
# 0**0=1なので、b=1のとき、0を出力してしまうが、正の整数という条件なのでWA

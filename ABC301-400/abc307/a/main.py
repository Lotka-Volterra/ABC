n = int(input())
w = list(map(int, input().split()))
for i in range(n):
    print(sum(w[7 * i : 7 * (i + 1)]), end=" ")
# TODO:空白区切りの出力
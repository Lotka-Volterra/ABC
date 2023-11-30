# ABC201_B　公式解答 キー、値と受け取ったものを、値、キーと逆にして格納する。[n][0]で降順で並び替えると、値が大きい順に並ぶ
N = int(input())
data = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    data.append([T, S])
# reverse=Trueで大きい順に並ぶ
data.sort(reverse=True)
print(data[1][1])

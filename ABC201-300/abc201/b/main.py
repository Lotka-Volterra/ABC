N = int(input())

ST = {}
for i in range(N):
    n, m = input().split()
    m = int(m)
    ST[n] = m
    #辞書の値で並び替え（降順）
sorted_ST = sorted(ST.items(), key=lambda i: i[1], reverse = True)
print(sorted_ST[1][0])

#別解 1位の高さと２位の名前を変数に保存しながら回す
N = int(input())
top_height = 0
top_name = ""
sec_height = 0
sec_name = ""

for i in range(N):
    s,t = input().split()
    t = int(t)
    if t > top_height:
        sec_name = top_name
        sec_height = top_height
        #topを書き換えるのは、secを書き換えたあと
        top_name = s
        top_height = t
    elif t>sec_height:
        sec_height = t
        sec_name = s
print(sec_name)

#公式解答 キー、値と受け取ったものを、値、キーと逆にして格納する。[n][0]で降順で並び替えると、値が大きい順に並ぶ
N = int(input())
data = []
for i in range(N):
    S,T = map(str,input().split())
    T = int(T)
    data.append([T,S])
data.sort(reverse=True)
print(data[1][1])


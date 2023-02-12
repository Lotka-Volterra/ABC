# 数字のリストを文字列のリストに変換
m = list(range(1000))
# mapはmapオブジェクトを生成するのでリストに変換する
n = list(map(str, m))

print(n == 1 or 2)
# これは、(n==1)or(2)と解釈され、n==1 がTrueならTrueが返ってくる。
# Falseなら後ろの2が返ってくる、空ならFalseだが数字が入っているのでTrue
# TrueかFalseを絶対返してほしいならbool()
print(bool(2))
# True
print(bool())
# False

# 2数の大小比較で2数が異なる数なら、ifではなくmax()を使ったほうが短く書ける
if A > B:

#ABC167。末尾の一つ前までは:−1
if s==t[:-1]:
    print("Yes")
else:
    print("No")
#2数の大小比較で2数が異なる数なら、ifではなくmax()を使ったほうが短く書ける
if A>B:
    print(A)
else:
    print(B)

print(max(A, B))  # max 関数を用いて最大値を出力する

# A%10やB％10をなにかの変数に代入するのではなく、式ごと比較
if A % 10 < B % 10:
    print(A)
else:
    print(B)

# 1の位の比較＝10で割った余り
# AがBの倍数かどうか＝AがBで割り切れる

# Python で割り算を行う際に演算子 / を使うと、計算結果が小数型 (float 型) になってしまいます。
# 整数値を出力したい場合は、演算子 // を使いましょう。

# 文字列同士は、演算子 + を用いてつなげることができます。

# Python の場合文字列の一部の文字を単純に変更することはできません。
# そのため、文字列を配列型に変換してから要素を入れ替え、文字列型に戻す必要があります。
S = "algo"
S[0] = "b"  # エラーが発生する
# 文字を入れ替える方法はさまざまですが、ここでは「一時変数を用いる方法」を説明します。
S = input()  # 入力を文字列型として受け取る
N, M = map(int, input().split())  # 入力を整数型として受け取る
S_list = list(S)  # S を配列型に変換する
tmp = S_list[N-1]  # 一時変数に S_list[N-1] を代入する
S_list[N-1] = S_list[M-1]
S_list[M-1] = tmp
S = "".join(S_list)  # 配列の要素を結合して文字列型に変換する
print(S)

# 区切り文字.join(リスト)でリストの要素の結合。
list = ["a", "b", "c"]

print("".join(list))  # abc
print(",".join(list))  # a,b,c

# N個の文字を文字列配列として受け取る
N = int(input())  # 入力を整数型として受け取る
A = [""] * N
for i in range(N):
    A[i] = input()  # 入力を文字列型配列として受け取る

# for item in reversed(A): とすると配列を逆から処理することができます。
N = int(input())  # 入力を整数型として受け取る
A = list(map(int, input().split()))  # 入力を整数型配列として受け取る
for item in reversed(A):  # A の各要素に対して逆順に処理を行う
    print(item)

# 逆順に処理する別解　初期値、最終値、増分
for num in range(5, 2, -1):
    print(num)  # 5、4、3

# 配列の総和を求める関数sum()を使えば、平均がすぐに求まる
N = int(input())  # 入力を整数型として受け取る
A = list(map(int, input().split()))  # 入力を整数型配列として受け取る
print(int(sum(A)/N))  # 配列の平均値を求める

# input()で受け取った文字列の一文字目だけ使う場合
N = int(input())
target = ''
for x in range(N):
    target += input()[0]
print(target)

# 初期値が１の場合
count = 0
for i in range(1, N):
    if A[i-1] < A[i]:
        count += 1

# 最大値の線形探索、max関数を使うほうが速いが、以下は初期値をA[0]とおいて比較していく方法
maxnum = A[0]
for x in A:
    if x > maxnum:
        maxnum = x

# 線形探索 (最大値) indexで最大値を表す（count[index]）ことで変数をむやみに増やさない
index = 0
for i in range(9):
    if count[i] > count[index]:
        index = i

# 文字列の全探索　回文　逆順にするreversed()を使わなくてもS[(N-1)-i]でいい
# データを受け取る
S = input()

# S の長さを取得する
N = len(S)

# 線形探索
flag = True
for i in range(N):
    if S[i] != S[(N-1)-i]:
        flag = False

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")

# 文字列の全探索　文字のスライス
# データを受け取る
S = input()
T = input()

# S, T の長さを取得する
N = len(S)
M = len(T)

# 線形探索 (0 から N-M まで)
flag = False
for i in range(N-M+1):
    if S[i:i+M] == T:
        flag = True

# 答えを出力する
if flag:
    print("Yes")
else:
    print("No")

# ABC204_B
# 下限がある場合の実装は、maxを使えばいい（計算値が０以下なら０，０より大きいなら計算値）


# 素数かを判定する関数
def check_prime(x):
    is_prime = True
    if x == 1:
        is_prime = False
    else:
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
    return is_prime


# データを受け取る
N = int(input())
A = list(map(int, input().split()))

# 配列の全探索
counter = 0
for x in A:
    # 素数ならば 1 を足す
    if check_prime(x):
        counter += 1

# 答えを出力する
print(counter)

# 数字を空白区切りで出力するにはカンマを使う
print(a, b - 1)

# ABC067　B問題　sumとスライスを組み合わせる
N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
print(sum(l[-K:]))

# 別解　総和の書き方
N = int(input())
s = ((1 + N) * N / 2) * 10000 / N
# 別の総和の書き方
z = sum(range(N+1))

# データを受け取る
S = input()
N = len(S)

# aからzまでの全探索
# 文字の全探索
count = 0
for x in range(ord('a'), ord('z')+1):
    c = chr(x)
    # S に c が含まれるかを調べる
    flag = False
    for i in range(N):
        if S[i] == c:
            flag = True
    # S に c が含まれるならば 1 を足す
    if flag:
        count += 1

# 答えを出力する
print(count)

# ABC201_B　公式解答 キー、値と受け取ったものを、値、キーと逆にして格納する。[n][0]で降順で並び替えると、値が大きい順に並ぶ
N = int(input())
data = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    data.append([T, S])
data.sort(reverse=True)
print(data[1][1])

# ABC033_B。ABC201と同じような解き方で解いた。
# SとPというリストを別々に作り、インデックスで結びつける
n = int(input())
S = []
P = []
for _ in range(n):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
if max(P) > sum(P)//2:
    print(S[P.index(max(P))])
else:
    print("atcoder")

# ABC009_A　切り上げ（つまり、偶数なら２で割った時の商を出し、奇数なら２で割った時の商＋１を出す）
a = int(input())
print((a+1)//2)

# ABC002_B　母音を置き換える
w = input()
vowels = "aiueo"

for v in vowels:
    w = w.replace(v, "")

print(w)

# ABC002_B 書き換えるなら、if i in boinをif i not in boinにして、continueの部分をなくす
W = input()
boin = ["a", "i", "u", "e", "o"]
word = ""
for i in W:
    if i not in boin:
        word += i
print(word)

# ABC155_A 重複しない要素数が２個のときYesと考える。set()で重複のないリストを得て、その要素数をlen()で取得
l = list(map(int, input().split()))
if len(set(l)) == 2:
    print("Yes")
else:
    print("No")
#数字を空白区切りで出力するにはカンマを使う
print(a, b - 1)

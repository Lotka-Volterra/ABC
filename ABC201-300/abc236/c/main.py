n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
tind = 0
for i in range(n):
    if s[i] == t[tind]:
        print("Yes")
        tind = min(tind + 1, m - 1)
    else:
        print("No")

# 模範解答
# インデックスとか関係なく、集合に含まれていたらYes、含まれていなかったらNo
# 重複が無いことがわかっているリストでも、setに変換した方がいい
# in listはO(n)(リストの最後まで検索するため)、in setはO(1)(ハッシュテーブルで効率よく検索)
n, m = map(int, input().split())
s = input().split()
t = set(input().split())
for x in s:
    print("Yes" if x in t else "No")

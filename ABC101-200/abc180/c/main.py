import math

n = int(input())
ans = []
for i in range(1, math.ceil(math.sqrt(n)) + 1):
    if n % i == 0:
        ans.append(i)
        ans.append(n // i)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
# nが平方数のとき、sqrt(n)が2つはいってしまうので、setで重複排除した
# 下記のように、if文かましてもいい
# if i != n // i:
#     ans.append(n // i)
# あるいは最初からansをsetにして、ans.addで重複を自動で排除しながら追加する

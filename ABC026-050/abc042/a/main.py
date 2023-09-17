#最初に思いついた解答
l = list(map(int, input().split()))
l.sort()
if l[0] == 5 and l[1] == 5 and l[2] == 7:
    print("YES")
else:
    print("NO")

#次に思いついた解答
l = list(map(int, input().split()))
if l.count(5) == 2 and l.count(7) == 1:
    print("YES")
else:
    print("NO")

#最速の解答。ソートしてリスト自体の比較
l = list(map(int, input().split()))
l.sort()
if l == [5, 5, 7]:
    print("YES")
else:
    print("NO")

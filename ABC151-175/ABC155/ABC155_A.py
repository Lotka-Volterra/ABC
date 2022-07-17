l = list(map(int, input().split()))
l.sort()
if (l[0] == l[1] and l[0] != l[2]) or (l[2] == l[1] and l[2] != l[0]):
    print("Yes")
else:
    print("No")
#重複しない要素数が２個のときYesと考える。set()で重複のないリストを得て、その要素数をlen()で取得
l = list(map(int, input().split()))
if len(set(l))==2:
    print("Yes")
else:
    print("No")
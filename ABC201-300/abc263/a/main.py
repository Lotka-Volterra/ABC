a = list(map(int, input().split()))
a.sort()
if ((a[0] == a[1] == a[2]) and (a[3] == a[4]) and (a[2] != a[3])) or (
    (a[0] == a[1]) and (a[2] == a[3] == a[4]) and (a[1] != a[2])
):
    print("Yes")
else:
    print("No")

# 回答例　
# a[0]==a[1]==..=a[4]、つまり全ての入力が同じことはないため、昇順に並べたとき、
# 以下のどちらかが成立することがフルハウスの条件
# a[0] == a[2] and a[3] == a[4]
# a[0] == a[1] and a[2] == a[4]
a = list(map(int, input().split()))
a.sort()
if (a[0] == a[2] and a[3] == a[4]) or (a[0] == a[1] and a[2] == a[4]):
    print("Yes")
else:
    print("No")

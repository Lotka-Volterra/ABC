def kaisu(num, count):
    num.sort()
    sa1 = num[1] - num[0]
    sa2 = num[2] - num[1]
    # 全ての数の奇偶が揃っている場合、2つ目に大きい数まで、一番小さい数に2を足し、2つ目に大きい数と一番小さい数の両者に1ずつ足す
    return sa1 // 2 + sa2 + count


a = list(map(int, input().split()))
odd = []
even = []
a.sort()
for i in range(3):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
# 奇偶が揃っている場合
if len(odd) == 3 or len(even) == 3:
    a.sort()
    print(kaisu(a, 0))
# 奇偶が揃っていない場合
# 偶数が一つだけの場合
elif len(odd) == 1:
    print(kaisu(odd + [even[0] + 1, even[1] + 1], 1))
else:
    print(kaisu(even + [odd[0] + 1, odd[1] + 1], 1))

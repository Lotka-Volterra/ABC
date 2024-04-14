n = int(input())
s = input()
r_count = 0
r_list = []
for i in s:
    if i == "R":
        r_count += 1
    r_list.append(r_count)
# 目標は、前からR個をすべてRにすること。
# そのために、前からR個の石の中に赤い石が何個あるか数える
# 前からR個の石のうち、白い石を、前からR+1個以降にある赤い石と入れ替えれば最小になる。
# 入れ替えは赤い石の災いを消すと同時に白い石を救うため効率がいい
front_r = r_list[r_count - 1]
print(r_count - front_r)

s = input()
ints = []
for i in range(len(s)):
    ints.append(int(s[i]))
flag = False
if ints[0] == 0:
    # 4,5,6が立っている2つの場合
    if ints[3] + ints[4] == 2 and ints[1] + ints[7] == 0:
        flag = True
    elif ints[4] + ints[5] == 2 and ints[2] + ints[8] == 0:
        flag = True
    # 4,5,6が倒れている3つの場合
    elif ints[6] == 1 and ints[1] + ints[7] >= 1 and ints[3] == 0:
        flag = True
    elif ints[1] + ints[7] >= 1 and ints[2] + ints[8] >= 1 and ints[4] == 0:
        flag = True
    elif ints[2] + ints[8] >= 1 and ints[9] >= 1 and ints[5] == 0:
        flag = True
print(["No", "Yes"][flag])

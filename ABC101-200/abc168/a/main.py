# N の 1 の位が 2,4,5,7,9 のとき hon
# N の 1 の位が 0,1,6,8 のとき pon
# N の 1 の位が 3 のとき bon
hon = [2, 4, 5, 7, 9]
n = input()
if n[2] in hon:
    print("hon")
elif n[2] == "3":
    print("bon")
else:
    print("pon")

n = input()
if n[-1] == "3":
    print("bon")
elif n[-1] in "0168":
    print("pon")
else:
    print("hon")

#別解
#print('pphbhhphph'[int(input())%10]+'on')
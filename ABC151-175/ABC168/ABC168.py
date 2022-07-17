n = input()
if n[-1] == "3":
    print("bon")
elif n[-1] in "0168":
    print("pon")
else:
    print("hon")

#別解
#print('pphbhhphph'[int(input())%10]+'on')
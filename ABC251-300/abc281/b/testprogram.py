import string


def judge(s):
    if (
        len(s) == 8
        and s[0] in string.ascii_uppercase
        and s[7] in string.ascii_uppercase
        and ord("1") <= ord(s[1]) <= ord("9")
    ):
        for i in range(2, 7):
            if ord("0") > ord(s[i]) or ord("9") < ord(s[i]):
                return "No"
            return "Yes"
    return "No"

alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number=["0","1","2","3","4","5","6","7","8","9"]
numberWithout0=["1","2","3","4","5","6","7","8","9"]
allalphnum=alph+number
allalphnum.append("")
for a in alph:
    # for b in allalphnum:
    #     for c in allalphnum:
    #         for d in allalphnum:
    #             for e in allalphnum:
    #                 for f in allalphnum:
    #                     for g in allalphnum:
    for b in numberWithout0:
        for c in number:
            for d in number:
                for e in number:
                    for f in number:
                        for g in number:
                            for h in alph:                                
                                st=a+b+c+d+e+f+g+h
                                if judge(st) == "No":
                                    print(st)
print("end")
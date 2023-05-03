import string

s = input()
if len(s) != 8:
    print("No")
else:
    if s[0] not in string.ascii_uppercase or s[7] not in string.ascii_uppercase:
        print("No")
    elif int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        print("No")
    else:
        print("Yes")

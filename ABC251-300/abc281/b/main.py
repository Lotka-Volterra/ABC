import string

s = input()
if (
    len(s) == 8
    and s[0] in string.ascii_uppercase
    and s[7] in string.ascii_uppercase
    and ord("1") <= ord(s[1]) <= ord("9")
):
    for i in range(2, 7):
        if ord("0") > ord(s[i]) or ord("9") < ord(s[i]):
            print("No")
            quit()
    print("Yes")
    quit()
print("No")

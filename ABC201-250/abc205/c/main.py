a, b, c = map(int, input().split())
# a,bが両方非負整数
if a >= 0 and b >= 0:
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")
# a,bの片方が負で片方が0
elif a * b == 0:
    if c % 2 == 1:
        if a < b:
            print("<")
        else:
            print(">")
    else:
        if a < b:
            print(">")
        else:
            print("<")
# a,bの片方が正で片方が負
elif a * b < 0:
    if c % 2 == 1:
        if a < b:
            print("<")
        else:
            print(">")
    else:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
else:
    if c % 2 == 1:
        if a < b:
            print(">")
        else:
            print("<")
    else:
        if a < b:
            print("<")
        else:
            print("<")

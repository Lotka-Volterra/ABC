v, a, b, c = map(int, input().split())
amari = v % (a+b+c)
if amari < a:
    print("F")
elif amari < (a+b):
    print("M")
else:
    print("T")

a = input()
b = input()
if len(a) > len(b):
    print("GREATER")
    quit()
elif len(a) < len(b):
    print("LESS")
    quit()
else:
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            print("GREATER")
            quit()
        elif int(a[i]) < int(b[i]):
            print("LESS")
            quit()
print("EQUAL")

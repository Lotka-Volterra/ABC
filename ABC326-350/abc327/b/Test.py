def Seikai(b):
    for i in range(1, 100):
        if i**i == b:
            return i
    return -1


def Fuseikai(b):
    for i in range(1000):
        if i**i == b:
            return i
    return -1


for i in range(1, 10**18 + 1):
    if Seikai(i) != Fuseikai(i):
        print(i)

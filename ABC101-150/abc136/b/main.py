n = input()
if len(n) == 1:
    print(int(n))
elif len(n) == 2:
    print(9)
elif len(n) == 3:
    print(9 + int(n) - 99)
elif len(n) == 4:
    print(9 + 900)
elif len(n) == 5:
    print(909 + int(n) - 9999)
else:
    print(909 + 90000)

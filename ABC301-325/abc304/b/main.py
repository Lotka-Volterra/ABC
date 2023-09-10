n = int(input())
if n < 10**3:
    print(n)
else:
    for i in range(3, 9):
        if 10**i < n < 10 ** (i + 1) - 1:
            print(n - n % 10 ** (i - 2))

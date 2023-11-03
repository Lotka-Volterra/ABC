n = int(input())
for i in range(n, 920):
    if int(str(i)[0]) * int(str(i)[1]) == int(str(i)[2]):
        print(i)
        quit()

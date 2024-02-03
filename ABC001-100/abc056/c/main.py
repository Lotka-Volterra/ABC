x = int(input())
total = 0
for i in range(1, x + 1):
    total += i
    if total >= x:
        print(i)
        quit()

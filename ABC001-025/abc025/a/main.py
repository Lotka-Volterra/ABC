s = list(input())
n = int(input())

count = 0
for i in s:
    for j in s:
        count += 1
        if count == n:
            print(i+j)

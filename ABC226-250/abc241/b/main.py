n, m =  map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
eaten = [0] * n
for i in range(m):
    isExist = False
    for j in range(n):
        if a[j] == b[i] and eaten[j] == 0:
            eaten[j] = 1
            isExist = True
            break
    if not isExist:
        print("No")
        quit()
print("Yes")

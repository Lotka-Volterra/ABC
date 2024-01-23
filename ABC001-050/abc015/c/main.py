def xor_saiki(ans, count):
    global found
    if count < n:
        for i in range(k):
            xor_saiki(ans ^ T[count][i], count + 1)
    else:
        if ans == 0:
            found = True


n, k = map(int, input().split())
T = []
found = False
for i in range(n):
    T.append(list(map(int, input().split())))
for i in range(k):
    xor_saiki(T[0][i], 1)
    if found:
        print("Found")
        break
else:
    print("Nothing")

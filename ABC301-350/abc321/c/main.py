k = int(input())
count = 0
for i in range(1, 9876543211):
    strI = str(i)
    is321Like = True
    for j in range(len(strI) - 1):
        if int(strI[j]) <= int(strI[j + 1]):
            is321Like = False
            break
    if is321Like:
        count += 1
    if count == k:
        print(i)
        quit()
